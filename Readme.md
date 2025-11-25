# AI Chatbot with Sentiment Analysis

A conversational AI chatbot with real-time sentiment analysis, built using LangChain, Groq API, and Streamlit.

## Features
 
- Real-time chat sentiment analysis for each user message
- Full conversation sentiment analysis
- Real-time chat interface with AI responses
- Conversation history stored in SQLite database

## Demo 
[Sentiment Analysis : Click here ](https://sentiment-analysis-avaz3kccgihk2wthaquwps.streamlit.app/)
## Prerequisites

- Python 3.11+
- Groq API key

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-chatbot-sentiment.git
cd ai-chatbot-sentiment
```

2. Create a Python virtual environment
```bash
python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows
```
   
4. Install dependencies
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
- Sentiment: TextBlob for Sentiment Analysis
- Model: Langchain framework (Groq) for communication
- Database: SQLite (chatbot_history.db)
- Frontend: Streamlit 


## Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add GROQ_API_KEY in secrets
4. Deploy



## License

MIT License
