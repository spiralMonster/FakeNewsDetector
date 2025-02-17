from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from select_best_news_query_specs import SelectBestNewsSearchSpecs
import os
import time
from typing import List
from dotenv import load_dotenv
load_dotenv()

def SelectBestNewsSearch(news_search_queries:List):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(SelectBestNewsSearchSpecs)

    template="""
    You are given three queries which are used to search the news on the web.
    Return the best query which will be produce good search results on web.
    Queries:
    {queries}
    """

    prompt=ChatPromptTemplate.from_template(template=template,
                                            input_variable=["queries"])

    best_news_search_chain=prompt|llm
    best_search=best_news_search_chain.invoke({
        "queries":news_search_queries
    }).best_search
    print("Best news search query selected....")
    time.sleep(5)
    return best_search


if __name__=="__main__":
    queries=['Delhi Railway station accident 18 dead', '18 dead several injured Delhi Railway station', 'Delhi Railway station incident several injured']
    print(SelectBestNewsSearch(queries))
