from EvidenceVerifier.evidence_verifier import EvidenceVerifier
from NewsChecker.news_checker import NewsChecker
from SemanticAndStructuredAnalyzer.SemanticAnalyzer.semantic_analyzer import SemanticAnalyzer
from SemanticAndStructuredAnalyzer.StructuredAnalyzer.structured_analyzer import StructuredAnalyzer

def FakeNewsDetector(title:str,content:str,link:str):
    evidence_verifier_results={}
    final_results={}

    if link:
        evidence_verifier_results=EvidenceVerifier(posted_article=content,link=link)

    else:
        evidence_verifier_results["remarks"]="Error"

    news_checker_results=NewsChecker(posted_article=title)
    structured_analyzer_results=StructuredAnalyzer(posted_article=content)
    semantic_analyzer_results=SemanticAnalyzer(posted_article=content)

    final_results["NewsChecker"]=news_checker_results
    final_results["StructureAnalyzer"]=structured_analyzer_results
    final_results["SemanticAnalyzer"]=semantic_analyzer_results
    final_results["EvidenceVerifier"]=evidence_verifier_results

    return final_results