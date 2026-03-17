import json
import requests

query = "https://api.chucknorris.io/jokes/random"
try:
    answer = requests.get(query)
    if answer.status_code == 200:
        answer = answer.json()
        print(answer["value"])
except requests.exceptions.RequestException as e:
    print("Request was not possible")
