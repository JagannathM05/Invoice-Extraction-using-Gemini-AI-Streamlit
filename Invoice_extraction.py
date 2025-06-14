import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
        parts = response.candidates[0].content.parts
        text = ' '.join(part.text for part in parts)
        return text
    
#initialise the streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Invoice Extraction Application")
input = st.text_input("Input prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Invoice image.")

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Respponse is ..")
    st.write(response)