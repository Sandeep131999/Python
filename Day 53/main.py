import re
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://appbrewery.github.io/Zillow-Clone/"

#Load the env
load_dotenv()
DOC_URL = os.getenv("DOC_URL")

#Request the URL
response = requests.get(URL)

#Web Scraping to read the dat
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

#To fill the Google form
def fill_google_form(question_text_part, answer):
    """It selects an input or textarea that belongs to a list item (div with role='listitem') which contains the given question text."""
    xpath = f"""
    //div[@role='listitem']
    [.//div[contains(normalize-space(), "{question_text_part}")]]
    //input | //textarea
    """

    field = wait.until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    field.click()
    field.clear()
    field.send_keys(answer)

wait = WebDriverWait(driver, 8)


#Loop the over data to insert the google form sheet
for i in range(len(alt_list)):

    fill_google_form("address of the property", alt_list[i])
    fill_google_form("price per month", price_list[i])
    fill_google_form("link to the property", href_list[i])

    # Click Submit
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']"))
    )
    submit_btn.click()

    # Click "Submit another response"
    another_response = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Submit another response')]")
        )
    )
    another_response.click()






