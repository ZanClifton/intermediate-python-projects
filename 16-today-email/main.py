import requests
from bs4 import BeautifulSoup as bs4
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
LOCATION = os.getenv("LOCATION")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
POLLEN_URL = os.getenv("POLLEN_URL")
WEATHERSTACK = os.getenv("WEATHERSTACK")
WEATHERSTACK_LOCATION = os.getenv("WEATHERSTACK_LOCATION")

DAY_OF_THE_WEEK = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

SUN_PARAMETERS = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 1,
}

WIND_DIRECTION = {
    "E": "easterly",
    "ENE": "east-northeasterly",
    "ESE": "east-southeasterly",
    "N": "northerly",
    "NE": "northeasterly",
    "NNE": "north-northeasterly",
    "NNW": "north-northwesterly",
    "NW": "northwesterly",
    "S": "southerly",
    "SE": "southeasterly",
    "SSE": "south-southeasterly",
    "SSW": "south-southwesterly",
    "SW": "southwesterly",
    "W": "westerly",
    "WNW": "west-northwesterly",
    "WSW": "west-southwesterly",
}

# Use datetime module to get information about today
now = datetime.now()

day = now.day
month = now.month
year = now.year
weekday = DAY_OF_THE_WEEK[now.weekday()]

# Date message
todays_details = f"Today's Date: {weekday} {day}/{month}/{year}"

# QUOTES
# QOTD
q_response = requests.get('https://zenquotes.io/api/random')
data = q_response.json()[0]
qotd = f"Quote of the day: {data['q']} - {data['a']}"

# KANYE QOTD
k_response = requests.get(url="http://api.kanye.rest")
kotd = k_response.json()["quote"]
kqotd = f"Kanye of the day: {kotd}"

# Email entry
quotes_of_the_day = f"{qotd} \n\n{kqotd}"

# POLLEN COUNT
# Get the html from the weather.com pollen page and turn it into soup
pollen_page = requests.get(POLLEN_URL)
soup = bs4(pollen_page.content, "html.parser")

tree = soup.find_all("strong")[0].string
grass = soup.find_all("strong")[3].string
ragweed = soup.find_all("strong")[6].string

# Email entry
pollen_count = f"""
Today's Pollen in {LOCATION}:
Tree: {tree}
Grass: {grass}
Ragweed: {ragweed}
"""

# SUNRISE AND SUNSET
# Connect to the sunrise-sunset api to get the times for sunrise and sunset today
sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json", params=SUN_PARAMETERS)
sun_response.raise_for_status()
data = sun_response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Email entry
dawn_to_dusk = f"Sunrise: {sunrise}\nSunset: {sunset}"

# Connect to the Weatherstack api to get the weather for today
weather_response = requests.get(url=f"http://api.weatherstack.com/current?access_key={WEATHERSTACK}&query={WEATHERSTACK_LOCATION}")
weather_data = weather_response.json()

cloud_cover = weather_data["current"]["cloudcover"]
feels_like = weather_data["current"]["feelslike"]
humidity = weather_data["current"]["humidity"]
observation_time = weather_data["current"]["observation_time"]
precipitation = weather_data["current"]["precip"]
temperature = weather_data["current"]["temperature"]
visibility_km = weather_data["current"]["visibility"]
weather_desc = weather_data["current"]["weather_descriptions"]
wind_dir = weather_data["current"]["wind_dir"]
wind_speed = weather_data["current"]["wind_speed"]

if visibility_km <= 1:
    visibility = "terrible! Expect road closures and diversions on any journey you make. Stay home; stay safe!"
elif visibility_km <= 2:
    visibility = "poor. There are dangers when driving and you should avoid it if possible."
elif visibility_km <= 5:
    visibility = "hazy, and you should be careful when driving."
else:
    visibility = "good!"

weather_description = ""
if len(weather_desc) == 1:
    weather_description = f"{weather_desc[0].lower()}, "
elif len(weather_desc) == 2:
    weather_description = f"{weather_desc[0].lower()} and {weather_desc[1].lower()}, "
elif len(weather_desc) == 3:
    weather_description = f"{weather_desc[0].lower()}, {weather_desc[1].lower()} and {weather_desc[2].lower()}, " 
else:
    for item in weather_desc:
        weather_description +=f"{weather_desc[item].lower()}, "

wind_direction = WIND_DIRECTION[wind_dir]  

# Email entry
weather_today = f"""
This weather observation for {LOCATION} was taken at {observation_time} UTC.
Today is {weather_description}cloud cover is {cloud_cover}%, and visibility is {visibility}
The current temperature is {temperature} degrees Celsius. It feels like {feels_like}.
Humidity is at {humidity}% and precipitation is {precipitation}mm.
Wind direction is {wind_direction} at {wind_speed}km/h.
"""

# Email in full
message = f"Subject:{todays_details}\n\n{todays_details}\n\n{quotes_of_the_day}\n\n{dawn_to_dusk}\n{pollen_count}{weather_today}\nHave a great {weekday}!\n\nZan\nxxx"

with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=message,
        )

print(message)
