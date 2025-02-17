from pydantic import BaseModel,Field

class SelectBestNewsSearchSpecs(BaseModel):
    best_search:str=Field(description="Best news search query")
