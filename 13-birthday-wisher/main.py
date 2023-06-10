# 1. Imports and environment variables

import datetime as dt
import pandas
from random import choice
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

YOUR_NAME_HERE = "Zan"

my_email = os.getenv("EMAIL")
my_secret = os.getenv("PASSWORD")

# 2. Check if today matches a birthday in the birthdays.csv
# 2a. Get the birthday CSV data in a dictionary
data = pandas.read_csv("./birthdays.csv")

birthdays = data.to_dict(orient="records")

# 2b. Get today's date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# 2c. Perform the check
for record in birthdays:
    if record["month"] == month and record["day"] == day:
        name = record["name"]
        email = record["email"]

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        templates = [1, 2, 3, 4, 5]
        template = choice(templates)

        with open(f"./letter_templates/letter_{template}.txt") as birthday_letter:
            letter = birthday_letter.read()
            edited_letter = letter.replace("[NAME]", name)
            email = edited_letter.replace("Zan", YOUR_NAME_HERE)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_secret)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=record["email"],
                msg=f"Subject:Happy Birthday, {name}!\n\n{email}",
            )
