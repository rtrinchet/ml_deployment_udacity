from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import uvicorn
import pickle
from solution.train_model import process_data
from mangum import Mangum


with open("model.pkl", "rb") as input_file:
    model = pickle.load(input_file)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

app = FastAPI()
handler = Mangum(app)

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


# Define a Pydantic model for the request body
class InputData(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: str = Field(alias="native-country")


@app.get("/")
async def welcome():
    return {"message": "Welcome to the API!"}


@app.post("/predict/")
async def make_prediction(input_data: InputData):
    data = input_data.dict(by_alias=True)
    data = pd.DataFrame(data, index=[1])
    X, _, _, _ = process_data(
        X=data, training=False, encoder=encoder, categorical_features=cat_features
    )
    prediction = model.predict(X)
    response_object = {"prediction": prediction[0].item()}

    return response_object


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
