from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from app.predict import predict_transaction

app = FastAPI()


class Transaction(BaseModel):

    features: list


@app.get("/")

def home():

    return {
        "message": "Fraud Detection API Running"
    }


@app.post("/predict")

def predict(transaction: Transaction):

    prediction, probability = predict_transaction(
        transaction.features
    )

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }