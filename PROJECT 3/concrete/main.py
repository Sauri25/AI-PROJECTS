import streamlit as st
import numpy as np
import joblib

st.title("Concrete Compressive Strength Predictor")

# Model selection
model_choice = st.selectbox("Select Model", ["Baseline Model", "Fine-tuned Model"])
model_path = "base.pkl" if model_choice == "Baseline Model" else "fine.pkl"


# Load model
@st.cache_resource
def load_model(path):
    return joblib.load(path)


model = load_model(model_path)

# Input fields
blast_furnace_slag = st.number_input(
    "Blast Furnace Slag (kg/m³)", min_value=0.0, value=100.0
)
fly_ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, value=50.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, value=5.0)
age = st.number_input("Age (days)", min_value=1, value=28)
cement_water_ratio = st.number_input("Cement/Water Ratio", min_value=0.1, value=0.5)
net_aggregate = st.number_input("Net Aggregate (kg/m³)", min_value=0.0, value=1000.0)

# Predict button
if st.button("Predict Strength"):
    input_data = np.array(
        [
            [
                blast_furnace_slag,
                fly_ash,
                superplasticizer,
                age,
                cement_water_ratio,
                net_aggregate,
            ]
        ]
    )

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Strength using **{model_choice}**: **{prediction:.2f} MPa**")
