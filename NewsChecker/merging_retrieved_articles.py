import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from merging_retrieved_articles_specs import MergingRetrievedArticlesSpecs
import time
from typing import List
from dotenv import load_dotenv
load_dotenv()

def MergingRetrievedArticles(retrieved_articles:List):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(MergingRetrievedArticlesSpecs)

    template="""
    You are provided with a list of news article.
    Your job is to aggregate the content of all the articles and create a short and crisp final article.
    Don't forget to include the minute details also.
    Articles:
    {articles}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["articles"])

    merging_articles_chain=prompt|llm
    final_article=merging_articles_chain.invoke({
        "articles":retrieved_articles
    }).final_article
    print("Merged scraped news articles....")
    time.sleep(3)
    return final_article


