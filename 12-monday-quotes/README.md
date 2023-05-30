<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/quote-email.jpeg" width=250px align=right alt="Language Flash Cards"/>

# "Monday" Quotes

This app, using [SMPT](https://sendgrid.com/blog/what-is-an-smtp-server/), lets you set a day of the week and email yourself (or a friend) an inspirational quote on that day.

There are just over 100 quotes, and one is randomly selected each time the program is run.

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
- Set the `RECIPIENT` variable to the email of any account you would like to receive the email in for testing (ensure you have access to this inbox)

### Picking A Day

On line 30, you can change the day of the week to any you like. This means that whichever weekday you want to test the script, you can set this to match, run the script with the instructions available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects#readme), and check it's working by looking in the recipient email inbox.

It's likely that the email will go into the spam folder, so please remember to whitelist the sender address in the recipient email contacts.
