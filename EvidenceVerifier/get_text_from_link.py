from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def GetTextFromLink(link:str):
    driver=webdriver.Chrome()

    driver.get(link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(10)

    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    text=[]
    elements=soup.find_all("p")
    for elem in elements:
        inst=elem.get_text()
        inst=inst.strip()
        if len(inst.split(" "))>3:
            text.append(inst)

    print("Text Extracted from link...")
    return text




if __name__=="__main__":
    link="https://www.ndtv.com/india-news/kiit-campus-tense-after-nepal-student-suicide-many-claim-forced-to-leave-7731253"
    print(GetTextFromLink(link))