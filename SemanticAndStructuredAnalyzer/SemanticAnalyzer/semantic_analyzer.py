import json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from get_model import GetModel
from data_preprocessing import DataPreprocessing
from reasoning_semantic_analyzer import ReasoningSemanticAnalyzer

def SemanticAnalyzer(posted_article:str=None):
    response={}

    embedding_path="../Data/glove.6B.100d.txt"
    model_weights_path="../Models/lstm_model_weights.weights.h5"
    word_index_path="../Models/word_index.json"
    tokenizer_path="../Models/tokenizer.json"

    model=GetModel(model_weights_path=model_weights_path,embedding_path=embedding_path,word_index_path=word_index_path)
    with open(tokenizer_path,"r") as file:
        tokenizer_json=json.load(file)
        tokenizer=tokenizer_from_json(tokenizer_json)

    data=DataPreprocessing(posted_article=posted_article,tokenizer=tokenizer)

    pred=model.predict(data,batch_size=1)[0][0]
    print("Model has predicted...")

    if pred>0.5:
        response["news_authenticity"] = "Real"
        response["confidence_score"]=pred

    else:
        response["news_authenticity"]="Fake"
        response["confidence_score"]=1-pred

    response["reason"]=ReasoningSemanticAnalyzer(model_prediction=pred,
                                                 confidence_score=response["confidence_score"],
                                                 posted_article=posted_article)

    response["remarks"]="Done"
    print("Semantic Analyzer completed....")
    return response









if __name__=="__main__":
    posted_article="""
    A Nepali student studying in the third year of B-Tech committed suicide in the hostel yesterday. It is suspected that the student was in a love affair with another student studying at KIIT. It is suspected that the student may have committed suicide due to some reason," said the statement.
    """
    SemanticAnalyzer(posted_article=posted_article)
