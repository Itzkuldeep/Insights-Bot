from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#--------------LOGICS
model = genai.GenerativeModel("gemini-pro")
def get_ideas(query):
    response = model.generate_content(query)
    return response.text

### Streamlit for UI

st.set_page_config(page_title="The Bot")

st.header("The Bot")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit:
    response = get_ideas(input)
    st.subheader("Your answer is: ")
    st.write(response)