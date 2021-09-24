import json
import requests

# URL = "http://127.0.0.1:8000/api/list/1"

# r = requests.get(url=URL)

# print(r)

# data = r.json()

# print(data)


URL = "http://127.0.0.1:8000/api/create"

data = {
    'name':'Satyam',
    'roll':20,
    'city':'Shidhpur'
}
json_data = json.dumps(data)


r = requests.post(url=URL, data=json_data)


print(r)

data = r.json()

print(data)



