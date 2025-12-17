# ai_classifier.py

import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def classify_text(text):
    prompt = f"""
    Classify the following quote as one of:
    - Motivational
    - Philosophical
    - Technical

    Respond with ONE word only.

    Quote:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
