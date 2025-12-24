import requests
from pandas.io.excel import register_writer
import datetime


#URL : https://pixe.la/v1/users/sandeep13/graphs/graph1.html?v=2

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

today = datetime.datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date":today,
    "quantity": "117.74",
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json = pixel_data, headers=headers)


#Update operation in pixela
GRAPH_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
print(GRAPH_UPDATE_ENDPOINT)

update_graph_config = {
    "name": "Daily Study Tracker",
    "unit": "hours"
}

# response = requests.put(
#     url=GRAPH_UPDATE_ENDPOINT,
#     json=update_graph_config,
#     headers=headers
# )


#Function to add daily study hours
def add_working_hours(quantity):
    today = datetime.datetime.now().strftime("%Y%m%d")

    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

    pixel_data = {
        "quantity": str(quantity)
    }

    response = requests.put(
        url=update_endpoint,
        json=pixel_data,
        headers=headers
    )

    print(response.text)

add_working_hours(190)