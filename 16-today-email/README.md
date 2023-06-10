<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/today-email.png" width=250px align=right alt="Today Email"/>

# Today Email

This app, using [SMPT](https://sendgrid.com/blog/what-is-an-smtp-server/), uses several APIs, and one instance of webscraping, to gather information and assemble it into a unique daily email.

The template includes an inspirational quote from [Zen Quotes](zenquotes.io), and one from [Kanye](kanye.rest), sunrise and sunset times from [Sunrise Sunset](https://sunrise-sunset.org/api), scrapes pollen data from [The Weather Channel website](weather.com) using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and adds a snapshot of the current weather at a particular location, provided by [Weatherstack](https://weatherstack.com).

## How To Set Up And Run This Project

### Setting Up Your 'Sender' Gmail Address

Begin by creating a new [Google account](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp). As you will need to use less secure settings to make this work, it's safest to set up a completely new account (with a unique password, of course - generate one using [Balrog Password Manager](https://github.com/ZanClifton/intermediate-python-projects/tree/main/10-password-manager)!) so that you can send emails without compromising your main account.

Within your Google account, do the following:

- Click your profile picture in the top right of the browser window and select "Manage your Google Account"
- Go to 'Security' on the left hand menu
- Under 'Signing in to Google' select '2-step verification' and set this up for your account
- Return to the Security page
- At the bottom of the page, select App passwords
- Enter a name that helps you remember where you’ll use the app password and select "Generate" to obtain a 16-character code
- Make a note of this code as you will need to add this to your environment variables

### Environment Variables

- Rename the `.env.example` file to `.env`
- `SENDER_EMAIL=""` - Set this variable to the email address you'd like to send from, i.e. the sender email you created above
- `PASSWORD=""` - Set this to the 16-digit code you generated within your Google account, e.g. "1234567890123456"
- `RECIPIENT_EMAIL=""` - This is the address you want to receive the email at
- `LOCATION=""` = This is the city or town name and only appears in the email text; no particular format is needed
- `LATITUDE=""` - You will need to find the `LATITUDE` for the location you want to check and enter it here (I used [Google Maps](https://www.google.com/maps) for this and `LONGITUDE` below)
- `LONGITUDE=""` - You will need to find the `LONGITUDE` for the location you want to check and enter it here
- `POLLEN_URL=""` - go to [The Weather Channel site](https://weather.com/en-GB/forecast/allergy/l/4603e477fe0f51c26997494613a50bf8b3286f12642a6a6432992b2db74243f4) and search for the location you want information for, copying the full URL you are directed to into this variable
- `WEATHERSTACK=""` - You will need to sign up for a free [Weatherstack](https://weatherstack.com/product) account to obtain an API key and add it here
- `WEATHERSTACK_LOCATION=""` - You can pass the name of a city, such as "New York", latitude and longitude such as "40.7831,-73.9712" or a UK/US/Canada zip/postcode, e.g. "99501"

You can now run the script with the instructions available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects#readme), and check it's working by looking in the recipient email inbox. The email text also prints to the console.

It's likely that the email will go into the spam folder, so please remember to whitelist the sender address in the recipient email contacts.

### Running This From The Cloud

Using the free Beginner tier of [Python Anywhere](https://www.pythonanywhere.com), you can set this script to run every day at a particular time.

**Before uploading your files, you will need to edit `main.py`, deleting lines 10-18 and replacing them with all the environment variables from `.env`.**

Only you will have access to this code from inside your account, so your information is as safe as it can be, uploaded privately.

Comment out lines 5, 6 and 8 by adding a `#` at the beginning of each line, or delete them:

```
# import os
# from dotenv import load_dotenv

# load_dotenv()
```

This will prevent these lines of code from running within Python Anywhere.

- Navigate to [Python Anywhere](https://www.pythonanywhere.com)
- Create a new account by selecting "Pricing & Signup" from the topbar of the webpage
- Select "Create a Beginner account" and enter your information on the next screen
- Navigate to the "Files" tab within Python Anywhere
- Upload your edited `main.py` file using the yellow "Upload a file" button
- Finally, select the "Tasks" tab within Python Anywhere and set the task to run daily at the time of your choice
