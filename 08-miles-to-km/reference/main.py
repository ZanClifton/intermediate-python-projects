from tkinter import *


# functions
def button_clicked():
    label.config(text=input.get())
    button.config(text="Do not press this button again!")


window = Tk()
window.title("Hello, world!")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# label
label = Label(text="This is a label", font=("Arial", 22, "bold"))
label.config(text="This is not a label")
label.config(padx=5, pady=5)
label.grid(column=0, row=0)

# buttons
button = Button(text="Do not press this button!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="This is not a button")
new_button.grid(column=2, row=0)

# entry
input = Entry(width=30)
input.insert(END, string="Actually, this IS a label")
input.grid(column=3, row=2)

# at the bottom
window.mainloop()
