from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from typing import Any, Dict, Optional
from advancedmd.util.util import split_text_into_chunks



class Get_Meeting_Points_Tool(BaseTool):
    name="get meeting points"
    description="Useful getting a list of the main points from a meeting transcript. Not useful in getting a summary. It takes 'transcript_input' which is a path to a .txt file containing the meeting transcript.  It outputs a list of main points."
    return_direct=True



    def _run(self, transcript_input: str):
        points = Points()._get_points(transcript_input)
        return points

    
        
    def _arun(self, json_url: str):
        raise NotImplementedError("This tool does not support async")
    


class Get_Meeting_Points_Summary_Tool(BaseTool):
    name = "get meeting points summary"
    description = "Useful for getting a summarized list of the points of a meeting based on a meeting transcript. Not useful for getting a summary. It takes a path to a .txt or .md file containing the meeting transcript. It outputs a summary of the points made in the meeting."
    return_direct = True

    def _run(self, input_filename: str, **kwargs):
        points = Points_Summary()._get_points_summary(input_filename)

        # Extract output_filename from kwargs. If not given, it defaults to None
        output_filename = kwargs.get('output_filename', None)

        # If output_filename is not given, prepend the points to the input file
        if output_filename is None:
            # Read original content of the file
            with open(input_filename, 'r') as file:
                original_content = file.read()

            # Write points and original content back into the file
            with open(input_filename, 'w') as file:
                file.write("-- Meeting Points Summary --")
                file.write(''+points + '\n\n' + original_content)

        # If output_filename is given, write points to a new text file
        else:
            with open(output_filename, 'w') as file:
                file.write("-- Meeting Points Summary --")
                file.write(points)
                

        return points

    def _arun(self, json_url: str):
        raise NotImplementedError("This tool does not support async")




class Points():

    from advancedmd.tools.meeting.prompt import (
        MAIN_POINTS_PROMPT,
        MAIN_POINTS_EXAMPLES,
    )


    llm = ChatOpenAI(
        temperature=0,
        model_name = 'gpt-3.5-turbo-16k'
    )

    def _get_points(self, text_input: str):
        

        meeting_transcript = ""
        template: Optional[str] =  self.MAIN_POINTS_PROMPT
        examples: Optional[str] = self.MAIN_POINTS_EXAMPLES

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
        
        chunks = split_text_into_chunks(text, 7000)

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
            print("POINTS-TRANSFORMED ::: "+transformed_part)

            # Run the chain on the chunk and add the result to the results list
            results.append(transformed_part)

        results_joined = ''.join(results)
        print("POINTS-results_joined"+ results_joined)
        
     
        # Concatenate the results before returning
        return results_joined
    
    

class Points_Summary():

    from advancedmd.tools.meeting.prompt import (
        MAIN_POINTS_SUMMARY_PROMPT,
        MAIN_POINTS_SUMMARY_EXAMPLES,
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name = 'gpt-3.5-turbo-16k'
    )

    def _get_points_summary(self, text_input: str):
        
        from langchain.prompts import PromptTemplate
        from langchain.chains.llm import LLMChain
        from langchain.prompts import PromptTemplate

        text = Points()._get_points(text_input)


        meeting_transcript = ""
        template: Optional[str] =  self.MAIN_POINTS_SUMMARY_PROMPT
        examples: Optional[str] = self.MAIN_POINTS_SUMMARY_EXAMPLES

    

        # Split the transcript into chunks
        chunks = split_text_into_chunks(text, 8000)

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
            print("POINTS-SUMMARY-TRANSFORMED-CHUNK ::: "+transformed_part)

            # Run the chain on the chunk and add the result to the results list
            results.append(transformed_part)

        results_joined = ''.join(results)
        print("POINTS-SUMMARY-results_joined::" + results_joined)
        
     
        # Concatenate the results before returning
        return results_joined






