import os
import worldnewsapi
from dotenv import load_dotenv
load_dotenv()

#Params:
# query : Give directly the entities extracted separated by space and don't generate the search query.
# from_time and to_time format : YYYY-MM-DD HH:mm:ss  Example: '2025-01-26 00:00:00'
# num_results_to_return : The number of results to be returned.


def GetNewsFromWorldNewsAPI(query,from_time,to_time,num_results_to_return=3):
    news_articles=[]

    configuration = worldnewsapi.Configuration(
        host="https://api.worldnewsapi.com"
    )

    configuration.api_key['apiKey'] = os.environ["WORLD_NEWS_API_KEY"]
    configuration.api_key['headerApiKey'] = os.environ["WORLD_NEWS_API_KEY"]

    with worldnewsapi.ApiClient(configuration) as client:
        api_instance = worldnewsapi.NewsApi(client)
        text=query
        source_country="in"
        language="en"
        earliest_publish_date=from_time
        latest_publish_date=to_time
        try:
            response = api_instance.search_news(
                text=text,
                source_country=source_country,
                language=language,
                earliest_publish_date=earliest_publish_date,
                latest_publish_date=latest_publish_date

            )
            news=response.to_dict()["news"]
            num_results=len(news)
            if num_results>0:
                if num_results<=num_results_to_return:
                    for article in news:
                        news_articles.append(article["summary"])

                else:
                    for article in news[:num_results_to_return]:
                        news_articles.append(article["summary"])
            else:
                print("No news found!!!!")

        except Exception as e:
            print(e)

        return news_articles


if __name__=="__main__":
    query="RFK Jr."
    from_time="2025-01-26 00:00:00"
    to_time="2025-01-27 00:00:00"

    news_articles=GetNewsFromWorldNewsAPI(
        query=query,
        from_time=from_time,
        to_time=to_time
    )
    print(news_articles)


