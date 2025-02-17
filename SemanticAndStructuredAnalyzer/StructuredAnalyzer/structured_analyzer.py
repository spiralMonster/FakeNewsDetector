## Here we are using GradientBoostClassifier as it was best among all the models.

import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingClassifier
from feature_extractor import FeatureExtractor
from reasoning_structured_analyzer import ReasoningStructuredAnalyzer

def StructuredAnalyzer(posted_article:str):
    response={}
    model=joblib.load("../Models/gradient_boosting_classifier.pkl")
    data=FeatureExtractor(posted_article)
    print(data)
    pred=model.predict(data)[0]
    print(pred)

    if pred==1:
        response["news_authenticity"]="Real"
    else:
        response["news_authenticity"]="Fake"

    reason=ReasoningStructuredAnalyzer(response["news_authenticity"],posted_article)
    response["reason"]=reason
    response["remarks"]="Done"
    print("Structured Analyzer completed....")
    return response






if __name__=="__main__":
    posted_article="""
    Indian national Mandeep Singh, who was caught while trying to enter the United States via the illegal ‘donkey’ route and was in the second batch of 116 illegal immigrants deported by the US to India, has recalled being forced to deal with crocodiles and snakes, trim his beard despite being a Sikh, and going without food for days.
    """
    print(StructuredAnalyzer(posted_article))



