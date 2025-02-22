import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="Visualizations", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("SolarPrediction.csv")  

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_columns = st.sidebar.multiselect("Select Features", df.columns.tolist(), default=df.columns.tolist())

# Title
st.title("Solar Radiation Data Visualizations")

# 1️ Display Dataset (Filtered)
st.subheader("Dataset Preview")
st.dataframe(df[selected_columns].head())

# 2️ Distribution Plots
st.subheader("Feature Distributions")
selected_feature = st.selectbox("Select a feature for distribution plot", df.columns.tolist())
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df[selected_feature], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# 3️ Scatter Plot
st.subheader("Scatter Plot")
x_feature = st.selectbox("Select X-axis feature", df.columns.tolist(), index=0)
y_feature = st.selectbox("Select Y-axis feature", df.columns.tolist(), index=1)

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=df[x_feature], y=df[y_feature], alpha=0.6)
st.pyplot(fig)

# 4️ Correlation Heatmap
st.subheader("Correlation Heatmap")

# Convert DateTime column (if any) and drop non-numeric columns
df_numeric = df.select_dtypes(include=['number'])  # Keep only numeric columns

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_numeric.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
st.pyplot(fig)

# 5 Box Plot for Outlier Detection
st.subheader("Box Plot")
box_feature = st.selectbox("Select feature for box plot", df.columns.tolist(), index=0)
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(y=df[box_feature])
st.pyplot(fig)

