#Scrap the data from amazon site send the alert message when sales prices
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
amazon_site_data  = response.text
soup = BeautifulSoup(amazon_site_data,'html.parser')

product_price = soup.select('.twisterSwatchPrice')[0]
product_price_trim = " "

for i in product_price:
    product_price_trim = i.getText().strip().replace("$","")

print(product_price_trim)


msg = EmailMessage()
msg['Subject'] = 'Subject of mail sent by Python code'
msg['From'] = os.getenv("EMAIL_ADDRESS")
msg['To'] = os.getenv("EMAIL_ADDRESS")

msg.set_content('Content of mail sent by Python code')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

