# import json

# import requests

# # TODO: send a GET using the URL http://127.0.0.1:8000
# r = requests.get("http://127.0.0.1:8000")

# # TODO: print the status code
# print("GET Status Code:", r.status_code)
# # TODO: print the welcome message
# print("GET Response:", r.json()["message"])



# data = {
#     "age": 37,
#     "workclass": "Private",
#     "fnlgt": 178356,
#     "education": "HS-grad",
#     "education-num": 10,
#     "marital-status": "Married-civ-spouse",
#     "occupation": "Prof-specialty",
#     "relationship": "Husband",
#     "race": "White",
#     "sex": "Male",
#     "capital-gain": 0,
#     "capital-loss": 0,
#     "hours-per-week": 40,
#     "native-country": "United-States",
# }

# # TODO: send a POST using the data above
# r = requests.post("http://127.0.0.1:8000/data/", json=data)

# # TODO: print the status code
# print("\nPOST Status Code:", r.status_code)
# # TODO: print the result
# print("POST Result:", r.json()["result"])

import json
import requests

try:
    r_get = requests.get("http://127.0.0.1:8000")
    r_get.raise_for_status()  # Raise an exception for HTTP errors
    print("GET Status Code:", r_get.status_code)
    print("GET Response:", r_get.json().get("message", "No message found"))
except requests.exceptions.RequestException as e:
    print("GET Request failed:", e)

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

try:
    r_post = requests.post("http://127.0.0.1:8000/data/", json=data)
    r_post.raise_for_status()  # Raise an exception for HTTP errors
    print("\nPOST Status Code:", r_post.status_code)
    print("POST Result:", r_post.json().get("result", "No result found"))
except requests.exceptions.RequestException as e:
    print("POST Request failed:", e)
