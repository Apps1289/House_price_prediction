import streamlit as st
import requests

#API endpoint URL
API_URL = "http://127.0.0.1:8000/predict"

# set the page title and favicon
st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon=":guardsman:", layout="wide"
    )

st.title("Heart Disease Prediction App")
st.write(
    "This app predicts the likelihood of heart disease based on user input. Please fill in the required information below and click the 'Predict' button to see the results."
)

with st.form(key="heart_disease_form"):
    st.subheader("Patient Information")
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox(
        "Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    resting_blood_pressure = st.number_input(
        "Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    cholesterol = st.number_input(
        "Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    
    fasting_blood_sugar = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
    
    resting_ecg = st.selectbox(
        "Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    
    maximum_heart_rate = st.number_input(
        "Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    
    exercise_angina = st.selectbox(
        "Exercise Induced Angina", ["Yes", "No"])
    
    ST_depression = st.number_input(
        "ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    
    st_slope = st.selectbox(
        "Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    
    major_vessels_count = st.number_input(
        "Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
    
    thalassemia = st.selectbox(
        "Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])
    
    submit_button = st.form_submit_button(label="Predict")
    
if submit_button:
    # Prepare the input data for the API request
    input_data = {
        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_blood_pressure": resting_blood_pressure,
        "cholesterol": cholesterol,
        "fasting_blood_sugar": fasting_blood_sugar,
        "resting_ecg": resting_ecg,
        "maximum_heart_rate": maximum_heart_rate,
        "exercise_angina": exercise_angina,
        "ST_depression": ST_depression,
        "st_slope": st_slope,
        "major_vessels_count": major_vessels_count,
        "thalassemia": thalassemia
    }
    
    # Send a POST request to the FastAPI endpoint
    try:
         response = requests.post(
        API_URL, json=input_data
        )
         
         if response.status_code == 200:
             prediction_result = response.json()
             
             prediction = prediction_result.get("prediction")
             probability = prediction_result.get("probabilities")
             
             if prediction == 1:
                 st.error(
                     f"higher risk of heart disease"
                 )
             else:
                 st.success(
                     f"lower risk of heart disease"
                 )
                 
             st.write(f"Probability of heart disease: {probability:.2f}")
         else:
                st.error(
                    f"Error: Received status code {response.status_code} from the API."
                )  
                st.json(response.json())
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
        st.stop()
    
    