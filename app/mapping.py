#mapping the categorical values to numerical values for the model
from pydantic import BeforeValidator
from typing import Annotated

sex_mapping = {"male": 1, "female": 0}
chest_pain_mapping = {"typical angina": 0, "atypical angina": 1, "non-anginal pain": 2, "asymptomatic": 3}
fasting_blood_sugar_mapping = {"true": 1, "false": 0}
resting_ecg_mapping = {"normal": 0, "st-t wave abnormality": 1, "left ventricular hypertrophy": 2}
exercise_angina_mapping = {"yes": 1, "no": 0}
st_slope_mapping = {"upsloping": 0, "flat": 1, "downsloping": 2}

thalassemia_mapping = {"normal": 1, "fixed defect": 2, "reversible defect": 3}

def ml_mapping(mapping: dict[str,int]):
    
    def validator(value: str) -> int:
        
        val_str = str(value).lower().strip()
        if val_str not in mapping:
            raise ValueError(f"Invalid value '{value}'. Expected one of: {list(mapping.keys())}")
        return mapping[val_str]
    
    return Annotated[int, BeforeValidator(validator)]


MLsex = ml_mapping(sex_mapping)
MLchest_pain_type = ml_mapping(chest_pain_mapping)
MLfasting_blood_sugar = ml_mapping(fasting_blood_sugar_mapping)
MLresting_ecg = ml_mapping(resting_ecg_mapping)
MLexercise_angina = ml_mapping(exercise_angina_mapping)
MLst_slope = ml_mapping(st_slope_mapping)
MLthalassemia = ml_mapping(thalassemia_mapping)
