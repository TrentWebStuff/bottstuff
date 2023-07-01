from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from pydantic import BaseModel


class WorklistSpec(BaseModel):
    query: str = Field(description="should be a search query")
    engine: str = Field(description="should be a search engine")



class WorklistTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"
    args_schema: Type[SearchSchema] = SearchSchema

    def _run(
        self,
        query: str,
        engine: str = "google",
  
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        search_wrapper = SerpAPIWrapper(params={"engine": engine, "gl": gl, "hl": hl})
        return search_wrapper.run(query)

    async def _arun(
        self,
        query: str,
        engine: str = "google",
        gl: str = "us",
        hl: str = "en",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")