from pydantic import BaseModel,Field
from typing import Literal

class CompareNewsArticleSpecs(BaseModel):
    evidence_comparison:Literal["Similar","Not Similar"]=Field(description="""
    Whether the two news articles are similar or not in their information.
    """)

    reason:str=Field(description="""
    The reason why the articles are similar or not with respect to each other.
    """)