import os
import time
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from compare_news_articles_specs import CompareNewsArticleSpecs
from dotenv import load_dotenv
load_dotenv()

def CompareNewsArticles(posted_article:str,supporting_article:str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(CompareNewsArticleSpecs)

    template="""
    You are provided with the posted news article and its supporting news article.
    Your job is to decide whether these articles are similar to each other or not in conveying information.
    Also provide reason why do you think they are similar or not.
    
    Posted article:
    {posted_article}
    
    Supporting article:
    {supporting_article}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["posted_article","supporting_article"])

    comparison_chain=prompt|llm

    results={}
    response=comparison_chain.invoke({
        "posted_article":posted_article,
        "supporting_article":supporting_article
    })

    results["reason"]=response.reason
    results["evidence_comparison"]=response.evidence_comparison

    time.sleep(3)
    print("Evidence Compared...")
    return results