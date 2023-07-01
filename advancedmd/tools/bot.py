
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.tools import BaseTool
from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun
from typing import Any, Dict, Optional, Tuple
from langchain.chains.llm import LLMChain
from langchain.text_splitter import CharacterTextSplitter 
from advancedmd.tools.meeting import prompt
from langchain.agents import initialize_agent
from advancedmd.tools.meeting.todos import Get_ToDos_Tool
from advancedmd.tools.meeting.points import Get_Meeting_Points_Summary_Tool, Get_Meeting_Points_Tool
from advancedmd.tools.meeting.summary import Get_Summary_Tool
from advancedmd.tools.meeting.meeting import Get_All_Meeting_Tool
from advancedmd.tools.bot_prompt import prompt

import os

import openai
import json
import os
import advancedmd

class Meeting_Bot():

    os.environ["OPENAI_API_KEY"] = "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"
    os.environ["SERPAPI_API_KEY"] = "31f0720aa61387674eb41e08ac20ce26fa350c8f0d85d62e454b482f189a89e9"

    meeting_points = Get_Meeting_Points_Tool()
    meeting_points_summary = Get_Meeting_Points_Summary_Tool()
    todos = Get_ToDos_Tool()
    summary = Get_Summary_Tool()
    all_meeting = Get_All_Meeting_Tool()

    turbo_llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

    tools = [ summary, meeting_points_summary, meeting_points, todos, all_meeting ]

    memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=3,
        return_messages=True
    )

    #create the agent
    conversational_agent = initialize_agent(
        agent='chat-conversational-react-description',
        #agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools,
        llm=turbo_llm,
        verbose=True,
        max_iterations=3,
        early_stopping_method='generate',
        memory=memory
    )
    conversational_agent.agent.llm_chain.prompt.messages[0].prompt.template = prompt


    def _run(self, task_string: str):
        result = self.conversational_agent(task_string)
        return result

# in the same way that the lower tools have a
# class and a tool, and this calls those.
# have a higher level agent that calls this tool
# need to add a tool def here that calls the Meeting_bot Class