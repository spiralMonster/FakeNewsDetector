from pydantic import BaseModel,Field

class CombineNewsArticleSpecs(BaseModel):
    final_news:str=Field(description="""
    The final news article created after combining all the provided news articles.
    """)