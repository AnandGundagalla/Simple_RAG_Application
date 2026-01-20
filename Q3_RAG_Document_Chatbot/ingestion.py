# ingestion.py

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_FOLDER = "pdfs"
VECTORSTORE_PATH = "vectorstore"

def ingest_pdfs():
    docs = []

    # Load PDFs
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
            docs.extend(loader.load())

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120
    )
    chunks = splitter.split_documents(docs)

    # Embeddings
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS index
    vectorstore = FAISS.from_documents(chunks, embedder)

    # Save
    vectorstore.save_local(VECTORSTORE_PATH)
    print("Vectorstore created and saved successfully!")

if __name__ == "__main__":
    ingest_pdfs()
