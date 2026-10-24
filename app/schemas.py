from pydantic import BaseModel, Field
from typing import Annotated, Literal
from app.mapping import (
    MLsex, MLchest_pain_type, MLfasting_blood_sugar,
    MLresting_ecg, MLexercise_angina, MLst_slope, MLthalassemia
    )

class HeartDiseaseInput(BaseModel):
    age : int
    sex: MLsex
    chest_pain_type: MLchest_pain_type
    resting_blood_pressure: int 
    cholesterol: int
    fasting_blood_sugar: MLfasting_blood_sugar
    resting_ecg: MLresting_ecg 
    maximum_heart_rate: int
    exercise_angina: MLexercise_angina
    ST_depression: float
    st_slope: MLst_slope 
    major_vessels_count: int 
    thalassemia: MLthalassemia 
    
    