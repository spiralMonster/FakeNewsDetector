import os
import time
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from combine_news_article_specs import CombineNewsArticleSpecs
from typing import List
from dotenv import load_dotenv
load_dotenv()


def CombineNewsArticles(news_articles:List):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(CombineNewsArticleSpecs)

    template="""
    You are provided with a list of news articles.
    Your job is to combine them and create a short and crisp final news article that will cover all the details.
    List of news article:
    {list_news_article}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["list_news_article"])

    combine_news_chain=prompt|llm

    final_news=combine_news_chain.invoke({
        "list_news_article":news_articles
    }).final_news

    time.sleep(3)
    print("News articles combined...")
    return final_news

