from pydantic import BaseModel,Field

class ReasoningSemanticAnalyzerSpecs(BaseModel):
    reason:str=Field(description="""
    Reason why the model has generated such response.
    """)