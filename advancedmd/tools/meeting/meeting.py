from advancedmd.tools.meeting.todos import Todos
from advancedmd.tools.meeting.points import Points
from advancedmd.tools.meeting.summary import Summary
from langchain.tools import BaseTool



class Get_All_Meeting_Tool(BaseTool):
    name="get All Meeting Stuff"
    description="Useful for getting everyhthing about a meeting when given the path to a file containing the meeting transcript."
    return_direct=True

   

    def _run(self, transcript_input: str):
        
        results = []
        points = Points()._get_points(transcript_input)
        todos = Todos()._get_todos(points)
        summary = Summary()._get_summary(points)

        results.append(summary)
        results.append(points)
        results.append(todos)
        
        return ' '.join(results)

        
    def _arun(self, json_url: str):
        raise NotImplementedError("This tool does not support async")
    