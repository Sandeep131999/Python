import requests
from bs4 import BeautifulSoup
"""Scraping bill bard to fetch the top 100 songs add them to my spotify playlist """
# pass_date = input("which year do you want to travel to ? Type the date in the format YYYY-MM-DD")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
URL = "https://www.billboard.com/charts/hot-100/" + "1999-06-13"
response = requests.get(url=URL,headers=header)
movies_website = response.text
soup = BeautifulSoup(movies_website,'html.parser')
song_names_spans = soup.select("li ul li h3")
songs_name = [song.getText().strip() for song in song_names_spans ]


