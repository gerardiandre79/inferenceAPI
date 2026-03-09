from fastapi import FastAPI
from app.schema import PredictionRequest
from app.model import predict

app = FastAPI(title="ML Inference API")

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def prediction(data: PredictionRequest):

    result = predict(data.text)

    return {
        "text": data.text,
        "prediction": result
    }