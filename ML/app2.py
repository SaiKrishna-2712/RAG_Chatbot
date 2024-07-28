import streamlit as st
from langchain.llms import ClaudeLLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model='claude-3-opus-20240229')

# Replace with your actual API keys
# OPENAI_API_KEY = 'your_openai_api_key'
CLAUDE_API_KEY = ''

# Initialize LLMs
# openai_llm = OpenAI(api_key=OPENAI_API_KEY)
claude_llm = ClaudeLLM(api_key=CLAUDE_API_KEY)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="The user said: {input}"
)

# Create a chain
# openai_chain = LLMChain(llm=openai_llm, prompt=prompt_template)
claude_chain = LLMChain(llm=claude_llm, prompt=prompt_template)

st.title("Conversational Chatbot")

user_input = st.text_input("You: ")

if st.button("Send"):
    with st.spinner("Thinking..."):
        # openai_response = openai_chain.run(input=user_input)
        claude_response = claude_chain.run(input=user_input)

        # st.subheader("OpenAI Response")
        # st.write(openai_response)

        st.subheader("Claude Response")
        st.write(claude_response)
