import requests
from datetime import datetime

parameters = {
    "lat" : -10.406680 ,
    "lng" : -36.436600,
    "formatted " : 0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params= parameters)
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(data)

sunrise_time = int(sunrise[0])
sunset_time = int(sunset[0])
time_now = datetime.now()
current_time = time_now.hour

#If the iss is close to my position
#Send mail to me





