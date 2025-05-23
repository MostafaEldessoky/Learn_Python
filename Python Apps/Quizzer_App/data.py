import requests

par = {
    'amount': 10,
    "category": 18,
    "type": "boolean",
}

res = requests.get(url="https://opentdb.com/api.php", params=par)
res.raise_for_status()
question_data = res.json().get("results")

