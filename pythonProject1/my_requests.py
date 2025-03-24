import requests

url = "http://127.0.0.1:5000/hello"

response = requests.post(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Eroare: {response.status_code}")