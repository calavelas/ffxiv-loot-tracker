import requests
import json

url = "http://127.0.0.1:8000/check/?staticName=Connection%20Issues&itemName=Edenmorn%20Head%20Gear%20Coffer"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

response_json = json.loads(response.text)
print(response_json['lootHistory'][3]['takenBy'])
