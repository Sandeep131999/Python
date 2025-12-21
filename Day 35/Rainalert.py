import requests
import send_sms
LAT = 13.339168
LONG = 77.113998

#Open weather api
API_KEY = "e91fac2dac83b27f22c7afc39d6088fb"

weather_ids = []

will_rain = False
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&cnt=4&units=metric&appid={API_KEY}")
weather_data = response.json()
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code )<700:
        will_rain = True

# if will_rain :

print("bring an umbrella")

send_sms.send_message("bring an umbrella, Today is so much rain ⛈️☔🌦️")




#Using PYTHON anywhere we can deploy the scheduler in online

#Store the Keys in Environment variables