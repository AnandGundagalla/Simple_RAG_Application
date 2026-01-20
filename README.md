📄 RAG Document Chatbot – Assignment Submission

This project implements a Retrieval-Augmented Generation (RAG) Document Question-Answering Chatbot using:

FAISS vectorstore

Sentence-Transformer embeddings

Gemini 2.5 Flash (latest Google model)

LangChain pipeline

Custom LLM wrapper

PDF ingestion + chunking + semantic search

🚀 Features
✔ Ingest PDFs

Reads all PDFs in pdfs/

Extracts text

Splits into chunks

Generates embeddings

Saves FAISS index (index.faiss, index.pkl)

✔ Ask questions about the documents

The chatbot retrieves relevant chunks from FAISS and generates an answer using Gemini.

✔ Uses Gemini 2.5 Flash LLM

Free tier

Fast

High-performance

Does not break with model changes like Groq

📌 Installation
Step 1 — Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

Step 2 — Install dependencies
pip install -r requirements.txt

Step 3 — Set API Key

Edit config.py:

GEMINI_API_KEY = "your_key_here"
LLM_MODEL = "gemini-2.5-flash"


**Folder Structure**

RAG_PROJECT_2/
│
├── Q1/
│   ├── Parse.py
│   ├── sample_input.txt
│
├── Q2/
│   ├── top_words.py
│   ├── sample_input.txt
│
├── Q3_RAG_Document_Chatbot/
│   ├── app.py
│   ├── ingestion.py
│   ├── rag_chain.py
│   ├── llm_provider.py
│   ├── config.py
│   ├── requirements.txt
│   ├── README.md
│   │
│   ├── pdfs/
│   │   └── your_documents.pdf
│   │
│   └── vectorstore/
│       ├── index.faiss
│       └── index.pkl
│
└── screenshots.pdf
