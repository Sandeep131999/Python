import requests
import send_sms
import time

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_VANTAGE_API = "O7M9IDMR8PXMR6ZC"
NEWS_API =  "050d74fd2bc641eb824d76d6b1c7ad22"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API
}

params_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data = requests.get(STOCK_ENDPOINT,params)
stock_data = data.json()['Time Series (Daily)']
data_list = [value for (key,value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_data_closing_price = data_list[0]['4. close']
print(yesterday_data_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = data_list[1]['4. close']
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_data_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference/float(yesterday_data_closing_price))*100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.
## STEP 2: https://newsapi.org/
 # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# if diff_percent > 5:
#Using slice operator fetch only 3 data in the list
news_article = requests.get(NEWS_ENDPOINT,params_news)
article = news_article.json()['articles']

#Slice Operator
three_articles = article[:3]

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article = [f"Headline :{article['title']}. \n Breif: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.
for article in formatted_article :
    send_sms.send_message(article)
    time.sleep(7)



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

