from typing import List
from langchain_core.tools import tool
from db.parent_store_manager import ParentStoreManager

class ToolFactory:
    
    def __init__(self, collection):
        self.collection = collection
        self.parent_store_manager = ParentStoreManager()
    
    def _search_child_chunks(self, query: str, k: int) -> List[dict]:
        """Search for the top K most relevant child chunks.

        Args:
            query: Search query string
            k: Number of results to return
        """
        try:
            # 降低相似度阈值，从0.7降到0.3，更容易找到相关内容
            results = self.collection.similarity_search(query, k=k, score_threshold=0.3)

            if not results:
                print(f"⚠️ 未找到相似度>0.3的结果，尝试无阈值检索...")
                # 兜底：如果阈值过滤后没有结果，去掉阈值重新检索
                results = self.collection.similarity_search(query, k=k)

            print(f"✅ 检索到 {len(results)} 个相关片段")
            return [
                {
                    "content": doc.page_content,
                    "parent_id": doc.metadata.get("parent_id", ""),
                    "source": doc.metadata.get("source", "")
                }
                for doc in results
            ]
        except Exception as e:
            print(f"❌ 检索错误: {e}")
            return []
    
    def _retrieve_parent_chunks(self, parent_ids: List[str]) -> List[dict]:
        """Retrieve full parent chunks by their IDs.
    
        Args:
            parent_ids: List of parent chunk IDs to retrieve
        """
        return self.parent_store_manager.load_many(parent_ids)
    
    def create_tools(self) -> List:
        """Crea e restituisce la lista di tools."""
        search_tool = tool("search_child_chunks")(self._search_child_chunks)
        retrieve_tool = tool("retrieve_parent_chunks")(self._retrieve_parent_chunks)
        
        return [search_tool, retrieve_tool]