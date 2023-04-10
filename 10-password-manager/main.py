from tkinter import *
from tkinter import messagebox

from random import choice, randint, shuffle

import pyperclip

PAYNES_GREY = "#6a6b83"
PLATINUM = "#e7e7e7"
AUBURN = "#a22c29"
EERIE_BLACK = "#191716"
TEKHELET = "#631a86"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    password_input.delete(0, END)

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_details():
    site = website_input.get()
    name = email_username_input.get()
    pw = password_input.get()


    if len(site) < 1 or len(pw) < 1:
        messagebox.showerror(title="Stop!", message="You must enter both a website name and a password!")

    else:
        is_ok = messagebox.askokcancel(title=site, message=f"You entered: \nWebsite: {site}\nEmail: {name}\nPassword: {pw}\nSave?")
        
        if is_ok:
            with open("passwords.txt", "a") as f:
                f.write(f"{site} | {name} | {pw}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("BALROG Password Manager")
window.config(padx=50, pady=50, bg=PLATINUM)

canvas = Canvas(width=200, height=200, bg=PLATINUM, highlightthickness=0)
logo = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website", bg=PLATINUM)
website.grid(column=0, row=1)

email_username = Label(text="Email/Username", bg=PLATINUM)
email_username.grid(column=0, row=2)

password = Label(text="Password", bg=PLATINUM)
password.grid(column=0, row=3)

website_input = Entry(width=42)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_username_input = Entry(width=42)
email_username_input.insert(0, "zan@email.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=24)
password_input.grid(column=1, row=3)

add_button = Button(text="Add", width=40, command=save_details)
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(text="Create Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

window.mainloop()
