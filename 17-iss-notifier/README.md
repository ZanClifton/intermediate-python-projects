<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/iss-notifier.png" width=700px align=right alt="ISS Notifier"/>

# ISS Notifier

This app, using [SMPT](https://sendgrid.com/blog/what-is-an-smtp-server/), sends a notification to your email when the International Space Station is above you, and it's dark enough to see it.

It compares your latitude and longitude with that of the ISS and can be left to run on your local machine, where it will check the conditions every 60 seconds.

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
- Rename the `.env.example` file to `.env`
- `SENDER_EMAIL=""` - Set this variable to the email address you'd like to send from, i.e. the sender email you created above
- `PASSWORD=""` - Set this to the 16-digit code you generated within your Google account, e.g. "1234567890123456"
- `RECIPIENT_EMAIL=""` - This is the address you want to receive the email at
- `LATITUDE=""` and `LONGITUDE=""` - You will need to find the `LATITUDE` for your location and enter it here (I used [Google Maps](https://www.google.com/maps) for this)
  - In a Google Maps coordinate pair, latitude (north-south) is listed first, followed by longitude (east-west). You can find them in the URL after

Once you have updated the environment variables, run the script with the instructions available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects#readme). You'll know if it's working after 60 seconds, as it will output information to the console.

It's likely that the email will go into the spam folder, so please remember to whitelist the sender address in the recipient email contacts.
