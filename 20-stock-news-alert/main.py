from twilio.rest import Client
import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWSCATCHER_API_KEY = os.getenv("NEWSCATCHER_API_KEY")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NO = os.getenv("TWILIO_PHONE_NO")

ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWSCATCHER_ENDPOINT = "https://api.newscatcherapi.com/v2/search"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
UP = "🔺"
DOWN = "🔻"

av_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_VANTAGE_API_KEY
}

news_headers = {
    "x-api-key": NEWSCATCHER_API_KEY
    }

news_querystring = {
    "q":f"\"{COMPANY_NAME}\"",
    "lang":"en",
    "sort_by":"relevancy",
    "page":"1",
    "page_size":"3"
}

today = dt.now()
day = today.day
month = today.month
year = today.year

av_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=av_params)
av_response.raise_for_status()
daily_information = av_response.json()["Time Series (Daily)"]
daily_info_list = [daily_information[item]["4. close"] for item in daily_information]

yesterdays_closing_price = float(daily_info_list[0])
day_before_yesterdays_closing_price = float(daily_info_list[1])
difference = abs(float(yesterdays_closing_price - day_before_yesterdays_closing_price))
diff_percent = "{:.2f}".format((difference / yesterdays_closing_price) * 100)

if float(diff_percent) >= 5:
    if yesterdays_closing_price > day_before_yesterdays_closing_price:
        percentage_change_msg = f"{UP}{diff_percent}"
    else:
        percentage_change_msg = f"{DOWN}{diff_percent}"
else: 
    percentage_change_msg = "No significant change"


response = requests.request(
    "GET", 
    NEWSCATCHER_ENDPOINT, 
    headers=news_headers, 
    params=news_querystring
)

articles = response.json()["articles"]

article_list = [f"""{article['title']}
{article['excerpt']}
Read more at {article['clean_url']}""" for article in articles]

sms_message_text = f"""{day}/{month}/{year}
{STOCK}: {percentage_change_msg}%

{article_list[0]}

{article_list[1]}

{article_list[2]}

"""

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages \
    .create(
        body=sms_message_text,
        from_=TWILIO_PHONE_NO,
        to=RECIPIENT_PHONE_NUMBER,
    )

print(message.sid)

