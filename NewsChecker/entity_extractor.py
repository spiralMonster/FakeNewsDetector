import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from NewsChecker.entity_extractor_specs import EntityExtractorSpecs
load_dotenv()

def EntityExtractor(news):
    llm=ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ['GOOGLE_GEMINI_API_KEY']
    ).with_structured_output(EntityExtractorSpecs)

    system_msg="""
    You are given a news.Your job is to extract the important entities from the news.
    """

    prompt=ChatPromptTemplate.from_messages(
        [
            ("system",system_msg),
            ("human","{news}")
        ]
    )

    entity_extractor_chain=prompt|llm
    entities=entity_extractor_chain.invoke({"news":news}).entities
    return entities

if __name__=="__main__":
    print(EntityExtractor("""
    Breitbart Reports On Bill Gates Being Caught Red Handed Running A Fraudulent Scheme Against President Trump & RFK Jr.
    """))
