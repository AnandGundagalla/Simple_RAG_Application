# rag_chain.py

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap, RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings   # Updated import


VECTORSTORE_PATH = "vectorstore"

def get_rag_chain(llm):

    # Use new huggingface embeddings class
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS vectorstore
    db = FAISS.load_local(
        VECTORSTORE_PATH,
        embedder,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    # Prompt Template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Answer ONLY using the context below.
If the answer is not present, reply: "The document does not contain this information."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # NEW LangChain Runnable RAG Pipeline
    rag_chain = (
        RunnableMap({
            "context": retriever,
            "question": RunnablePassthrough()
        })
        | prompt
        | llm
    )

    return rag_chain
