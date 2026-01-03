from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

#Create and configure the edge web driver
driver = webdriver.Edge(edge_options)

#Naviagete to the wikipedia
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

#Home in on anchor tag using css selectors
article_count  = driver.find_element(By.CSS_SELECTOR, value = "#articlecount a")

#Find element by link text
all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")

#Find the "Search" <input> by Name
search = driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)