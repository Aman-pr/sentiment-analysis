import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
from textblob import TextBlob
import os

@st.cache_resource
def get_chatbot():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY missing add it to your env vars. Chat part won't work, but sentiment still does.")
        st.stop()
    
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1024
    )

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        sentiment = "Positive"
        color_class = "sentiment-positive"
    elif polarity < -0.1:
        sentiment = "Negative"
        color_class = "sentiment-negative"
    else:
        sentiment = "Neutral"
        color_class = "sentiment-neutral"
    
    return {
        "sentiment": sentiment,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "color_class": color_class
    }

def analyze_conversation_sentiment(messages):
    user_messages = [msg["content"] for msg in messages if msg["role"] == "user"]
    
    if not user_messages:
        return None
    
    full_text = " ".join(user_messages)
    blob = TextBlob(full_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        sentiment = "Positive"
        color = "#4ade80"
    elif polarity < -0.1:
        sentiment = "Negative"
        color = "#f87171"
    else:
        sentiment = "Neutral"
        color = "#fbbf24"
    
    return {
        "sentiment": sentiment,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "color": color,
        "message_count": len(user_messages)
    }

def generate_response(user_message, chat_history):
    try:
        chatbot = get_chatbot()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a friendly and helpful AI assistant. Keep responses conversational and concise."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        history = []
        for msg in chat_history[-6:]:
            if msg["role"] == "user":
                history.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                history.append(AIMessage(content=msg["content"]))
        
        chain = prompt | chatbot
        response = chain.invoke({
            "chat_history": history,
            "input": user_message
        })
        
        return response.content
    
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
