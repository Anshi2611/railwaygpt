from langchain_groq import ChatGroq
import os


def analyze_complaint(complaint_text):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    prompt = f"""
You are an Indian Railways customer support AI.

Analyze the following passenger complaint and return:

Category (Cleanliness/Food/Staff/Delay/Safety/Other):
Sentiment (Positive/Neutral/Negative):
Priority (High/Medium/Low):
Suggested Reply:

Complaint:
{complaint_text}
"""

    response = llm.invoke(prompt)
    return response.content
