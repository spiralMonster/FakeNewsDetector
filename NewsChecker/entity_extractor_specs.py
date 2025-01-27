from pydantic import BaseModel,Field
from typing import List

class EntityExtractorSpecs(BaseModel):
    entities:List[str] =Field(description="""
    The entities from the news.
    """)