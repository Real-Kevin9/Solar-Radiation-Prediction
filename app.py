import streamlit as st

st.set_page_config(page_title="Solar Radiation Predictor", layout="wide")

st.title("Solar Radiation Prediction App")
st.markdown("""
### About This App
This application predicts **solar radiation** based on various weather conditions using a trained **machine learning model**.
It is built using **Streamlit** and supports:
- **Data Visualizations**
- **Solar Radiation Prediction**

### Dataset
The dataset used in this app is from **SolarPrediction.csv**. It contains historical weather data, including:
- Temperature (°C)
- Pressure (hPa)
- Humidity (%)
- Wind Speed (m/s)
- Date & Time (converted to numeric features)
- Solar Radiation (Target Variable)

**Explore the Visualizations or Predict Solar Radiation using the sidebar!**
""")
