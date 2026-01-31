from langchain_groq import ChatGroq
import os

def generate_delay_message(train, delay_minutes, reason):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    prompt = f"""
You are an Indian Railways announcement system.

Generate the following for a delayed train:

Train: {train}
Delay: {delay_minutes} minutes
Reason: {reason}

Provide:
1. Passenger Announcement
2. SMS Update
3. Formal Explanation (official tone)
"""

    response = llm.invoke(prompt)
    return response.content
