from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent


import streamlit as st

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


search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
]


memory = ConversationBufferMemory(memory_key="chat_history")


llm=OpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)



prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=memory,
)

