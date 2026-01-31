import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from rag_engine import load_rag, rag_answer
from complaint_module import analyze_complaint
from delay_module import generate_delay_message

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="RailwayGPT",
    page_icon="🚆",
    layout="centered"
)

st.title("🚆 RailwayGPT – AI Assistant for Indian Railways")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Module",
    [
        "General Chat",
        "Railway FAQ Bot (RAG)",
        "Complaint Analyzer",
        "Delay Message Generator"
    ]
)

# Initialize base LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# -------------------------------
# 1️⃣ General Chat
# -------------------------------
if menu == "General Chat":
    st.subheader("💬 General Railway Chat")

    user_input = st.text_input("Ask anything about Indian Railways:")

    if user_input:
        with st.spinner("Thinking..."):
            response = llm.invoke(user_input)
            st.success(response.content)

# -------------------------------
# 2️⃣ Railway FAQ Bot (RAG)
# -------------------------------
elif menu == "Railway FAQ Bot (RAG)":
    st.subheader("📚 Railway Rules & Policy Chatbot")

    # Load RAG only once
    if "rag_loaded" not in st.session_state:
        db, rag_llm = load_rag()
        st.session_state["db"] = db
        st.session_state["rag_llm"] = rag_llm
        st.session_state["rag_loaded"] = True

    question = st.text_input("Ask about railway rules, refunds, Tatkal, etc.")

    if question:
        with st.spinner("Searching railway policies..."):
            answer = rag_answer(
                st.session_state["db"],
                st.session_state["rag_llm"],
                question
            )
            st.success(answer)

# -------------------------------
# 3️⃣ Complaint Analyzer
# -------------------------------
elif menu == "Complaint Analyzer":
    st.subheader("🚨 Railway Complaint Analyzer")

    complaint_text = st.text_area(
        "Enter passenger complaint:",
        placeholder="Example: The coach was very dirty and washroom was not cleaned..."
    )

    if st.button("Analyze Complaint"):
        if complaint_text.strip() == "":
            st.warning("Please enter a complaint.")
        else:
            with st.spinner("Analyzing complaint..."):
                result = analyze_complaint(complaint_text)
                st.success(result)

# -------------------------------
# 4️⃣ Delay Message Generator
# -------------------------------
elif menu == "Delay Message Generator":
    st.subheader("⏱️ Train Delay Message Generator")

    train = st.text_input("Train Name / Number")
    delay = st.number_input("Delay (in minutes)", min_value=0)
    reason = st.text_input("Reason for delay")

    if st.button("Generate Message"):
        if train.strip() == "" or reason.strip() == "":
            st.warning("Please fill all fields.")
        else:
            with st.spinner("Generating delay messages..."):
                result = generate_delay_message(train, delay, reason)
                st.success(result)
