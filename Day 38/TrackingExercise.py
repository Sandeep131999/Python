from copyreg import dispatch_table

import requests


#The final goal is to create a Google Doc with simple workout tasks that calculate calories based on correctly entered parameters

#Todo 1 : Find the calories

API_Key = "nix_live_3NqDWDhPuH8c4ZI7Cjsv7IrxDoVznMNW"
App_ID = "app_9c4bbe9929d641b39a746923"
Base_URL = "https://app.100daysofpython.dev"
Nutrition_Api_Endpoint = "/v1/nutrition/natural/exercise"
Final_URL = Base_URL + Nutrition_Api_Endpoint
Health_Check_Endpoint = "https://app.100daysofpython.dev/healthz"

#Checking the heath of the api before proceeding



headers = {
    "x-app-id": App_ID,
    "x-app-key": API_Key,
    "Content-Type": "application/json"
}

data = {
    "query": "swam for 1 hour"
}
response = requests.post(url=Final_URL,headers=headers,json=data)

data = response.json()
print(data)







