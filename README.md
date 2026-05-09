# FlowSync AeroCore OS

An autonomous multi-agent AI workflow system built for AgentHon Hackathon.

## Features

- Multi-agent architecture
- AI workflow orchestration
- Research agent
- Documentation agent
- Productivity workflows
- Retry engine
- Planner system
- FastAPI backend
- Streamlit frontend
- Groq LLM integration

## Tech Stack

- Python
- FastAPI
- Streamlit
- Groq API

## Run Locally

# Create virtual environment
python -m venv venv

# Activate virtual environment

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install uvicorn fastapi
pip install -r requirements.txt
pip install groq python-dotenv requests
pip install tavily-python

# Create .env file inside backend folder
GROQ_API_KEY="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"
TAVILY_API_KEY="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"

# Run Backend
cd backend
py -m uvicorn main:app --reload

# Run frontend.py

py -m streamlit run frontend.py

## Future Improvements

- Real-time workflow monitoring
- Memory-enhanced agents
- Autonomous task execution
- Workflow analytics dashboard

## Team

Built for AgentHon Hackathon.
