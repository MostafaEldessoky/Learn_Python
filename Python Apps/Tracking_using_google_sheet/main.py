import requests
from datetime import datetime

api_id = "c12d8b65"
api_key = "2a7f626ef871039142d98ebbcffc9e9f"
api_url1 = "https://trackapi.nutritionix.com/v2/natural/exercise"
data1 = {
    "query": input("what you did today? "),
    "gender": "man",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 27
}

header = {
    "x-app-id": api_id,
    "x-app-key": api_key,
}

respond = requests.post(url=api_url1, json=data1, headers=header)
info = respond.json()

ex = info['exercises'][0]['user_input']
dur = info['exercises'][0]['duration_min']
cal = info['exercises'][0]['nf_calories']

now = datetime.today()

api_url2 = "https://api.sheety.co/18136cad05ce3e603c84d483d0e75dbc/workoutsTrackerProject/workouts"
data2 = {
    "workout": {
        "date": f"{now.strftime('%d/%m/%Y')}",
        "time": f"{now.strftime('%X')}",
        "exercise": ex.title(),
        "duration": dur,
        "calories": cal,
    }
}

header = {
    "Authorization": "Basic bW91c3RhZmE6bW9zdGFmYUAxOTk1",
}

respond = requests.post(url=api_url2, json=data2, headers=header)
print(respond.text)
