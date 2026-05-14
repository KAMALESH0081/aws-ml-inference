from fastapi import FastAPI
from pydantic import BaseModel
import boto3
import joblib
import os

app = FastAPI()

MODEL_PATH = "model/linear_regression.pkl"

BUCKET_NAME="my-first-bucket-ai-2004"

# Download model from S3 only once
if not os.path.exists(MODEL_PATH):

    s3 = boto3.client("s3")

    os.makedirs("model", exist_ok=True)

    s3.download_file(
        BUCKET_NAME,
        MODEL_PATH,
        MODEL_PATH
    )

model = joblib.load(MODEL_PATH)

class InputData(BaseModel):
    number: float

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/predict")
def predict(data: InputData):

    prediction = model.predict([[data.number]])

    return {
        "prediction": float(prediction[0])
    }