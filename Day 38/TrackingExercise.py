import requests
from datetime import datetime
import sys
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

#Todo 1 : Find the calories based on the workout activities
API_Key = os.getenv("Exercise_API_Key")
App_ID = os.getenv("Exercise_App_ID")
Base_URL = "https://app.100daysofpython.dev"
Nutrition_Api_Endpoint = "/v1/nutrition/natural/exercise"
Final_URL = Base_URL + Nutrition_Api_Endpoint
Health_Check_Endpoint = "https://app.100daysofpython.dev/healthz"
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_ENDPOINT_UPDATE = "https://api.sheety.co/8fa4502c28026726d45e47fd7ee69599/simpleWorkoutLog/workout/2"
workout_calculating = ""
FILE_NAME = "store_count.txt"
count = 0

user_input = input("Enter something (or leave empty to quit): ").strip()
if not user_input:
    print("No input provided. Exiting...")
    sys.exit()

#Checking the heath of the api before proceeding
check_health = requests.get(Health_Check_Endpoint).json()

#Authentiation headers
headers = {
    "x-app-id": App_ID,
    "x-app-key": API_Key,
    "Content-Type": "application/json"
}
data = {
    "query": user_input
}
#Checking api connection before going to further process
if check_health['status'] == "ok":
    response = requests.post(url=Final_URL,headers=headers,json=data)
    workout_calculating = response.json()["exercises"][0]
    print(workout_calculating)
else:
    print("Please connect the internet")


#Read file
with open(FILE_NAME, "r") as fr:
    count += int(fr.read())

#Todo 2 Write the workouts to spread sheet
payload = {
    "workout": {
        "id": count,
        "date": datetime.today().strftime('%d %b %Y'),
        "exercise": workout_calculating['name'],
        "duration (min)": workout_calculating['duration_min'],
        "caloriesBurned": workout_calculating['nf_calories'],
        "Photo": workout_calculating['photo']['highres'],
    }
}

headers = {
    "Content-Type": "application/json",
}

#Insert the data to google sheets
# response = requests.post(url=SHEET_ENDPOINT, json=payload, headers=headers)

payload_update = {
    "workout": {
        "exercise": "Sandeep",
    }
}

response = requests.put(url=SHEET_ENDPOINT_UPDATE, json=payload, headers=headers)

#update the data of google sheet

#Write file
with open(FILE_NAME, "w") as fw:
   fw.write(str(count+1))






