import requests

# url = "http://127.0.0.1:5000/api/users/1"
#
# data = {"name": "Claudiu"}
#
# #response = requests.post(url, json=data)
# response = requests.put(url, json=data)
#
# if response.status_code == 200 or response.status_code == 201:
#     data = response.json()
#     print(data)
# else:
#     print(f"Eroare: {response.status_code}")
#
# response = requests.delete(url)
#
# if response.status_code == 200 or response.status_code == 201:
#     data = response.json()
#     print(data)
# else:
#     print(f"Eroare: {response.status_code}")

url = "http://127.0.0.1:5000/id"

my_param = {"my_id": 1}

response = requests.get(url, params=my_param)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Eroare: {response.status_code}")
