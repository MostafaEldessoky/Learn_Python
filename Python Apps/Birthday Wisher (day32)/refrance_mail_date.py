# ----------------------------send email---------------------------------------
import smtplib

my_email = "moustafa.eldesouky@gmail.com"
my_password = "Mostafa@751995"
to_email = "moustafa.eldesouky@outlook.com"
massage = "Subject:test\n\nhello world"
with smtplib.SMTP("smtp.gmail.com") as connection:
    # for security
    connection.starttls()
    # login to my account to be able to send mail from it
    connection.login(user=my_email, password=my_password)
    # email body
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=massage)
# -------------------------------date time-----------------------------------
import datetime as dt

# create object with now time state
now = dt.datetime.now()
# return attributes from now time state
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(now, year, month, day, hour, minute, second)
# create object with specifics time state
date_of_birthday = dt.datetime(year=2022, month=7, day=27)
print(date_of_birthday)