from bs4 import BeautifulSoup as bs4
import requests

URL = "https://weather.com/en-GB/forecast/allergy/l/Warrington+England?canonicalCityId=5edf6e8b69e4c1d4bbe4bbc73c528bdbe3bba0bc3ec57a57e7d54878d3d86dfe"

page = requests.get(URL)

soup = bs4(page.content, "html.parser")

# print(soup.find_all("strong")) # Prints all the <strong> tags in the document (these only apply to the pollen results)

string = f"""
3 Day Pollen Breakdown

Tree Pollen:
Today: {soup.find_all("strong")[0].string}
Tomorrow: {soup.find_all("strong")[1].string}
Day After: {soup.find_all("strong")[2].string}

Grass Pollen: 
Today: {soup.find_all("strong")[3].string}
Tomorrow: {soup.find_all("strong")[4].string}
Day After: {soup.find_all("strong")[5].string}

Ragweed Pollen:
Today: {soup.find_all("strong")[6].string}
Tomorrow: {soup.find_all("strong")[7].string}
Day After: {soup.find_all("strong")[8].string}
"""


with open("data.txt", "w") as file:
    file.write(string)
