"""
Database operations for chatbot history
"""
import sqlite3
from datetime import datetime

def init_database():
    """Initialize SQLite database"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    # Create conversations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            sentiment TEXT,
            polarity REAL,
            subjectivity REAL
        )
    ''')
    
    # Create sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            title TEXT,
            message_count INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

def create_session(session_id):
    """Create a new session in database"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    # Create title with just date and time
    title = datetime.now().strftime("%b %d, %I:%M %p")
    
    cursor.execute('''
        INSERT OR IGNORE INTO sessions (session_id, title)
        VALUES (?, ?)
    ''', (session_id, title))
    
    conn.commit()
    conn.close()

def save_message(session_id, role, message, sentiment=None, polarity=None, subjectivity=None):
    """Save a message to database"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO conversations (session_id, role, message, sentiment, polarity, subjectivity)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (session_id, role, message, sentiment, polarity, subjectivity))
    
    # Update message count
    cursor.execute('''
        UPDATE sessions 
        SET message_count = message_count + 1
        WHERE session_id = ?
    ''', (session_id,))
    
    conn.commit()
    conn.close()

def load_session_messages(session_id):
    """Load all messages from a session"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT role, message, sentiment, polarity, subjectivity, timestamp
        FROM conversations
        WHERE session_id = ?
        ORDER BY id ASC
    ''', (session_id,))
    
    messages = cursor.fetchall()
    conn.close()
    return messages

def get_all_sessions():
    """Get all sessions from database"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT session_id, title, created_at, message_count
        FROM sessions
        ORDER BY created_at DESC
        LIMIT 20
    ''')
    
    sessions = cursor.fetchall()
    conn.close()
    return sessions

def delete_session(session_id):
    """Delete a session and its messages"""
    conn = sqlite3.connect('chatbot_history.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM conversations WHERE session_id = ?', (session_id,))
    cursor.execute('DELETE FROM sessions WHERE session_id = ?', (session_id,))
    
    conn.commit()
    conn.close()
