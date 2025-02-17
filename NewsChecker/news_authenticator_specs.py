from pydantic import BaseModel,Field
from typing import Literal

class NewsAuthenticatorSpecs(BaseModel):
    news_authenticity:Literal["Yes","No"]=Field(description="""
    Whether the news is authentic or not.
    """)
    reason:str=Field(description="Reason why the news is authentic or not")