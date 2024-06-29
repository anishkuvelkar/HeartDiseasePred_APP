# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:20:10 2024

@author: Dell
"""

import numpy as np
import pickle
import streamlit as st

#Loading a saved model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

def diabetes_prediction(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease'
  
def main() :
    #Giving a title
    st.title('Heart disease prediction APP')
    diagnosis = ''
    # Collecting inputs from the user
    age = st.number_input("What is your age?", min_value=1, max_value=120, step=1)
    sex = st.selectbox("What is your sex?", options=[("Male", 1), ("Female", 0)])
    cp = st.selectbox("What type of chest pain are you experiencing?", options=[("Typical angina", 0), ("Atypical angina", 1), ("Non-anginal pain", 2), ("Asymptomatic", 3)])
    trestbps = st.number_input("What is your resting blood pressure (in mm Hg)?", min_value=80, max_value=200, step=1)
    chol = st.number_input("What is your serum cholesterol level (in mg/dL)?", min_value=100, max_value=600, step=1)
    fbs = st.selectbox("Is your fasting blood sugar level greater than 120 mg/dL?", options=[("True", 1), ("False", 0)])
    restecg = st.selectbox("What are your resting electrocardiographic results?", options=[("Normal", 0), ("Having ST-T wave abnormality", 1), ("Showing probable or definite left ventricular hypertrophy by Estes' criteria", 2)])
    thalach = st.number_input("What is your maximum heart rate achieved?", min_value=60, max_value=220, step=1)
    exang = st.selectbox("Do you experience exercise-induced angina?", options=[("Yes", 1), ("No", 0)])
    oldpeak = st.number_input("What is the value of ST depression induced by exercise relative to rest?", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("What is the slope of the peak exercise ST segment?", options=[("Upsloping", 0), ("Flat", 1), ("Downsloping", 2)])
    ca = st.selectbox("How many major vessels (0-3) are colored by fluoroscopy?", options=[0, 1, 2, 3,4])
    thal = st.selectbox("What is your thalassemia status?", options=[("Normal", 1), ("Fixed defect", 2), ("Reversible defect", 3)])

    # Button to submit the form
    if st.button('Heart disease results'):
        # Displaying the inputs for confirmation
        st.write(f"Age: {age}")
        st.write(f"Sex: {sex[0]}")
        st.write(f"Chest Pain Type: {cp[0]}")
        st.write(f"Resting Blood Pressure: {trestbps} mm Hg")
        st.write(f"Serum Cholesterol Level: {chol} mg/dL")
        st.write(f"Fasting Blood Sugar > 120 mg/dL: {fbs[0]}")
        st.write(f"Resting Electrocardiographic Results: {restecg[0]}")
        st.write(f"Maximum Heart Rate Achieved: {thalach}")
        st.write(f"Exercise Induced Angina: {exang[0]}")
        st.write(f"ST Depression Induced by Exercise Relative to Rest: {oldpeak}")
        st.write(f"Slope of the Peak Exercise ST Segment: {slope[0]}")
        st.write(f"Number of Major Vessels Colored by Fluoroscopy: {ca}")
        st.write(f"Thalassemia: {thal[0]}")
        st.success("Your inputs have been successfully recorded!")
        diagnosis = diabetes_prediction([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        st.success(diagnosis)
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    