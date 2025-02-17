from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def ScrapeNewsFromWeb(query,num_articles=8):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    driver=webdriver.Chrome(options=chrome_options)

    articles=[]
    transformed_query=query.replace(" ","+")
    url=f"https://www.google.com/search?q={transformed_query}&sca_esv=7e8fd767af5eb3c9&biw=1480&bih=750&tbm=nws&sxsrf=AHTn8zr-ffOFJFNzoMBK4EgF10VsFa-ehQ%3A1739706553540&ei=udCxZ6PSIO2W4-EPro3c8A8&ved=0ahUKEwjjkoz5j8iLAxVtyzgGHa4GF_4Q4dUDCA8&uact=5&oq=Delhi+Railway+station+accident+20+dead&gs_lp=Egxnd3Mtd2l6LW5ld3MiJkRlbGhpIFJhaWx3YXkgc3RhdGlvbiBhY2NpZGVudCAyMCBkZWFkMgUQIRigATIFECEYoAFIsQtQzgFY7whwAHgAkAEAmAGAAqABggqqAQUwLjEuNbgBA8gBAPgBAZgCA6ACggWYAwCIBgGSBwUwLjEuMqAHmBo&sclient=gws-wiz-news"
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(10)

    response=driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    element = soup.find_all("div", class_="n0jPhd ynAwRc MBeuO nDgy9d")
    for ind, elem in enumerate(element):
        if ind >= num_articles:
            break

        articles.append(elem.get_text())

    driver.quit()
    print("News scraped from web....")
    return articles

if __name__=="__main__":
    query="Delhi Railway station accident 20 dead"
    articles=ScrapeNewsFromWeb(query)
    print(articles)
    print(len(articles))


