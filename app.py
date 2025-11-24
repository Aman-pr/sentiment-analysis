"""
Main Streamlit application for AI Chatbot with Sentiment Analysis
"""
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

# Import custom modules
from database import (
    init_database, create_session, save_message, 
    load_session_messages, get_all_sessions, delete_session
)
from ai_models import (
    analyze_sentiment, analyze_conversation_sentiment, generate_response
)
from styles import get_custom_css

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="centered")

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize database
if "db_initialized" not in st.session_state:
    init_database()
    st.session_state.db_initialized = True

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False
if "session_id" not in st.session_state:
    st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    create_session(st.session_state.session_id)
if "delete_mode" not in st.session_state:
    st.session_state.delete_mode = False

# Header
st.markdown("""
    <div class="chat-header">
        <h1>AI Chatbot</h1>
        <p>Real-time Sentiment Analysis with Database Storage</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Controls")
    
    if st.button("New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_ended = False
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        create_session(st.session_state.session_id)
        st.rerun()
    
    if st.button("End Chat & Full Analysis", use_container_width=True, type="primary"):
        if len(st.session_state.messages) > 0:
            st.session_state.chat_ended = True
            st.rerun()
        else:
            st.warning("Start chatting first!")
    
    st.markdown("---")
    
    # Real-time stats - SMALLER
    st.markdown("### Analysis")
    user_message_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    
    if st.session_state.messages:
        # Count sentiments
        sentiments = [msg.get("sentiment", {}).get("sentiment", "") for msg in st.session_state.messages if msg["role"] == "user" and "sentiment" in msg]
        if sentiments:
            positive_count = sentiments.count("Positive")
            negative_count = sentiments.count("Negative")
            neutral_count = sentiments.count("Neutral")
            
            # Stack metrics vertically
            st.metric("Positive", positive_count)
            st.metric("Negative", negative_count)
            st.metric("Neutral", neutral_count)
    
    st.markdown("---")
    
    # Previous sessions - ChatGPT style
    with st.expander("Previous Chats", expanded=True):
        sessions = get_all_sessions()
        
        if sessions:
            for session_id_item, title, created_at, msg_count in sessions:
                is_current = session_id_item == st.session_state.session_id
                
                cols = st.columns([10, 1])
                
                with cols[0]:
                    if st.button(
                        title,
                        key=f"load_{session_id_item}",
                        use_container_width=True,
                        type="primary" if is_current else "secondary",
                        disabled=is_current
                    ):
                        if not is_current:
                            # Load session
                            st.session_state.session_id = session_id_item
                            st.session_state.messages = []
                            st.session_state.chat_ended = False
                            
                            # Load messages from database
                            db_messages = load_session_messages(session_id_item)
                            for role, message, sentiment, polarity, subjectivity, timestamp in db_messages:
                                msg = {"role": role, "content": message}
                                if sentiment:
                                    msg["sentiment"] = {
                                        "sentiment": sentiment,
                                        "polarity": polarity,
                                        "subjectivity": subjectivity,
                                        "color_class": f"sentiment-{sentiment.lower()}"
                                    }
                                st.session_state.messages.append(msg)
                            
                            st.rerun()
                
                with cols[1]:
                    if st.button("×", key=f"del_{session_id_item}", use_container_width=True):
                        if delete_session(session_id_item):
                            if is_current:
                                st.session_state.messages = []
                                st.session_state.chat_ended = False
                                st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
                                create_session(st.session_state.session_id)
                            st.rerun()
        else:
            st.info("No saved chats yet")
    
    st.markdown("---")
    st.caption("Powered by LangChain + Groq")
    st.caption("SQLite Database Storage")

# Main chat area
if not st.session_state.chat_ended:
    # Load messages from database if empty
    if not st.session_state.messages:
        db_messages = load_session_messages(st.session_state.session_id)
        for role, message, sentiment, polarity, subjectivity, timestamp in db_messages:
            msg = {"role": role, "content": message}
            if sentiment:
                msg["sentiment"] = {
                    "sentiment": sentiment,
                    "polarity": polarity,
                    "subjectivity": subjectivity,
                    "color_class": f"sentiment-{sentiment.lower()}"
                }
            st.session_state.messages.append(msg)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
            # Show sentiment for user messages
            if message["role"] == "user" and "sentiment" in message:
                sent_data = message["sentiment"]
                st.markdown(f"""
                    <div class="sentiment-badge {sent_data['color_class']}">
                        {sent_data['sentiment']} | {sent_data['polarity']:.2f}
                    </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Analyze sentiment immediately
        sentiment_data = analyze_sentiment(prompt)
        
        # Save to database
        save_message(
            st.session_state.session_id,
            "user",
            prompt,
            sentiment_data['sentiment'],
            sentiment_data['polarity'],
            sentiment_data['subjectivity']
        )
        
        # Add user message with sentiment
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt,
            "sentiment": sentiment_data
        })
        
        with st.chat_message("user"):
            st.write(prompt)
            st.markdown(f"""
                <div class="sentiment-badge {sentiment_data['color_class']}">
                    {sentiment_data['sentiment']} | {sentiment_data['polarity']:.2f}
                </div>
            """, unsafe_allow_html=True)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, st.session_state.messages)
                st.write(response)
        
        # Save assistant response to database
        save_message(st.session_state.session_id, "assistant", response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

else:
    # Show full conversation analysis
    st.markdown("## Conversation Analysis")
    
    analysis = analyze_conversation_sentiment(st.session_state.messages)
    
    if analysis:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Overall Sentiment", analysis["sentiment"])
        
        with col2:
            st.metric("Polarity Score", f"{analysis['polarity']:.2f}")
            st.caption("Range: -1 to +1")
        
        with col3:
            st.metric("Messages Analyzed", analysis["message_count"])
        
        # Visualization
        st.markdown("### Sentiment Breakdown")
        
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#1a1a1a')
        ax.set_facecolor('#1a1a1a')
        
        categories = ['Polarity', 'Subjectivity']
        values = [abs(analysis['polarity']), analysis['subjectivity']]
        colors = [analysis['color'], '#60a5fa']
        
        bars = ax.barh(categories, values, color=colors, alpha=0.8)
        ax.set_xlabel('Score', color='white')
        ax.set_title('Sentiment Metrics', color='white', fontsize=14, pad=20)
        ax.set_xlim(0, 1)
        ax.tick_params(colors='white')
        ax.spines['bottom'].set_color('#333')
        ax.spines['top'].set_color('#333')
        ax.spines['right'].set_color('#333')
        ax.spines['left'].set_color('#333')
        
        st.pyplot(fig)
        
        # Interpretation
        st.markdown("### Interpretation")
        
        if analysis['polarity'] > 0.1:
            interpretation = "Your conversation had a positive tone. You expressed optimism and satisfaction."
        elif analysis['polarity'] < -0.1:
            interpretation = "Your conversation had a negative tone. You may have expressed concerns or dissatisfaction."
        else:
            interpretation = "Your conversation was neutral. You maintained a balanced and objective tone."
        
        st.info(interpretation)
        
        # Show conversation history
        with st.expander("View Conversation History"):
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    sentiment_info = ""
                    if "sentiment" in msg:
                        sentiment_info = f" [{msg['sentiment']['sentiment']}]"
                    st.markdown(f"**You{sentiment_info}:** {msg['content']}")
                else:
                    st.markdown(f"**Bot:** {msg['content']}")
                st.markdown("---")
    
    else:
        st.warning("No messages to analyze. Start a new chat!")
    
    if st.button("Start New Conversation", type="primary", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_ended = False
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        create_session(st.session_state.session_id)
        st.rerun()
