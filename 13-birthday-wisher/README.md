<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/birthday-wisher.jpeg" width=250px align=right alt="Birthday Wisher"/>

# Birthday Wisher

This app, using [SMPT](https://sendgrid.com/blog/what-is-an-smtp-server/), uses a saved csv file of birthdays of your favourite people and emails them on their birthday.

There are 5 different birthday emails and one will be randomly selected each time someone is emailed.

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

- Look for the `.env.example` file
- Create a new file called `.env` in the same folder
- Copy the contents of the `.env.example` file into the `.env` file
- Set the `EMAIL` variable to the email address you'd like to send from, e.g. "my.email@gmail.com"
- Set the `PASSWORD` variable to the 16-digit code you generated within your Google account, e.g. "1234567890123456"

### Updating `birthdays.csv`

In the root of this folder there is a file called `birthdays.csv`. You should manually add the names, email addresses and birth dates of those you'd like to email into this file.

I recommend adding a test record with today's date and an email address whose inbox you can check, as well, so you can see if the program is running as expected.

### Updating `main.py`

On line 13 there is a variable `YOUR_NAME_HERE = "Zan"` Please replace "Zan" with your own name in quotes, unless you'd like everyone on your birthday list to believe I'm emailing them instead of you.

Once you have updated `birthdays.csv` and `main.py`, run the script with the instructions available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects#readme), and check it's working by looking in the recipient email inbox.

It's likely that the email will go into the spam folder, so please remember to whitelist the sender address in the recipient email contacts.

### Running This From The Cloud

Using the free Beginner tier of [Python Anywhere](https://www.pythonanywhere.com), you can set this script to run every day at a particular time.

Before uploading your files, you will need to edit `main.py` once more, this time adding your email address and password into their respective variables on lines 15 and 16.

```
my_email = "change.this@example.com"
my_secret = "1234567890123456"
```

Only you will have access to this code from inside your account, so your information is as safe as it can be, uploaded privately.

Comment out lines 8, 9 and 11 by adding a `#` at the beginning of each line:

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
- Upload your edited `main.py` and `birthdays.csv` files using the yellow "Upload a file" button
- On the left hand side of the page, create a new directory under 'Directories' called "letter_templates"
- Navigate into this folder and upload the five letter templates, `letter_1.txt` to `letter_5.txt`
- Finally, select the "Tasks" tab within Python Anywhere and set the task to run daily at the time of your choice
