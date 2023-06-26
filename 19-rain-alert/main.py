import json
import requests
import time
import os
from dotenv import load_dotenv

from datetime import datetime
from twilio.rest import Client

load_dotenv()

ONECALL_API_KEY = os.getenv("ONECALL_API_KEY")
ONECALL_ENDPOINT = os.getenv("ONECALL_ENDPOINT")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NO = os.getenv("TWILIO_PHONE_NO")

now = time.time()

weather_parameters = {
    "appid": ONECALL_API_KEY,
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "minutely,daily,alerts"
}

onecall_response = requests.get(ONECALL_ENDPOINT, params=weather_parameters) # forecast
onecall_response.raise_for_status()
json_data = onecall_response.json()

weather_data = json_data["hourly"]

weather_slice = {hour["dt"]: hour["weather"][0]["id"] 
                for hour in weather_data[:12]}

will_rain = False

for item in weather_slice:
    condition_code = weather_slice[item]
    if condition_code < 700:
        will_rain = True

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if will_rain:
    message = client.messages \
        .create(
            body="Bring a brolly! ☔☔☔",
            from_=TWILIO_PHONE_NO,
            to=RECIPIENT_PHONE_NUMBER
        )

    print(message.sid)
