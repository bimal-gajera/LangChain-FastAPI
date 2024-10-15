import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/code-generator/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/cs-guide/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']


st.title("LangChain API with llama app")

input_text1 = st.text_input("Search problem and get the solution code...")
input_text2 = st.text_input("Search any concept you'd like to learn about...")


if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))