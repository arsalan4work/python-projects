import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# Set api key
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# load model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Function to translate with genai
def translate_language(user_text, source_lang, target_lang):
    prompt = f"""
    Translate the following text from {source_lang} to {target_lang}:

    {user_text}
    
    
    please don't add extra text, only tranlated text
    """
    response = model.generate_content(prompt)
    return response.text if response else "Translation failed."

# Streamlit App UI
st.title("Language Translator using Gemini AI")

# User input for text
user_text = st.text_area("Enter text to translate:")

# Language options
languages = ["English", "Spanish", "French", "German","Urdu", "Hindi", "Chinese", "Japanese", "Russian", "Arabic",
             "Portuguese"]
source_lang = st.selectbox("Select source language:", languages)
target_lang = st.selectbox("Select target language:", languages)

if st.button("Translate"):
    if user_text.strip():
        translated_text = translate_language(user_text, source_lang, target_lang)
        st.title("Translated Text")
        st.subheader(translated_text)
    else:
        st.warning("Please enter text to translate.")