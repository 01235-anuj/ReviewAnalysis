import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Conversation history
messages = [SystemMessage(content="You are a friendly assistant.")]

while True:
    paper = input("Paper (or 'exit'): ")
    if paper.lower() == "exit":
        break
    style = input("Style (simple/detailed): ")

    # Create dynamic user message
    user_msg = HumanMessage(content=f"Explain '{paper}' in {style} style.")
    messages.append(user_msg)

    # Get AI response
    response = chat.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("AI:", response.content)

