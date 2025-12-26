custom_css = """
    /* ============================================
       MODERN CLEAN THEME - 高对比度清爽配色
       ============================================ */

    /* 进度条隐藏 */
    .progress-text {
        display: none !important;
    }

    /* ============================================
       主容器 - 浅色背景
       ============================================ */
    .gradio-container {
        max-width: 1200px !important;
        width: 100% !important;
        margin: 0 auto !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        background: #f8fafc !important;
    }

    /* ============================================
       标签页 - 现代风格
       ============================================ */
    button[role="tab"] {
        color: #64748b !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 3px solid transparent !important;
        border-radius: 8px 8px 0 0 !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        transition: all 0.25s ease !important;
    }

    button[role="tab"]:hover {
        color: #3b82f6 !important;
        background: rgba(59, 130, 246, 0.08) !important;
    }

    button[role="tab"][aria-selected="true"] {
        color: #2563eb !important;
        background: white !important;
        border-bottom: 3px solid #2563eb !important;
    }

    /* 标签页容器 */
    .tabs {
        border-bottom: 1px solid #e2e8f0 !important;
        background: white !important;
    }

    /* 文档管理标签页居中 */
    #doc-management-tab {
        max-width: 800px !important;
        margin: 0 auto !important;
    }

    /* ============================================
       按钮样式 - 现代渐变
       ============================================ */
    button {
        border-radius: 10px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08) !important;
    }

    button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.12) !important;
    }

    /* 主要按钮 - 蓝色渐变 */
    .primary {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        padding: 12px 28px !important;
        font-size: 15px !important;
    }

    .primary:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3) !important;
    }

    /* 危险按钮 - 红色渐变 */
    .stop {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
        color: white !important;
        padding: 12px 28px !important;
        font-size: 15px !important;
    }

    .stop:hover {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
        box-shadow: 0 6px 16px rgba(220, 38, 38, 0.3) !important;
    }

    /* 次要按钮 */
    button:not(.primary):not(.stop) {
        background: white !important;
        color: #475569 !important;
        border: 2px solid #cbd5e1 !important;
        padding: 12px 28px !important;
        font-size: 15px !important;
    }

    button:not(.primary):not(.stop):hover {
        background: #f8fafc !important;
        border-color: #94a3b8 !important;
        color: #1e293b !important;
    }

    /* ============================================
       输入框和文本框 - 清爽白色
       ============================================ */
    input, textarea {
        background: white !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        color: #1e293b !important;
        font-size: 15px !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
    }

    input:focus, textarea:focus {
        border-color: #3b82f6 !important;
        outline: none !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
        background: #fafbfc !important;
    }

    textarea[readonly] {
        background: #f1f5f9 !important;
        color: #334155 !important;
        border-color: #cbd5e1 !important;
    }

    /* ============================================
       文件上传区 - 现代卡片风格
       ============================================ */
    .file-preview,
    [data-testid="file-upload"] {
        background: white !important;
        border: 2px dashed #cbd5e1 !important;
        border-radius: 16px !important;
        min-height: 200px !important;
        transition: all 0.3s ease !important;
    }

    .file-preview:hover,
    [data-testid="file-upload"]:hover {
        border-color: #3b82f6 !important;
        background: #f8fafc !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1) !important;
    }

    /* 文件上传文字 */
    .file-preview *,
    [data-testid="file-upload"] * {
        color: #475569 !important;
    }

    .file-preview:hover *,
    [data-testid="file-upload"]:hover * {
        color: #3b82f6 !important;
    }

    /* ============================================
       文件列表框
       ============================================ */
    #file-list-box {
        background: white !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
    }

    #file-list-box textarea {
        background: transparent !important;
        border: none !important;
        color: #334155 !important;
        padding: 0 !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }

    /* ============================================
       聊天输入框
       ============================================ */
    textarea[placeholder="Type a message..."] {
        background: white !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 24px !important;
        padding: 14px 20px !important;
        font-size: 15px !important;
        color: #1e293b !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
    }

    textarea[placeholder="Type a message..."]:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1), 0 2px 8px rgba(0,0,0,0.04) !important;
    }

    /* 聊天提交按钮 */
    form:has(textarea[placeholder="Type a message..."]) button[type="submit"] {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50% !important;
        width: 44px !important;
        height: 44px !important;
        padding: 0 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }

    form:has(textarea[placeholder="Type a message..."]) button[type="submit"]:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3) !important;
    }

    /* ============================================
       聊天气泡 - 现代气泡风格
       ============================================ */
    .chatbot {
        background: transparent !important;
        border: none !important;
    }

    .message {
        border-radius: 20px !important;
        padding: 14px 20px !important;
        max-width: 80% !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }

    .message.user {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        margin-left: auto !important;
        border-bottom-right-radius: 6px !important;
    }

    .message.bot {
        background: white !important;
        color: #1e293b !important;
        border: 2px solid #e2e8f0 !important;
        border-bottom-left-radius: 6px !important;
    }

    /* ============================================
       标题文字
       ============================================ */
    h1, h2, h3, h4, h5, h6 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }

    h1 { font-size: 32px !important; }
    h2 { font-size: 26px !important; }
    h3 { font-size: 22px !important; }

    /* Markdown内容 */
    .markdown {
        color: #334155 !important;
        line-height: 1.7 !important;
    }

    /* ============================================
       进度条
       ============================================ */
    .progress-bar-wrap {
        border-radius: 10px !important;
        overflow: hidden !important;
        background: #e2e8f0 !important;
        height: 8px !important;
    }

    .progress-bar {
        border-radius: 10px !important;
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%) !important;
        height: 100% !important;
        transition: width 0.3s ease !important;
    }

    /* ============================================
       全局优化
       ============================================ */
    * {
        box-shadow: none !important;
    }

    /* 隐藏底部Gradio标志 */
    footer {
        visibility: hidden !important;
        height: 0 !important;
    }

    /* 滚动条美化 */
    ::-webkit-scrollbar {
        width: 10px !important;
        height: 10px !important;
    }

    ::-webkit-scrollbar-track {
        background: #f1f5f9 !important;
        border-radius: 10px !important;
    }

    ::-webkit-scrollbar-thumb {
        background: #cbd5e1 !important;
        border-radius: 10px !important;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8 !important;
    }

    /* ============================================
       卡片和容器
       ============================================ */
    .gradio-container {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
    }

    /* 增加卡片阴影 */
    [class*="container"] {
        box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
    }
"""