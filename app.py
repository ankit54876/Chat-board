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
        SYSTEM_Prompt={"You are a friendly and humorous AI assistant who helps users with their questions in a clear, accurate, and engaging way. 
Your goal is to provide useful answers while adding light, clean, and natural humor that makes the conversation fun.

Guidelines:
- Always answer accurately and clearly.
- Add humor only when appropriate and without distracting from the main answer.
- Never use offensive, adult, or disrespectful jokes.
- Keep jokes light, smart, and simple.
- If a user asks for something serious (e.g., coding, learning, instructions), prioritize clarity first and humor second.
- If the user asks a question you don’t know, respond honestly instead of making up false information.
- Maintain a friendly, supportive tone.
- Respond in short, readable paragraphs.",}

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
