from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from typing import Any, Dict, Optional
from advancedmd.util.util import split_text_into_chunks





class Get_ToDos_Tool(BaseTool):
    name="get meeting todos"
    description="Useful for taking string that is a list of meeting main points and distillng a list of todos."
    return_direct=True


    def _run(self, meeting_main_points: str):
        todos = Todos()._get_todos(meeting_main_points)
        return todos
        
    def _arun(self, json_url: str):
        raise NotImplemented





class Todos():

    from advancedmd.tools.meeting.prompt import (
        TODOS_PROMPT,
        TODOS_EXAMPLES,
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name = 'gpt-3.5-turbo-16k'
    )

    def _get_todos(self, text_input: str):

        meeting_todos = ""
        template: Optional[str] =  self.TODOS_PROMPT
        examples: Optional[str] = self.TODOS_EXAMPLES

        # Check if the input is a URL or a content string
        if text_input.endswith('.txt'):
            with open(text_input, 'r') as file:
                # Read the entire contents of the file
                text = file.read()
        elif text_input.endswith('.md'):
            with open(text_input, 'r') as file:
                # Read the entire contents of the file
                text = file.read()
        else:
            text = text_input

        # Split the transcript into chunks
        chunks = split_text_into_chunks(text, 6000)

        # Initialize results list
        results = []

        for chunk in chunks:
            prompt=PromptTemplate(
                    template = template,
                    input_variables=["transcript", "examples"],
                )

            prompt.format(transcript = chunk, examples = examples )
            
            chain = LLMChain(
                llm=self.llm,
                prompt=prompt,
            )
            
            #print("CHUNK :::")
            transformed_part = chain.run({'transcript' : chunk, 'examples' : examples})
            #print("TRANSFORMED ::: "+transformed_part)

            # Run the chain on the chunk and add the result to the results list
            results.append(transformed_part)

        return ''.join(results)