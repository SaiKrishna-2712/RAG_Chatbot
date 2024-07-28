from langchain_community.llms import OpenAI, HuggingFaceHub
import streamlit as st
import os

# Function to load OpenAI model and get response
def get_openai_response(question):
    llm = OpenAI(api_key="", model_name="gpt-3.5-turbo", temperature=0.5)
    response = llm(question)
    return response

# Function to load Hugging Face model and get response
def get_huggingface_response(question):
    llm = HuggingFaceHub(repo_id="meta-llama/Meta-Llama-3-8B", huggingfacehub_api_token="", model_kwargs={"temperature":0.6})
    response = llm(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")

# Select model type
model_type = st.selectbox("Choose Model", ["OpenAI", "HuggingFace"])

submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    if model_type == "OpenAI":
        response = get_openai_response(input)
    else:
        response = get_huggingface_response(input)
    
    st.subheader("The Response is")
    st.write(response)
