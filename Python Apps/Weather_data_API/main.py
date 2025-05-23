import requests
from twilio.rest import Client

# weather API
api_key = "ef2f96a769738c13e41eee88e6a3db8e"
api_url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "lat": 26.820553,
    "lon": 30.802498,
    "appid": api_key,
}
rep = requests.get(url=api_url, params=parameters)
rep.raise_for_status()
data = rep.json()["weather"][0]["main"]

# SMS generator with twilio
account_sid = 'ACa10291481cc8910e1d0a36da040c1832'
auth_token = 'bef78487b96ea4001030fd9730ac10c2'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
         body=f'Hello mostafa this is my first API App send from my server sky is now {data} on egypt',
         from_='+17179155977',
         to="+20 109 901 2514"
     )
print(message.status)






























