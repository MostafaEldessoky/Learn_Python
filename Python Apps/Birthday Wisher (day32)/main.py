import smtplib
import datetime as dt
from random import choice

with open("quotes.txt") as f:
    q = f.readlines()

r = choice(q)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    my_email = "moustafa.eldesouky@gmail.com"
    my_password = "Mostafa@751995"
    to_email = "moustafa.eldesouky@outlook.com"
    massage = f"Subject:Random_Quotes\n\n{r}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=massage)

