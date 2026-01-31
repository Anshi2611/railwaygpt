from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os


def load_rag():
    # Load railway rules
    with open("data/railway_rules.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Split text
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector DB
    db = FAISS.from_documents(docs, embeddings)

    # LLM
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    return db, llm


def rag_answer(db, llm, question):
    # Retrieve relevant docs
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful Indian Railways assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content
