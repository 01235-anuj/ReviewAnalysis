import os
import json
import re
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.title(" Review Analyzer ")

# Input box
review = st.text_area(
    "Enter Movie Review:",
    placeholder="Type your movie review here..."
)

if st.button("Analyze") and review.strip():
    # Prepare strict prompt for Gemini
    prompt = f"""
    Analyze the following movie review. Respond ONLY with valid JSON (no extra text):
    {{
        "sentiment": "<positive|negative|neutral>",
        "brief_analysis": "<1-2 sentence summary>"
    }}

    Review: "{review}"
    """

    # Call Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Clean output
    cleaned_text = re.sub(r"```json|```", "", response.text).strip()

    # Try parsing JSON
    try:
        data = json.loads(cleaned_text)
        st.subheader("Structured Analysis:")
        st.write(f"**Sentiment:** {data.get('sentiment', 'unknown')}")
        st.write(f"**Brief Analysis:** {data.get('brief_analysis', 'No analysis generated.')}")
    except json.JSONDecodeError:
        st.error("Failed to parse AI response. Here's the raw output:")
        st.text(cleaned_text)

# --- Footer with GitHub & LinkedIn ---
st.markdown("---")
st.markdown("👨‍💻 Developed by **Anuj Mishra**")
st.markdown("🔗 [GitHub](https://github.com/01235-anuj) | 💼 [LinkedIn](https://www.linkedin.com/in/anuj-mishra-01235)")
