import streamlit as st
import numpy as np
import joblib

st.title("Body Type Predictor")

model_choice = st.selectbox("Select Model", ["Baseline Model", "Fine-tuned Model"])
model_path = "base.pkl" if model_choice == "Baseline Model" else "fine.pkl"

model, scaler, le = joblib.load(model_path)

density = st.number_input("Density", value=1.0, step=0.01)
age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight", value=70.0, step=0.1)
height = st.number_input("Height", value=170.0, step=0.1)
neck = st.number_input("Neck", value=40.0, step=0.1)
chest = st.number_input("Chest", value=90.0, step=0.1)
abdomen = st.number_input("Abdomen", value=85.0, step=0.1)
hip = st.number_input("Hip", value=95.0, step=0.1)
thigh = st.number_input("Thigh", value=55.0, step=0.1)
knee = st.number_input("Knee", value=35.0, step=0.1)
ankle = st.number_input("Ankle", value=22.0, step=0.1)
biceps = st.number_input("Biceps", value=30.0, step=0.1)
forearm = st.number_input("Forearm", value=28.0, step=0.1)
wrist = st.number_input("Wrist", value=18.0, step=0.1)

if st.button("Predict Category"):
    features = np.array(
        [
            [
                density,
                age,
                weight,
                height,
                neck,
                chest,
                abdomen,
                hip,
                thigh,
                knee,
                ankle,
                biceps,
                forearm,
                wrist,
            ]
        ]
    )
    features_scaled = scaler.transform(features)
    pred_encoded = model.predict(features_scaled)
    pred = le.inverse_transform(pred_encoded)
    st.write(f"Predicted Category: {pred[0]}")
