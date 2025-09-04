import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Dropdown for research papers
paper = st.selectbox(
    "Select a research paper:",
    [
        "Attention Is All You Need (2017)",
        "BERT: Pre-training of Deep Bidirectional Transformers (2018)",
        "GPT: Improving Language Understanding (2018)",
        "GPT-2: Language Models are Unsupervised Multitask Learners (2019)",
        "GPT-3: Language Models are Few-Shot Learners (2020)"
    ]
)

# Dropdown for explanation style
style = st.selectbox(
    "Choose explanation style:",
    ["Beginner-friendly", "Code Oriented", "Mathematical", "Code Oriented and Mathematicel"]
)

# Dropdown for length
length = st.selectbox(
    "Select explanation length:",
    ["Short (2-3 sentences)", "Medium (1-2 paragraphs)", "Detailed (essay-style)"]
)


# Generate button
if st.button("Generate Explanation"):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    Explain the research paper: {paper}.
    Style: {style}.
    Length: {length}.
    Focus only on key points about the transformer concepts.
    """
    
    response = model.generate_content(prompt)
    st.subheader("🧠 Gemini Explanation:")
    st.write(response.text)
