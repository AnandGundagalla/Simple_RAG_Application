# app.py

from llm_provider import get_llm
from rag_chain import get_rag_chain

def main():
    print("Loading Groq Llama3-8B model...")
    llm = get_llm()

    print("Setting up RAG pipeline...")
    rag_chain = get_rag_chain(llm)

    print("\n🔥 Document Chatbot Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer = rag_chain.invoke(question)

        print("\nBot:", answer)
        print("-" * 40)

if __name__ == "__main__":
    main()
