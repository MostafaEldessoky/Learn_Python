from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def action1():
    entry3.delete(first=0, last=END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    x = [random.choice(letters) for _ in range(0, 12)]
    y = [random.choice(symbols) for _ in range(0, 4)]
    z = [random.choice(numbers) for _ in range(0, 8)]
    a = x + y + z
    random.shuffle(a)
    out = ''.join(a)
    entry3.insert(0, string=f"{out}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def action2():
    if len(entry1.get()) == 0:
        messagebox.showinfo(title="Message", message="please enter your website")
    elif len(entry2.get()) == 0:
        messagebox.showinfo(title="Message", message="please enter your email/username")
    elif len(entry3.get()) == 0:
        messagebox.showinfo(title="Message", message="please enter your password")
    else:
        x = messagebox.askokcancel(title="Massage", message="are you sure you want to save these data")
        if x:
            a1 = entry1.get()
            a2 = entry2.get()
            a3 = entry3.get()
            new_info = {a1: {"email/username": a2, "password": a3}}

            try:
                with open("Passwords.json", "r") as j:
                    data = json.load(j)
                    data.update(new_info)
            except FileNotFoundError:
                with open("Passwords.json", "w") as j:
                    json.dump(new_info, j, indent=4)
            else:
                with open("Passwords.json", "w") as j:
                    json.dump(data, j, indent=4)
            finally:
                with open("Passwords.txt", "a") as p:
                    p.write(f"{a1}  |  {a2}  |  {a3}\n")

            entry1.delete(first=0, last=END)
            entry2.delete(first=0, last=END)
            entry3.delete(first=0, last=END)
            messagebox.showinfo(title="Message", message="your data saved correctly")


# ---------------------------- SEARCH ------------------------------- #
def action3():
    try:
        with open("Passwords.json", "r") as j:
            data = json.load(j)
            x = data.get(f"{entry1.get()}")
        if x is not None:
            messagebox.showinfo(title="Message",
                                message=f"Website: {entry1.get()}\nEmail/UserName: {x['email/username']}\nPassword: "
                                        f"{x['password']}")
        elif entry1.get() == "":
            messagebox.showinfo(title="Message", message="Enter the website please")
        else:
            messagebox.showinfo(title="Message", message="this website is not found in your data")
    except FileNotFoundError:
        messagebox.showinfo(title="Message", message="you dont have any data stored yet")


i = 0


def action4():
    my_emails = ["moustafa.eldesouky@gmail.com", "moustafa.eldesouky@outlook.com", "moustafa.eldesouky@icloud.com"]
    global i
    if i != 3:
        entry2.delete(first=0, last=END)
        entry2.insert(0, string=f"{my_emails[i]}")
        i += 1
        if i == 3:
            i = 0


# ---------------------------- UI SETUP ------------------------------- #

w = Tk()
w.minsize(width=500, height=300)
w.title("Password Manger")
w.config(padx=20, pady=20)

password_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website", font=("Courier", 10, "bold"))
label1.grid(column=0, row=1)

label2 = Label(text="Email/UserName:", font=("Courier", 10, "bold"))
label2.grid(column=0, row=2)

label3 = Label(text="Password", font=("Courier", 10, "bold"))
label3.grid(column=0, row=3)

entry1 = Entry(width=32)
entry1.focus()
entry1.grid(column=1, row=1)

entry2 = Entry(width=32)
entry2.grid(column=1, row=2)

entry3 = Entry(width=32)
entry3.grid(column=1, row=3)

button1 = Button(text="Generate Password", command=action1, width=14)
button1.grid(column=2, row=3)

button2 = Button(text="Add", command=action2, width=43)
button2.grid(column=1, row=4, columnspan=2)

button3 = Button(text="Search Website", command=action3, width=14)
button3.grid(column=2, row=1)

button4 = Button(text="Add Email", command=action4, width=14)
button4.grid(column=2, row=2)

w.mainloop()
