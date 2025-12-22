import requests
from pandas.io.excel import register_writer

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sandeep13"
TOKEN = "my_secret_token_543"


#Using post request create a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)


#using post request t create a graph
GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",          # must be unique
    "name": "Coding Hours",
    "unit": "hours",
    "type": "float",         # "int" or "float"
    "color": "shibafu"       # graph color
}

# response = requests.post(
#     url=GRAPH_ENDPOINT,
#     json=graph_config,
#     headers=headers
# )
#
# print(response.text)
GRAPH_ID = "graph1"
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date":"20251224",
    "quantity": "9.74",
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, json = pixel_data, headers=headers)
print(response.text)