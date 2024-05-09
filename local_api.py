import json
import requests
import pandas as pd
from ml.data import process_data, apply_label
import pickle

with open("model/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


# TODO: send a GET using the URL http://127.0.0.1:8000
r_get = requests.get("http://127.0.0.1:8000")

# TODO: print the status code
print("GET Status Code:", r_get.status_code)
# TODO: print the welcome message
if r_get.status_code == 200:
    print("GET Response:", r_get.json()["message"])


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

data_df = pd.DataFrame([data])

data_processed, _, _, _ = process_data(data_df, training=False, encoder=encoder)

r_post = requests.post("http://127.0.0.1:8000/data/", json=data)
print("\nPOST Status Code:", r_post.status_code)
if r_post.status_code == 200:
    print("POST Result:", r_post.json()["result"])