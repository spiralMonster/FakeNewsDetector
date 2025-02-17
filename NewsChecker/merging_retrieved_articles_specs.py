from pydantic import BaseModel,Field

class MergingRetrievedArticlesSpecs(BaseModel):
    final_article:str=Field(description="""
    The article with aggregated content of provided articles.
    """)