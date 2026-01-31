# RailwayGPT – AI Assistant for Indian Railways

RailwayGPT is a production-ready LLM-powered AI web application that assists users with Indian Railways related queries. The system combines Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) to deliver accurate and domain-specific responses.

Live Application:
https://railwaygpt.onrender.com

FEATURES

1. General Railway Chat  
Ask general questions related to Indian Railways using a Groq-hosted LLaMA model.

2. Railway FAQ Bot (RAG)  
Answers railway policy and rule-based questions using a FAISS vector database and document-grounded retrieval.

3. Complaint Analyzer  
Automatically analyzes passenger complaints to identify category, sentiment, priority, and generates professional auto-replies.

4. Delay Message Generator  
Generates passenger announcements, SMS updates, and formal delay explanations based on train details and delay information.

ARCHITECTURE

User (Streamlit UI)
        |
        v
     LLM Layer
   /      |       \
 Chat   RAG   NLP Modules
          |
      FAISS Vector Database
          |
   Railway Policy Data

TECH STACK

Python  
Streamlit  
LangChain (Modular)  
Groq LLM API (LLaMA 3.1)  
FAISS  
Sentence Transformers  
GitHub  
Render (Deployment)

PROJECT STRUCTURE

railwaygpt/
├── app.py
├── rag_engine.py
├── complaint_module.py
├── delay_module.py
├── requirements.txt
├── data/
│   └── railway_rules.txt
└── README.md

ENVIRONMENT VARIABLES

GROQ_API_KEY=your_api_key_here

RUN LOCALLY

pip install -r requirements.txt
streamlit run app.py

USE CASES

AI-powered railway customer support  
Policy-based question answering  
Complaint classification and prioritization  
Automated passenger communication  
LLM + RAG learning project

RESUME DESCRIPTION

Built an end-to-end LLM-powered Railway Assistant using custom RAG architecture and FAISS vector database. The application supports railway policy Q&A, complaint analysis, and automated delay messaging, and is deployed as a production-ready Streamlit web application on Render.

AUTHOR

Anshika Gupta  
GitHub: https://github.com/Anshi2611
