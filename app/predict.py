import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../models/fraud_model.pkl")

scaler_path = os.path.join(BASE_DIR, "../models/scaler.pkl")

model = joblib.load(model_path)

scaler = joblib.load(scaler_path)


def predict_transaction(data):

    data = np.array(data).reshape(1, -1)

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0][1]

    return prediction, probability