import os
import time
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from reasoning_structured_analyzer_specs import ReasoningStructuredAnalyzerSpecs
from dotenv import load_dotenv
load_dotenv()

def ReasoningStructuredAnalyzer(news_authenticity:str,posted_article:str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.4,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(ReasoningStructuredAnalyzerSpecs)

    template="""
    We have trained a machine learning model to detect the fake or real news.
    The model is trained on the structure of the news including features such as grammatical mistakes,punctuation errors,etc.
    
    You will be provided with the prediction of the ML model along with the news.
    Your job is to provide the reason that why model has given this prediction.
    Try to include evidences from the news article that will support your reasoning.
    Be sure and don't use the phrases such as 'May be' or 'I think so'.
    
    Model Prediction:
    {model_prediction}
    
    News Article:
    {news_article}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["model_prediction","news_article"])

    reasoning_chain=prompt|llm
    response=reasoning_chain.invoke({
        "model_prediction":news_authenticity,
        "news_article":posted_article
    }).reason

    time.sleep(3)
    print("Reason provided...")
    return response