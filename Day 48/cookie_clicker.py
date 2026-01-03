from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://orteil.dashnet.org/cookieclicker/"

# Create Edge options
edge_options = webdriver.EdgeOptions()

# Start WebDriver
driver = webdriver.Edge(options=edge_options)
driver.get(URL)

wait = WebDriverWait(driver, 30)

# ---- Select Language (English) ----
language = wait.until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
language.click()

# ---- Wait for the big cookie ----
cookie = wait.until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

# ---- Click the cookie ----
cookie.click()
