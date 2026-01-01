#Scrap the data from amazon site send the alert message when sales prices
import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
amazon_site_data  = response.text
soup = BeautifulSoup(amazon_site_data,'html.parser')

product_price = soup.select('.twisterSwatchPrice')[0]
product_price_trim = " "

for i in product_price:
    product_price_trim = i.getText().strip().replace("$","")

