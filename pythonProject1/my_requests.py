import requests

url = "http://127.0.0.1:5000/api/users"

data = {"name": "Claudiu"}

response = requests.post(url, json=data)

if response.status_code == 200 or response.status_code == 201:
    data = response.json()
    print(data)
else:
    print(f"Eroare: {response.status_code}")