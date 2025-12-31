from bs4 import BeautifulSoup
import requests
import pandas as pd

#WEB SCRAPPiNG THROUGH WEBSITES
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.select(".athing")
article_texts = []
article_links = []
article_upvote = []

for article in articles:
    #CSS Selector
    title_tag = article.select_one(".titleline a")
    #Score tag
    score_tag = article.find_next_sibling("tr").select_one(".score")

    if title_tag and score_tag:
        article_texts.append(title_tag.get_text(strip=True))
        article_links.append(title_tag.get("href"))
        article_upvote.append(int(score_tag.get_text().split()[0]))

max_upvote = max(article_upvote)
index = article_upvote.index(max_upvote)

print(article_texts[index])
print(article_links[index])
print(article_upvote[index])


# """If we dont use encoding while reading the html file we will get this error cp932 binary reading error"""
# with open("Portfolio.html", encoding="utf-8") as file:
#       contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# for link in soup.find_all('p'):
#     print(link)
