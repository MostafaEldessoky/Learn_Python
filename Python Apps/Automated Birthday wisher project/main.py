# ------------------------ Extra Hard Starting Project ----------------------
# TODO:1. Update the birthdays.csv
# TODO:2. Check if today matches a birthday in the birthdays.csv
# TODO:3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
#  actual name from birthdays.csv
# TODO:4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
from random import choice

my_email = "moustafa.eldesouky@gmail.com"
my_password = "Mostafa@751995"
letter = []

for i in range(1, 4):
    with open(f"letter_{i}.txt") as f:
        letter.append(f.read())

now = dt.datetime.now()

data = pd.read_csv("birthdays.csv")
ck = {data["email"][i]: [data["name"][i], data["month"][i], data["day"][i]] for i in range(len(data["day"]))}

for i, j in ck.items():
    if j[1] == now.month and j[2] == now.day:
        letter[0] = letter[0].replace("[NAME]", j[0])
        letter[1] = letter[1].replace("[NAME]", j[0])
        letter[2] = letter[2].replace("[NAME]", j[0])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=i, msg=f"Subject:HappyBirthDay\n\n{choice(letter)}")
