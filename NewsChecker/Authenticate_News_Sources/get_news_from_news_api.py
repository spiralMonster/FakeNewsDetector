from newsapi import NewsApiClient
import os
from dotenv import load_dotenv
load_dotenv()

#Params:
# query: str
# from_date and to_date in format of YYYY-MM-DD
# num_results_to_return : The number of results to be returned.

def GetNewsFromNewsAPI(query,from_date,to_date,num_results_to_return=3):
    news_articles = []
    try:
        client = NewsApiClient(api_key=os.environ["NEWS_API_KEY"])

        response = client.get_everything(
            q=query,
            language="en",
            from_param=from_date,
            to=to_date
        )
        num_result = response["totalResults"]
        if num_result > 0:
            if num_result<=num_results_to_return:
                for article in response["articles"]:
                    description = article["description"]
                    news_articles.append(description)

            else:
                for article in response["articles"][:num_results_to_return]:
                    description = article["description"]
                    news_articles.append(description)


        else:
            print("News not found!!!!!")

    except Exception as e:
        print(e)

    return news_articles

if __name__=="__main__":
    query=""
    from_date="2025-02-01"
    to_date="2025-12-15"

    news_articles=GetNewsFromNewsAPI(
        query=query,
        from_date=from_date,
        to_date=to_date
    )
    print(news_articles)


