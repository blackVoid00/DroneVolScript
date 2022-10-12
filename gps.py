import requests
import json
playload = {"email": "hello@gmail.com", "password": "Hello"}
url = "https://soraeir.herokuapp.com/login"
r = requests.post(url, json=playload)
# print(r.json())
data = r.json()
# print(data["token"])
headers = {"x-access-token": data["token"]}
url2 = "https://soraeir.herokuapp.com/api/gpsdata"
r2 = requests.get(url2, headers=headers)
data2 = r2.json()
print(data2[0]['longitude'])
