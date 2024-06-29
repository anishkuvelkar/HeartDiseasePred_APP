import numpy as np
import pickle
import streamlit as st

# Loading a saved model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

def diabetes_prediction(input_data):
    try:
        # Change the input data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # Perform prediction using loaded model
        prediction = loaded_model.predict(input_data_reshaped)

        if prediction[0] == 0:
            return 'The Person does not have a Heart Disease'
        else:
            return 'The Person has Heart Disease'

    except Exception as e:
        print(f"Error occurred during prediction: {e}")

def main():
    # Giving a title
    st.title('Heart disease prediction APP')

    # Collecting inputs from the user
    age = st.number_input("What is your age?", min_value=1, max_value=120, step=1)
    sex = st.selectbox("What is your sex?", options=["Male", "Female"])
    cp = st.selectbox("What type of chest pain are you experiencing?", options=["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
    trestbps = st.number_input("What is your resting blood pressure (in mm Hg)?", min_value=80, max_value=200, step=1)
    chol = st.number_input("What is your serum cholesterol level (in mg/dL)?", min_value=100, max_value=600, step=1)
    fbs = st.selectbox("Is your fasting blood sugar level greater than 120 mg/dL?", options=["True", "False"])
    restecg = st.selectbox("What are your resting electrocardiographic results?", options=["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy by Estes' criteria"])
    thalach = st.number_input("What is your maximum heart rate achieved?", min_value=60, max_value=220, step=1)
    exang = st.selectbox("Do you experience exercise-induced angina?", options=["Yes", "No"])
    oldpeak = st.number_input("What is the value of ST depression induced by exercise relative to rest?", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("What is the slope of the peak exercise ST segment?", options=["Upsloping", "Flat", "Downsloping"])
    ca = st.selectbox("How many major vessels (0-4) are colored by fluoroscopy?", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("What is your thalassemia status?", options=["Normal", "Fixed defect", "Reversible defect"])

    # Button to submit the form
    if st.button('Heart disease results'):
        # Displaying the inputs for confirmation
        st.write(f"Age: {age}")
        st.write(f"Sex: {sex}")
        st.write(f"Chest Pain Type: {cp}")
        st.write(f"Resting Blood Pressure: {trestbps} mm Hg")
        st.write(f"Serum Cholesterol Level: {chol} mg/dL")
        st.write(f"Fasting Blood Sugar > 120 mg/dL: {fbs}")
        st.write(f"Resting Electrocardiographic Results: {restecg}")
        st.write(f"Maximum Heart Rate Achieved: {thalach}")
        st.write(f"Exercise Induced Angina: {exang}")
        st.write(f"ST Depression Induced by Exercise Relative to Rest: {oldpeak}")
        st.write(f"Slope of the Peak Exercise ST Segment: {slope}")
        st.write(f"Number of Major Vessels Colored by Fluoroscopy: {ca}")
        st.write(f"Thalassemia: {thal}")
        
        # Calling the prediction function
        input_data = [age, 1 if sex == "Male" else 0, ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"].index(cp), trestbps, chol, 1 if fbs == "True" else 0, ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy by Estes' criteria"].index(restecg), thalach, 1 if exang == "Yes" else 0, oldpeak, ["Upsloping", "Flat", "Downsloping"].index(slope), ca, ["Normal", "Fixed defect", "Reversible defect"].index(thal)]
        diagnosis = diabetes_prediction(input_data)
        st.success(diagnosis)

if __name__ == "__main__":
    main()
