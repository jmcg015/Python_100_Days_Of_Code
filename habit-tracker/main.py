import requests
from datetime import datetime

USERNAME = "USERNAME"
TOKEN = "TOKEN"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# date_to_change = datetime(year=2021, month=10, day=19)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

date_change_data = {
    "quantity": "3.5",
}

# response = requests.put(url=update_pixel_endpoint, json=date_change_data, headers=headers)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
