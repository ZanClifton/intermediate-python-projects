from tkinter import *


PAYNES_GREY = "#6a6b83"
PLATINUM = "#e7e7e7"
AUBURN = "#a22c29"
EERIE_BLACK = "#191716"
TEKHELET = "#631a86"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_details():
    site = website_input.get()
    name = email_username_input.get()
    pw = password_input.get()
    with open("passwords.txt", "a") as f:
        f.write(f"{site} | {name} | {pw}\n")

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

generate_password_button = Button(text="Create Password")
generate_password_button.grid(column=2, row=3)

window.mainloop()
