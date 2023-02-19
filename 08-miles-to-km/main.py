from tkinter import *


# calculate function
def calculate():
    number = float(input.get())
    calculation = round(number * 1.609344, 2)
    output.config(text=str(calculation))


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=5, height=5)
window.config(padx=50, pady=50)

# labels
equals = Label(text="is equal to")
equals.grid(column=0, row=1)

km = Label(text="Kilometres")
km.grid(column=2, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

output = Label(text="1.61")
output.grid(column=1, row=1)

# button
calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

# input
input = Entry(width=10)
input.insert(END, string="1")
input.grid(column=1, row=0)

# keep window open
window.mainloop()
