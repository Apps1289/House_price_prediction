import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
from pathlib import Path

# Load the trained model and preprocessor
BASE_DIR = Path(__file__).resolve().parent.parent

model = tf.keras.models.load_model(
    BASE_DIR / "models" / "heart_disease_model.keras"
)

preprocessor = joblib.load(
    BASE_DIR / "models" / "preprocessor.pkl"
)


def predict_heart_disease(data:dict):
    # Convert input data to a numpy array
    input_data = pd.DataFrame([data])
    
    # Preprocess the input data
    preprocessed_data = preprocessor.transform(input_data)
    
    # Make predictions using the trained model
    probabilities = model.predict(preprocessed_data)[0][0]
    predictions = (probabilities > 0.5).astype(int)
    
    return predictions, float(probabilities)
    