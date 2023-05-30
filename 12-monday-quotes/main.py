import smtplib
import datetime as dt
from random import choice
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_secret = os.getenv("PASSWORD")
recipient_email = os.getenv("RECIPIENT")

message = "Hello"

day_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

now = dt.datetime.now()
today = day_of_the_week[now.weekday()]

quote_of_the_day = ""

if today == "Tuesday":
    with open("./quotes.txt") as quote_list:
        quotes = quote_list.readlines()
        quote_of_the_day = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypts email in case it's intercepted
        connection.login(user=my_email, password=my_secret)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:{today} Inspiration!\n\n{quote_of_the_day}\n\nHave a happy {today}!",
        )
