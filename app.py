## Conversational Q&A Chatbot
import streamlit as st

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from xai_sdk import Client
import os


## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

grok=Client(api_key=os.getenv("GROK_API_KEY"))

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

## Function to load OpenAI model and get respones

def get_grok_response(question):
    response = grok.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": "You are a comedian AI assistant"},
            {"role": "user", "content": question},
        ],
        temperature=0.5,
    )
    return response.choices[0].message["content"]

input=st.text_input("Input: ",key="input")
response=get_grok_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)