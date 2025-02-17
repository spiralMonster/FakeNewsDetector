import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from news_authenticator_specs import NewsAuthenticatorSpecs
from dotenv import load_dotenv
import time
load_dotenv()

def NewsAuthenticator(posted_article:str,real_article:str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(NewsAuthenticatorSpecs)

    template="""
    You are given with the posted news article and the real news article.
    Your job is to decide whether the posted news article is authentic or not by analyzing it with real news article.
    Give your answer has either "Yes" or "No".
    And also provide the reason why you think the posted article is authentic or not.
    Posted article:
    {posted_article}
    Real article:
    {real_article}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["posted_article","real_article"])

    authenticity_chain=prompt|llm
    result={}

    authenticator_response=authenticity_chain.invoke({
        "posted_article":posted_article,
        "real_article":real_article
    })

    result["news_authenticity"]=authenticator_response.news_authenticity
    result["reason"]=authenticator_response.reason
    print("News Authentication completed.....")
    time.sleep(3)
    return result
