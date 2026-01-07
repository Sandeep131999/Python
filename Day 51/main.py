import re

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://appbrewery.github.io/Zillow-Clone/"
DOC_URL = "https://docs.google.com/forms/d/1IfL6fvG2mUK606Y0jZcbDPsC68KiKb0FKqEIVvAg1sE/edit?pli=1"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

alt_list = []
href_list = []
price_list = []
for a in soup.select(".property-card-link"):

    img = a.find("img")
    if img and img.get("alt"):
        alt_list.append(img["alt"])

    if a.get("href"):
        href_list.append(a["href"])

for b in soup.select(".PropertyCardWrapper__StyledPriceLine"):
    cleaned = b.text
    sd = re.sub(r"[^\$\d]", "",cleaned)
    price_list.append(sd)

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(edge_options)
driver.get(DOC_URL)

property_Address = driver.find_element(By.CLASS_NAME, "Hvn9fb ")






