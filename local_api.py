import json
import requests
from ml.data import process_data  

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000")

# TODO: print the status code
print("GET Status Code:", r.status_code)
# TODO: print the welcome message
print("GET Response:", r.json()["message"])


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

data_processed, _, _, _ = process_data([data], training=False)

# TODO: send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# TODO: print the status code
print("\nPOST Status Code:", r.status_code)
# TODO: print the result
print("POST Result:", r.json()["result"])

