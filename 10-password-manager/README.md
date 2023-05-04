<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/password-manager.png" width=250px align=right alt="Password Manager"/>

# Balrog Password Manager

Using the Tkinter module this app creates a password manager which can store your email address so that you don't have to keep inputting it when you add new sites and can generate a secure password on demand. It can also retrieve stored passwords from the (non-encrypted) json data file. The password is automatically copied to the clipboard for immediate use.

To store your email address, navigate to line 125 of `main.py` and replace 'zan@email.com' with your own email address. When you run the app, you will see your email address pre-populated in the email address field.

To utilise this app, you will need to install the Tkinter module in addition to Pyperclip. You can do this in the command line interface.

**For Tkinter:**

Ubuntu:

```
$ sudo apt-get install python3-tk
```

MacOS:

```
brew install python-tk
```

**For Pyperclip:**

```
$ pip3 install pyperclip
```

The app will generate an unencrypted file for your passwords. Please do not commit genuine passwords to GitHub.

You can try it on [Replit](https://replit.com/@ZanClifton/balrog-password-manager?v=1) directly in your browser, without installing an IDE. If you use the public repl, again, please be sure not to share any genuine passwords as the password file will also be publicly available there.

Instructions for creating a local copy are available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects/blob/main/README.md).
