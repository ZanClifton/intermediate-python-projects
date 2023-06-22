import requests
from datetime import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
LATITUDE = float(os.getenv("LATITUDE"))
LONGITUDE = float(os.getenv("LONGITUDE"))

PARAMETERS = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

def iss_is_above():
    if (latitude > LATITUDE - 5 and
        latitude < LATITUDE +5 and
        longitude > LONGITUDE - 5 and
        longitude < LONGITUDE +5):
        return True
    else:
        return False

def it_is_dark():
    if (hour > sunset or
        hour < sunrise):
        return True
    else:
        return False

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

latitude = float(iss_response.json()["iss_position"]["latitude"])
longitude = float(iss_response.json()["iss_position"]["longitude"])

iss_position = (latitude, longitude)

sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json", params=PARAMETERS)
sun_response.raise_for_status()
data = sun_response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

now = dt.now()
hour = now.hour

loop = 0

while True:
    time.sleep(60)
    loop += 1
    if iss_is_above() and it_is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject:Look up!\n\nThe ISS is above you!",
            )
        print("The ISS is above, it's night time, and an email has been sent telling you to look up.\n\nYou may be able to see the International Space Station right now.\n\n_____\n\n")
    else:
        print(f"Times checked: {loop}\n\nThe script is still checking, but the conditions aren't right for seeing the International Space Station at the moment.\n\nNo email has been sent.\n\n_____\n\n")
