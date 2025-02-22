import streamlit as st
import joblib
import pandas as pd
import numpy as np
import json
import os

# Set page config
st.set_page_config(page_title="Solar Radiation Prediction", layout="wide")

# Load the trained model
model = joblib.load("solar_radiation_model.pkl")

# Load feature names
if os.path.exists("feature_names.json"):
    with open("feature_names.json", "r") as f:
        feature_names = json.load(f)
else:
    feature_names = ["Temperature", "Pressure", "Humidity", "WindSpeed", "Hour", "Day", "Month"]  # Modify based on dataset

# Load scaler if used
scaler = joblib.load("scaler.pkl") if os.path.exists("../scaler.pkl") else None

# Define feature units (Modify based on dataset)
feature_units = {
    "Temperature": "°C",
    "Pressure": "hPa",
    "Humidity": "%",
    "WindSpeed": "m/s",
    "Hour": "(0-23)",
    "Day": "(1-31)",
    "Month": "(1-12)"
}

# Streamlit UI
st.title("Solar Radiation Prediction")
st.markdown("Enter the required details below to predict solar radiation.")

# Create input fields dynamically with units
input_data = []
for feature in feature_names:
    unit = feature_units.get(feature, "")
    value = st.number_input(f"Enter {feature} ({unit})", value=0.0, format="%.2f")
    input_data.append(value)

# Convert input to DataFrame
input_df = pd.DataFrame([input_data], columns=feature_names)

# Apply scaling if needed
if scaler:
    input_df = scaler.transform(input_df)

# Predict button
if st.button("Predict Solar Radiation"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Solar Radiation: {prediction:.2f} W/m²")

