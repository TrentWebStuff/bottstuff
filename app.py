import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl
from  advancedmd.tools.bot import Meeting_Bot


template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=False)
def factory():
    mbot = Meeting_Bot()
    print(mbot._run("Summarize this meeting  '/Users/tpeterson/Library/CloudStorage/GoogleDrive-trenten.peterson@gmail.com/My Drive/Obsidian/Trent-Work/TEST TEST.md'"))
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=ChatOpenAI(temperature=0, streaming=True))

    return llm_chain