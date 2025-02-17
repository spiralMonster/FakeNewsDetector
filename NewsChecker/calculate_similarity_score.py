
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
import os
import time
from typing import List
from dotenv import load_dotenv
load_dotenv()

def calculate_cosine_similarity(query1,query2):
    dot=np.dot(query1,query2)
    norm1=np.linalg.norm(query1)
    norm2=np.linalg.norm(query2)

    similarity_score=dot/(norm1*norm2)
    return similarity_score

def CalSimilarityScore(posted_article:str,retrieved_articles:List):
    query_score={}
    embedding_model=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.environ["GOOGLE_GEMINI_API_KEY"])
    time.sleep(2)
    query_embedding=embedding_model.embed_query(posted_article)

    for ret_article in retrieved_articles:
        ret_article_embedding=embedding_model.embed_query(ret_article)
        query_score[ret_article]=calculate_cosine_similarity(query_embedding,ret_article_embedding)

    return query_score

if __name__=="__main__":
    ret_articles=["New Delhi railway station stampede updates: AAP's Sanjay Singh accuses government of cover-up", 'New Delhi Railway Station Stampede Live Updates: Delhi Police holds high-level meeting, initiates inquest proceedings', 'New Delhi Railway Station Stampede Live Updates: 18 dead after Maha Kumbh crowd triggers chaos, Govt announce', '20-yr-old man and minor girl died after jumping in front of train: Police', 'U.P. train derailment highlights | Two dead as Chandigarh-Dibrugarh Express derails; Modi govt systematically jeopardised rail safety, says Kharge']
    print(CalSimilarityScore("Delhi Railway station accident 20 dead",ret_articles))



