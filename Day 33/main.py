import time
from multiprocessing.managers import convert_to_error

import requests
from datetime import datetime
import smtplib

from pandas.core.dtypes.common import is_scipy_sparse
MY_EMAIL = "sandeepa13.1999@gmail.com"
MY_PASS = "jlpw biow faqd nrte"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

"""To Check the iss position near to my location"""
def iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True


"""To check the night time"""
def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    resp = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    resp.raise_for_status()
    da = resp.json()
    sunrise = int(da["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(da["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True


if iss_over_head() and is_night():
    time.sleep(10)
    connection = smtplib.SMTP("smtp@gmail.com",587)
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASS)
    connection.sendmail(
        from_addr= MY_EMAIL,
        to_addrs= MY_EMAIL,
        msg = "subject : lookup \n\n The iss is above you in the sky."
    )

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



