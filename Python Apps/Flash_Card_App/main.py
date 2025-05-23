from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
timer = ""

try:
    data = pd.read_csv("New_Dic.csv")
    data = data.to_dict()
    data = {data["Arabic"][i]: data["English"][i] for i in range(len(data["Arabic"]))}
    key_lists = list(data.keys())
except FileNotFoundError:
    data = pd.read_csv("My_Dic.csv")
    data = data.to_dict()
    data = {data["Arabic"][i]: data["English"][i] for i in range(len(data["Arabic"]))}
    key_lists = list(data.keys())


def action1():
    global k
    window.after_cancel(timer)
    data.pop(k)
    key_lists.remove(k)
    x = pd.DataFrame(list(data.items()), columns=["Arabic", "English"])
    x.to_csv("New_Dic.csv")
    k = choice(key_lists)
    count_down(2, k)


def action2():
    global k
    window.after_cancel(timer)
    k = choice(key_lists)
    count_down(2, k)


def count_down(count, key):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1, key)
        canvas.create_image(405, 276, image=background1_image)
        canvas.create_text(400, 130, text="English", fill="black", font=("Time New Roman", 24, "italic"))
        canvas.create_text(400, 280, text=f"{data[key]}", fill="black", font=("Time New Roman", 36, "bold"))
        canvas.place(x=40, y=20)
    else:
        canvas.create_image(405, 276, image=background2_image)
        canvas.create_text(400, 130, text="العربية", fill="black", font=("Time New Roman", 24, "italic"))
        canvas.create_text(400, 280, text=f"{key}", fill="black", font=("Time New Roman", 36, "bold"))
        canvas.place(x=40, y=20)


window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR)
window.minsize(width=900, height=700)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)

background1_image = PhotoImage(file="card_front.png")
background2_image = PhotoImage(file="card_back.png")

button1_image = PhotoImage(file="right.png")
button2_image = PhotoImage(file="wrong.png")

button1 = Button(image=button1_image, command=action1)
button1.place(x=650, y=570)

button2 = Button(image=button2_image, command=action2)
button2.place(x=150, y=570)

k = choice(key_lists)
count_down(2, k)

window.mainloop()
