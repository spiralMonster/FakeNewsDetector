import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from NewsChecker.generate_news_search_specs import NewsSearchGeneratorSpecs
load_dotenv()

def NewsSearchGenerator(news_entities):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.4,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(NewsSearchGeneratorSpecs)

    template="""
    You are given a list of entities.
    You have to generate 3 search queries related to those entities to get news about them on search engine.
    **Note**: 
     -A search query should not be more than 10-12 words.
     - Have the correlation between entities in the search query.
    Entities:
    {entities}
    """


    prompt=ChatPromptTemplate.from_template(template=template,input_variable=["entities"])
    news_search_gen_chain=prompt|llm
    news_query=news_search_gen_chain.invoke({"entities":news_entities}).news_search_query
    return news_query


if __name__=="__main__":
    entities=['Breitbart', 'Bill Gates', 'President Trump', 'RFK Jr.']
    news_query=NewsSearchGenerator(entities)
    print(news_query)

