import streamlit as st
import pickle
import numpy as np

st.title("SEEP Mela Participant Predictor")

# Select model
model_choice = st.selectbox("Select Model", ["Baseline Model", "Fine-tuned Model"])

# Load selected model
model_path = "base_model.pkl" if model_choice == "Baseline Model" else "ok.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Inputs
course_encoded = st.number_input("Course (encoded)", min_value=0, max_value=5, step=1)
sessions = st.number_input("Sessions Conducted", min_value=1, max_value=10, step=1)
year = st.number_input("Year", min_value=2083, max_value=2090, step=1)
# Predict
if st.button("Predict Participants"):
    features = np.array([[year, course_encoded, sessions]])
    prediction = model.predict(features)
    st.write(f"Predicted Participants: {int(prediction[0])}")
