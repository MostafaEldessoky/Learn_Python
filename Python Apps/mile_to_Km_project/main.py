from tkinter import *


def button_clicked():
    x = float(inp.get())
    x = x * 1.6
    my_label4.config(text=f"{x}")


window = Tk()
window.title("Mile To KM Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

my_label1 = Label(text="Miles")
my_label1.place(x=210, y=40)
my_label1.config(padx=10, pady=10)

my_label2 = Label(text="KM")
my_label2.place(x=210, y=80)
my_label2.config(padx=10, pady=10)

my_label3 = Label(text="Is Equal To")
my_label3.place(x=10, y=80)
my_label3.config(padx=10, pady=10)

my_label4 = Label(text="0")
my_label4.place(x=125, y=80)
my_label4.config(padx=10, pady=10)

button = Button(text="Calculate", command=button_clicked)
button.place(x=110, y=120)

inp = Entry(width=10)
inp.place(x=110, y=50)

window.mainloop()
