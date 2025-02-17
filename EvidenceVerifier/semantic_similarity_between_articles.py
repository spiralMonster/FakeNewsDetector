import os
import time
import numpy as np
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

def SemanticSimilarityBetweenArticles(posted_article:str,supporting_article:str):
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                                   google_api_key=os.environ["GOOGLE_GEMINI_API_KEY"])

    vec1=embedding_model.embed_query(posted_article)
    vec2=embedding_model.embed_query(supporting_article)

    dot=np.dot(vec1,vec2)
    norm1=np.linalg.norm(vec1)
    norm2=np.linalg.norm(vec2)

    similarity_score=dot/(norm1*norm2)
    time.sleep(2)
    print("Similarity score calculated.....")
    return similarity_score

