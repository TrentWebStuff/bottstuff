from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from typing import Any, Dict, Optional
from advancedmd.util.util import split_text_into_chunks




class Get_Summary_Tool(BaseTool):
    name="get meeting summary"
    description="Useful for summarizing notes or a transcript from a meeting. Not useful when createing a list of main points from a meeting."
    return_direct=True

    def _run(self, input: str, **kwargs):
        print("in get summary tool")
        summaries = Summary()._get_summary(input)
        output = Summary()._get_sum_of_summary(summaries)

        # Extract output_filename from kwargs. If not given, it defaults to None
        output_filename = kwargs.get('output_filename', None)

        # If output_filename is not given, prepend the points to the input file
        if output_filename is None:
            # Read original content of the file
            with open(input, 'r') as file:
                original_content = file.read()

            # Write points and original content back into the file
            with open(input, 'w') as file:
                file.write("-- Meeting Points Summary --")
                file.write(''+output + '\n\n' + original_content)

        # If output_filename is given, write points to a new text file
        else:
            with open(output_filename, 'w') as file:
                file.write("-- Meeting Points Summary --")
                file.write(output)
                
        return output
        
    def _arun(self, input: str):
        raise NotImplemented
    




class Summary():
  

    from advancedmd.tools.meeting.prompt import (
        SUMMARY_PROMPT,
        SUMMARY_EXAMPLES,
        SUM_SUMMARY_PROMPT,
        SUM_SUMMARY_EXAMPLES,
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name = 'gpt-3.5-turbo-16k'
    )

    def _get_summary(self, text_input: str):

        meeting_todos = ""
        template: Optional[str] =  self.SUMMARY_PROMPT
        examples: Optional[str] = self.SUMMARY_EXAMPLES

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
    
    def _get_sum_of_summary(self, text_input: str):

        meeting_todos = ""
        template: Optional[str] =  self.SUM_SUMMARY_PROMPT
        examples: Optional[str] = self.SUM_SUMMARY_EXAMPLES

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
    




