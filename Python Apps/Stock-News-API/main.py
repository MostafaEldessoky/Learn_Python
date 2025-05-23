import requests
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK = "TESLA"
COMPANY_NAME = "Tesla Inc"

now = datetime.today()
y = now - timedelta(days=1)
p = now - timedelta(days=2)
y_year = str(y.year)
y_month = y.month
y_day = y.day
p_year = str(p.year)
p_month = p.month
p_day = p.day
if y_month < 10:
    y_month = "0" + str(y_month)
else:
    y_month = str(y_month)
if p_month < 10:
    p_month = "0" + str(p_month)
else:
    p_month = str(p_month)
if y_day < 10:
    y_day = "0" + str(y_day)
else:
    y_day = str(y_day)
if p_day < 10:
    p_day = "0" + str(p_day)
else:
    p_day = str(p_day)

api_url = "https://www.alphavantage.co/query"
api_key = "7UHRFPG9HZKUDUH4"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key
}
respond = requests.get(url=api_url, params=parameters)
respond.raise_for_status()
data1 = float(respond.json()['Time Series (Daily)'][y_year + "-" + y_month + "-" + y_day]['4. close'])
data2 = float(respond.json()['Time Series (Daily)'][p_year + "-" + p_month + "-" + p_day]['4. close'])
if data1 > data2:
    per = f"🔺 {round((data1 / data2) * 100 - 100, 2)}%"
else:
    per = f"🔻 {round((data2 / data1) * 100 - 100, 2)}%"

api_url = "https://newsapi.org/v2/everything"
api_key = "0e8b5f7f483c4ce0a6c4ed1cdf8bc586"
parameters = {
    "q": COMPANY_NAME,
    "from": y_year + "-" + y_month + "-" + y_day,
    "to": p_year + "-" + p_month + "-" + p_day,
    "sortBy": "relevancy",
    "apiKey": api_key,
    " language": "en",
    "pageSize": "1"
}
respond = requests.get(url=api_url, params=parameters)
respond.raise_for_status()
art = respond.json()['articles'][0]['title']
body = respond.json()['articles'][0]['description']

account_sid = 'ACa10291481cc8910e1d0a36da040c1832'
auth_token = 'bef78487b96ea4001030fd9730ac10c2'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f'TESLA:{per}\nHeadline:{art}\nBrief:{body}',
    from_='+17179155977',
    to="+201099012514"
)
print(message.status)
