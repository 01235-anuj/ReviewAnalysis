# five_line_cricket_poem_gemini.py
# Requirements: pip install google-generativeai
# Set API key:
#   export GOOGLE_API_KEY="your-gemini-api-key"

import os
import google.generativeai as genai

# configure with your API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def get_five_line_poem_on_cricket(model="gemini-1.5-flash", temperature=0.1):
    """
    Generate a five-line poem on cricket using Gemini.
    """
    prompt = (
        "Write a short poem about cricket in exactly five lines. "
        "Each line should be on a new line, creative and rhythmic."
    )

    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt, generation_config={"temperature": temperature})
    
    return response.text.strip()

if __name__ == "__main__":
    poem = get_five_line_poem_on_cricket()
    print("Five-line cricket poem:\n")
    print(poem)
