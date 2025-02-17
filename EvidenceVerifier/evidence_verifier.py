from get_text_from_link import GetTextFromLink
from combine_news_article import CombineNewsArticles
from compare_news_articles import CompareNewsArticles
from semantic_similarity_between_articles import SemanticSimilarityBetweenArticles

def EvidenceVerifier(posted_article:str,link:str):
    text=GetTextFromLink(link=link)
    final_news_article=CombineNewsArticles(news_articles=text)
    result={}
    result=CompareNewsArticles(posted_article=posted_article,supporting_article=final_news_article)
    semantic_similarity_score=SemanticSimilarityBetweenArticles(posted_article=posted_article,
                                                                supporting_evidence=final_news_article)

    result["semantic_similarity_score"]=semantic_similarity_score
    return result

