# Import Libraries

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)


st.set_page_config(page_title="me T-Bot")
st.header("Trent bot")



# Open API key'
import os
os.environ["OPENAI_API_KEY"] = "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"

chat = ChatOpenAI(temperature=0)


template = """
    Act as a travel agent.
    I am your client, looking for a great vacation.
    Engage with me in a dialog, and guide me in a conversational format ( you talk, then I talk, then you, then me, etc.) Until you are able to complete the REQUIRED QUESTIONS in the JSON object below with the necessary information to book the vacation. 
    Take things slowly. Do not ask me more than one or two questions at a time. 
    Keep your responses to One or two sentences at a time, or at most a short paragraph. Help me along. Don't rush me.    
    
    JSON:
    &#123'Questions' :
    [&#123'Where' : 'Where does the user want to go?'&#125,
    &#123'When' : 'When does the user want to go there?'&#125,
    &#123'What' : 'What do they want to do when they get there?'&#125,
    &#123'Who' : 'Who do they want to go with?'&#125,
    &#123'Why' : 'Why do they want to go there?'&#125]&#125. 
    
    When you have this information, tell me that you send me an email with my itinerary.
    End by writing out the JSON Above.
    
    Please start the conversation with a warm introduction.
    
  
  
    
    YOUR RESPONSE:
"""

def get_text():
    user_text = st.text_area(label="User Input", label_visibility='collapsed', placeholder="Your chat", key="user_input")
    return user_text


user_input = get_text()

if len(user_input.split(" ")) > 700:
    st.write("Please enter a shorter chat. The maximum length is 700 words.")
    st.stop()



llm = ChatOpenAI(temperature=0)

chat_prompt = ChatPromptTemplate.from_messages(
    [ SystemMessagePromptTemplate.from_template(template),
     MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("user_input")
    ]
)

memory = ConversationBufferMemory(return_messages=True)
#memory = ConversationBufferWindowMemory(k=2)

conversation = LLMChain(llm=chat, memory=memory, prompt=chat_prompt, verbose=True)


conversation.predict(input=user_input)

st.write(memory)
#st.write(ConversationBufferMemory)
#st.write(memory.chat_memory)
#st.write(memory)


# -> 'Hello! How can I assist you today?'