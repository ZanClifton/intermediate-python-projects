from bs4 import BeautifulSoup as bs4
# print(soup.find_all("strong")) # Prints all the <strong> tags in the document (these only apply to the pollen results)
import requests

from art import flowers

looking_for_data = "y"

print(
    f"""{flowers}

Hello!

This script scrapes pollen count data from The Weather Channel website and saves it in a text file.

The location for which the data is scraped can be altered by pasting the following URL into your browser and navigating there.

https://weather.com/en-GB/forecast/allergy/l/74d3ef23c255b3c569ef5be6914b31e94000d796f2118d8eba492946e93afe0ceb0a5f8a9ed095c44db7867780433ee3

Once there, search for the location you wish to see data for and select it from the dropdown in the search bar. Copy the entire new URL from the address bar of your browser and provide it when prompted, below.
"""
)

while looking_for_data != "n":
    location = input(
        """
If you will be changing the default location for the pollen count, you can label it here. 

You can choose to leave this input blank. If you do, your data will be labelled as 'Birmingham, England'.

Type here: """
    )

    if location == "":
        location = "Birmingham, England"

    URL = input(
        """

If you have a URL for your chosen location for the pollen count, please enter it here. 

You can leave this blank and data for the default selection of Birmingham, England will be provided.

Type here: """
    )

    if URL == "":
        URL = "https://weather.com/en-GB/forecast/allergy/l/74d3ef23c255b3c569ef5be6914b31e94000d796f2118d8eba492946e93afe0ceb0a5f8a9ed095c44db7867780433ee3"

    try:
        page = requests.get(URL)

        soup = bs4(page.content, "html.parser")

        string = f"""3 Day Pollen Breakdown for {location}
    

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

        print(
            """
All done!

If you are interested in seeing the pollen data this script just scraped from The Weather Channel website at weather.com, please navigate to the data.txt file where this information has been laid out for you.
"""
        )
    except:
        print("\n\nThe URL you entered did not provide the data you were looking for.")

    looking_for_data = input("\n\nWould you like data for another location? y/n ")

print("Thank you for trying out this pollen scraper!")
