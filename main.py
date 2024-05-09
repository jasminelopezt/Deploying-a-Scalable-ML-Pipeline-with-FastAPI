import os
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
import logging
import sys

from ml.data import apply_label, process_data
from ml.model import inference, load_model

# DO NOT MODIFY
class Data(BaseModel):
    age: int = Field(..., example=37)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=178356)
    education: str = Field(..., example="HS-grad")
    education_num: int = Field(..., example=10, alias="education-num")
    marital_status: str = Field(
        ..., example="Married-civ-spouse", alias="marital-status"
    )
    occupation: str = Field(..., example="Prof-specialty")
    relationship: str = Field(..., example="Husband")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States", alias="native-country")

# path_encoder = "model/encoder.pkl" # TODO: enter the path for the saved encoder 
# encoder = load_model(path_encoder)

model_path = 'model/model.pkl'

with open(model_path, 'rb') as f:
    model = pickle.load(f)

encoder_path = 'model/encoder.pkl'

with open(encoder_path, 'rb') as f:
    encoder = pickle.load(f)

# TODO: create a RESTful API using FastAPI
app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
logger.info('API is starting up!!!!!!!!')

# TODO: create a GET on the root giving a welcome message
@app.get("/")
async def get_root():
    """ Say hello!"""
    return {"message": "Welcome to the API!"}

# TODO: create a POST on a different path that does model inference
@app.post("/data/")
async def post_inference(data: Data):
    # DO NOT MODIFY: turn the Pydantic model into a dict.
    logger.info(data)
    data_dict = data.dict()
    logger.info("1")
    # DO NOT MODIFY: clean up the dict to turn it into a Pandas DataFrame.
    # The data has names with hyphens and Python does not allow those as variable names.
    # Here it uses the functionality of FastAPI/Pydantic/etc to deal with this.
    data = {k.replace("_", "-"): [v] for k, v in data_dict.items()}
    data = pd.DataFrame.from_dict(data)
    logger.info("2")
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    logger.info("3")
    data_processed, _, _, _ = process_data(
        data, categorical_features=cat_features,training=False, encoder=encoder
    )
    logger.info("4")
    _inference = inference(model, data_processed)
    logger.info("5")
    return {"result": apply_label(_inference)}
