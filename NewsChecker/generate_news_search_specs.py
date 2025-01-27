from pydantic import BaseModel,Field
from typing import List

class NewsSearchGeneratorSpecs(BaseModel):
    news_search_query: List[str]=Field(description="""
    List of 3 news search prompt.
    """)