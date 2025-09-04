import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

print("Chatbot ready! (type 'exit' to quit)\n")
 
 # ✅ Conversation history
history = []


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    # Add user message to history
    history.append({"role": "user", "parts": [user_input]})

    # Generate response using full history
    response = model.generate_content(history)

    # Add model's reply to history
    history.append({"role": "model", "parts": [response.text]})

    # Print AI reply
    print("AI:", response.text)

