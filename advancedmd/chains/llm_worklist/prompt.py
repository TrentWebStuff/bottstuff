# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

_PROMPT_TEMPLATE = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.

Request: ${{Question with math problem.}}
```text
${{single line summary of what the user wants to do with the worklists table}}
```

Response: ${{Response}}

Begin.



Request: {request}
"""

PROMPT = PromptTemplate(
    input_variables=["request"],
    template=_PROMPT_TEMPLATE,
)
