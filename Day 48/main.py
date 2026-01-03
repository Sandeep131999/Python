from selenium import webdriver
from selenium.webdriver.common.by import  By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.8158743a-e3ec-4239-b3a8-31bfee7d4a15&dib=eyJ2IjoiMSJ9.h0NXGO4UwWV-XKN55HotZpJrZA1L5wvY2y684Y-OP-F8RB1_pSN97HT7B3wI8UJAonloz0vb1oOJLiQPruiN862UHzo4BhWOZayiLP7gHeUzGtfkd6AvIHy8sBpB4sN1bA6Z7RQOO6UOI9EMvplnRpK1_gD37ZbMhyzCW86UKrSCx9HIRZFAheUOKCsX-UnOm5fOkDWhfCkEOLICVoVe842piqcayYNNOkTBGta4ceE.JSE7tHt80zUdO1KK-rXilIbmhNNn3g8KPAHFhxn3-Ns&dib_tag=se&keywords=cooker&pd_rd_r=687eeb84-4f79-4f2a-ac8c-6ac398fc8a3e&pd_rd_w=nuFkJ&pd_rd_wg=e8pAg&qid=1767374461&sr=8-3&th=1")

price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="")
print(price_dollar.text)


driver.close()
driver.quit()