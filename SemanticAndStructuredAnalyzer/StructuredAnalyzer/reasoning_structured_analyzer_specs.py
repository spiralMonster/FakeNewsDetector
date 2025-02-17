from pydantic import BaseModel,Field

class ReasoningStructuredAnalyzerSpecs(BaseModel):
    reason:str=Field(description="""
    Reason why the model has generated such response.
    """)