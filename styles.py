"""
CSS styles for the chatbot interface
"""

def get_custom_css():
    """Return custom CSS styling"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0a0a0a;
        color: #e5e5e5;
    }
    
    .chat-header {
        text-align: center;
        padding: 30px 20px;
        background: #1a1a1a;
        color: #ffffff;
        border-radius: 12px;
        margin-bottom: 30px;
        border: 1px solid #2a2a2a;
    }
    
    .chat-header h1 {
        font-weight: 600;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
        color: #ffffff;
    }
    
    .chat-header p {
        opacity: 0.6;
        font-weight: 400;
        color: #999;
    }
    
    .sentiment-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 16px;
        font-size: 0.65rem;
        font-weight: 600;
        margin-top: 6px;
        letter-spacing: 0.3px;
        text-transform: uppercase;
    }
    
    .sentiment-positive {
        background-color: #1a3a1a;
        color: #4ade80;
        border: 1px solid #2d5a2d;
    }
    
    .sentiment-negative {
        background-color: #3a1a1a;
        color: #f87171;
        border: 1px solid #5a2d2d;
    }
    
    .sentiment-neutral {
        background-color: #3a2d1a;
        color: #fbbf24;
        border: 1px solid #5a4a2d;
    }
    
    [data-testid="stSidebar"] {
        background-color: #0f0f0f;
        border-right: 1px solid #2a2a2a;
        padding-top: 2rem;
    }
    
    [data-testid="stSidebar"] * {
        color: #e5e5e5 !important;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h3 {
        font-weight: 600;
        letter-spacing: -0.3px;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    [data-testid="stSidebar"] .stExpander {
        background-color: transparent;
        border: none;
        border-radius: 0;
        margin-bottom: 0;
    }
    
    [data-testid="stSidebar"] .stExpander > div > div {
        padding: 0 !important;
    }
    
    [data-testid="stSidebar"] .element-container {
        margin-bottom: 0 !important;
    }
    
    [data-testid="stSidebar"] [data-testid="column"] {
        padding: 0 !important;
        gap: 0 !important;
    }
    
    [data-testid="stSidebar"] .row-widget {
        gap: 0 !important;
        margin-bottom: 2px !important;
    }
    
    [data-testid="stSidebar"] .stButton {
        margin: 0 !important;
    }
    
    [data-testid="stSidebar"] .stButton button {
        border-radius: 8px !important;
        border: none !important;
        background-color: transparent !important;
        transition: background-color 0.2s ease;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #2a2a2a !important;
    }
    
    [data-testid="stSidebar"] .stButton button[kind="primary"] {
        background-color: #2a2a2a !important;
    }
    
    [data-testid="stSidebar"] .stButton button[kind="primary"]:hover {
        background-color: #353535 !important;
    }
    
    [data-testid="stSidebar"] .stButton button:disabled {
        background-color: #2a2a2a !important;
    }
    
    [data-testid="stSidebar"] .row-widget:hover {
        background-color: #2a2a2a;
        border-radius: 8px;
    }
    
    [data-testid="stSidebar"] [data-testid="column"]:last-child button {
        opacity: 0;
        transition: opacity 0.2s ease;
    }
    
    [data-testid="stSidebar"] .row-widget:hover [data-testid="column"]:last-child button {
        opacity: 1;
    }
    
    .stChatMessage {
        background-color: #1a1a1a !important;
        border: 1px solid #2a2a2a;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
    }
    
    .stChatMessage p {
        color: #e5e5e5 !important;
        line-height: 1.6;
    }
    
    [data-testid="stChatInput"] {
        background-color: #1a1a1a;
        border: 1px solid #3a3a3a;
        border-radius: 12px;
        padding: 2px;
    }
    
    [data-testid="stChatInput"] textarea {
        background-color: #1a1a1a !important;
        color: #e5e5e5 !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 0.95rem;
        padding: 14px 16px !important;
        line-height: 1.5;
        min-height: 52px !important;
    }
    
    [data-testid="stChatInput"] textarea:focus {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    [data-testid="stChatInput"]:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }
    
    [data-testid="stChatInput"] textarea::placeholder {
        color: #666 !important;
    }
    
    .stButton button {
        background-color: #1f1f1f;
        color: #e5e5e5;
        border: 1px solid #3a3a3a;
        border-radius: 8px;
        width: 100%;
        font-weight: 400;
        padding: 0.6rem 0.7rem;
        transition: all 0.2s ease;
        font-size: 0.85rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        text-align: left;
    }
    
    .stButton button:hover {
        background-color: #2a2a2a;
        border-color: #4a4a4a;
    }
    
    .stButton button[kind="primary"] {
        background-color: #3b82f6;
        color: #ffffff;
        border: none;
        padding: 0.6rem 0.7rem;
    }
    
    .stButton button[kind="primary"]:hover {
        background-color: #2563eb;
    }
    
    .stButton button:disabled {
        background-color: #2a2a2a;
        color: #666;
        border-color: transparent;
        padding: 0.6rem 0.7rem;
    }
    
    [data-testid="stMetric"] {
        background-color: #1a1a1a;
        padding: 6px;
        border-radius: 6px;
        border: 1px solid #3a3a3a;
        margin-bottom: 4px;
    }
    
    [data-testid="stMetricLabel"] {
        color: #888 !important;
        font-size: 0.65rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetricValue"] {
        color: #e5e5e5 !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    hr {
        border: none;
        height: 1px;
        background-color: #2a2a2a;
        margin: 1.5rem 0;
    }
    
    .stMarkdown {
        color: #e5e5e5;
    }
    
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
        letter-spacing: -0.5px;
    }
    
    .stSelectbox > div > div {
        background-color: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 8px;
        color: #e5e5e5;
    }
    
    .stSpinner > div {
        border-color: #e5e5e5 transparent transparent transparent;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #3a3a3a;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #4a4a4a;
    }
    </style>
    """
