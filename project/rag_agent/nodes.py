from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage, AIMessage
from .graph_state import State, AgentState
from .schemas import QueryAnalysis
from .prompts import *

def analyze_chat_and_summarize(state: State, llm):
    if len(state["messages"]) < 4:
        return {"conversation_summary": ""}
    
    relevant_msgs = [
        msg for msg in state["messages"][:-1]
        if isinstance(msg, (HumanMessage, AIMessage))
        and not getattr(msg, "tool_calls", None)
    ]

    if not relevant_msgs:
        return {"conversation_summary": ""}
    
    conversation = "Conversation history:\n"
    for msg in relevant_msgs[-6:]:
        role = "User" if isinstance(msg, HumanMessage) else "Assistant"
        conversation += f"{role}: {msg.content}\n"

    summary_response = llm.with_config(temperature=0.2).invoke([SystemMessage(content=get_conversation_summary_prompt())] + [HumanMessage(content=conversation)])
    return {"conversation_summary": summary_response.content, "agent_answers": [{"__reset__": True}]}

def analyze_and_rewrite_query(state: State, llm):
    last_message = state["messages"][-1]
    conversation_summary = state.get("conversation_summary", "")

    context_section = (f"Conversation Context:\n{conversation_summary}\n" if conversation_summary.strip() else "") + f"User Query:\n{last_message.content}\n"

    # 手动JSON方式：让LLM返回JSON文本
    json_prompt = get_query_analysis_prompt() + """

IMPORTANT: You must respond with a valid JSON object in this exact format:
{
  "is_clear": true,
  "questions": ["question1", "question2"],
  "clarification_needed": "explanation if unclear"
}

Do not include any other text, only the JSON."""

    try:
        response = llm.with_config(temperature=0.1).invoke(
            [SystemMessage(content=json_prompt)] +
            [HumanMessage(content=context_section)]
        )

        # 手动解析JSON
        import json
        response_text = response.content.strip()

        # 尝试提取JSON（处理可能的markdown代码块）
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()

        parsed = json.loads(response_text)

        if len(parsed.get("questions", [])) > 0 and parsed.get("is_clear", False):
            delete_all = [
                RemoveMessage(id=m.id)
                for m in state["messages"]
                if not isinstance(m, SystemMessage)
            ]
            return {
                "questionIsClear": True,
                "messages": delete_all,
                "originalQuery": last_message.content,
                "rewrittenQuestions": parsed["questions"]
            }
        else:
            clarification = parsed.get("clarification_needed", "")
            if not clarification or len(clarification.strip()) < 10:
                clarification = "I need more information to understand your question."
            return {
                "questionIsClear": False,
                "messages": [AIMessage(content=clarification)]
            }

    except json.JSONDecodeError as e:
        print(f"❌ JSON解析错误: {e}")
        print(f"LLM返回: {response.content[:200]}...")
        # 兜底：使用原始问题
        return {
            "questionIsClear": True,
            "messages": [],
            "originalQuery": last_message.content,
            "rewrittenQuestions": [last_message.content]
        }
    except Exception as e:
        print(f"❌ 查询分析错误: {e}")
        import traceback
        traceback.print_exc()
        # 兜底：使用原始问题
        return {
            "questionIsClear": True,
            "messages": [],
            "originalQuery": last_message.content,
            "rewrittenQuestions": [last_message.content]
        }

def human_input_node(state: State):
    return {}

def agent_node(state: AgentState, llm_with_tools):
    sys_msg = SystemMessage(content=get_rag_agent_prompt())    
    if not state.get("messages"):
        human_msg = HumanMessage(content=state["question"])
        response = llm_with_tools.invoke([sys_msg] + [human_msg])
        return {"messages": [human_msg, response]}
    
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

def extract_final_answer(state: AgentState):
    for msg in reversed(state["messages"]):
        if isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
            res = {
                "final_answer": msg.content,
                "agent_answers": [{
                    "index": state["question_index"],
                    "question": state["question"],
                    "answer": msg.content
                }]
            }
            return res
    return {
        "final_answer": "Unable to generate an answer.",
        "agent_answers": [{
            "index": state["question_index"],
            "question": state["question"],
            "answer": "Unable to generate an answer."
        }]
    }

def aggregate_responses(state: State, llm):
    if not state.get("agent_answers"):
        return {"messages": [AIMessage(content="No answers were generated.")]}

    sorted_answers = sorted(state["agent_answers"], key=lambda x: x["index"])

    formatted_answers = ""
    for i, ans in enumerate(sorted_answers, start=1):
        formatted_answers += (f"\nAnswer {i}:\n"f"{ans['answer']}\n")

    user_message = HumanMessage(content=f"""Original user question: {state["originalQuery"]}\nRetrieved answers:{formatted_answers}""")
    synthesis_response = llm.invoke([SystemMessage(content=get_aggregation_prompt())] + [user_message])
    
    return {"messages": [AIMessage(content=synthesis_response.content)]}