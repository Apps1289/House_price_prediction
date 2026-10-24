import fastapi
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from app.schemas import HeartDiseaseInput
from app.predict import predict_heart_disease

app = FastAPI(
    title="Heart Disease Prediction API", 
    version="1.0"
    )

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Heart Disease Prediction API!"
        }
    
@app.get("/health")
def read_health():
    return {
        "status": "healthy"
        }
    
@app.post("/predict")
def predict(data: HeartDiseaseInput):
    
    predictions, probabilities = predict_heart_disease(
        data.model_dump()
    )
    
    return JSONResponse(
        content={
            "predictions": int(predictions),
            "probabilities": float(probabilities)
        }
    )
    