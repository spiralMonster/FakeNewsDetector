import os
import time
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from reasoning_semantic_analyzer_specs import ReasoningSemanticAnalyzerSpecs
from dotenv import load_dotenv
load_dotenv()

def ReasoningSemanticAnalyzer(model_prediction:str,confidence_score:float,posted_article:str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.4,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(ReasoningSemanticAnalyzerSpecs)

    template="""
    We have trained a LSTM based model to predict whether the news is Real or Fake.
    The model analyzes the semantic structure of the article and gives prediction.
    You are given with the news article,model prediction and the confidence score.
    Your job is to provide the reason that why model has given this prediction.
    Try to include evidences from the news article and explain how it is contributed in model prediction.
    Be sure and don't use the phrases such as 'May be' or 'I think so'.
    
    News Article:
    {news_article}
    
    Model Prediction:
    {model_prediction}
    
    Confidence Score:
    {confidence_score}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["news_article","model_prediction","confidence_score"])

    reasoning_chain=prompt|llm

    reason=reasoning_chain.invoke({
        "news_article":posted_article,
        "model_prediction":model_prediction,
        "confidence_score":confidence_score
    }).reason

    time.sleep(3)
    return reason