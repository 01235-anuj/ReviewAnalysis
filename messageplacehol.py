import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.title("Gemini Chatbot 💬")

# Initialize conversation in session state
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]

# Input box with placeholder
user_input = st.text_input("Your message:", placeholder="Type your message here...")

if st.button("Send") and user_input.strip():
    # Add user input to history
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Generate AI response using Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    st.session_state.messages.append(AIMessage(content=response.text))

# Display conversation
conversation_text = ""
for m in st.session_state.messages:
    if isinstance(m, HumanMessage):
        conversation_text += f"You: {m.content}\n"
    elif isinstance(m, AIMessage):
        conversation_text += f"AI: {m.content}\n"

st.text_area("Conversation", value=conversation_text, height=300)
