# AI Chatbot with Sentiment Analysis

A conversational AI chatbot with real-time sentiment analysis, built using LangChain, Groq API, and Streamlit.

## Features

- Real-time chat interface with AI responses
- Sentiment analysis for each user message
- Conversation history stored in SQLite database
- Full conversation sentiment analysis
- Dark minimalistic UI

## Prerequisites

- Python 3.11+
- Groq API key

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-chatbot-sentiment.git
cd ai-chatbot-sentiment
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Download TextBlob data
```bash
python -m textblob.download_corpora
```

4. Set environment variable
```bash
export GROQ_API_KEY="your-groq-api-key"
```

## Usage

Run the application:
```bash
streamlit run app.py
```

## Project Structure

```
.
├── app.py              
├── database.py         
├── ai_models.py       
├── styles.py          
├── requirements.txt   
└── README.md         
```

## Configuration

The chatbot uses:
- Model: Groq
- Database: SQLite (chatbot_history.db)
- Sentiment: TextBlob

## Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add GROQ_API_KEY in secrets
4. Deploy

### Render

1. Create new Web Service
2. Connect GitHub repository
3. Add environment variable: GROQ_API_KEY
4. Deploy

## License

MIT License
