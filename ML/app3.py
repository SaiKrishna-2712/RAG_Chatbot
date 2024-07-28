import streamlit as st
# from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI #ChatGoogleGenerativeAI is a constructor for declaring gemini llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

# Store your api key
CLAUDE_API_KEY = ''
GEMINI_API_KEY = ''

# Initialize LLMs
# claude_llm = ChatAnthropic(api_key=CLAUDE_API_KEY, model='claude-3-opus-20240229')
gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key = GEMINI_API_KEY, temperature=1.0)
# temperature determines the creativity of the llm model by altering the parameters of the soft max function higher the temperature more the creativity

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables = ["input"],
    template="Give the user response in bullet points for user input: {input}"
)
#prompt template helps in generating customizzed outputs

# Create a chain
# claude_chain = LLMChain(llm=claude_llm, prompt=prompt_template)
gemini_runnable = prompt_template | gemini_llm | StrOutputParser()

st.title("Conversational ChatBot using Gemini")

user_input = st.text_input("You: ")

if st.button("Send"):
    with st.spinner("Thinking..."):
        # claude_response = claude_chain.run(input=user_input)
        gemini_response = gemini_runnable.invoke({"input":user_input})

        st.subheader("Gemini Response")
        st.write(gemini_response)

        # st.subheader("Claude Response")
        # st.write(claude_response)
