from langchain import OpenAI, LLMChain, PromptTemplate
import chainlit as cl
from advancedmd.tools.bot import Meeting_Bot
import os


OPENAI_API_KEY = cl.user_session.get("env").get("OPENAI_API_KEY")


prompt_template = "What is a good name for a company that makes {product}?"


@cl.langchain_factory(use_async=False)
def main():

    meeting_bot = Meeting_Bot()
    return meeting_bot.conversational_agent


@cl.langchain_postprocess
async def postprocess(output: str):
    await cl.Message(content="In the end it doesn't even matter.").send()
