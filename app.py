import streamlit as st
import os
import pandas as pd

# Agar dataset.csv file nahi hai, toh run.py ko chalao
if not os.path.exists("dataset.csv"):
    st.write("Generating dataset.csv from run.py...")
    os.system("python run.py")

# Fir dataset.csv file ko load karo
if os.path.exists("dataset.csv"):
    df = pd.read_csv("dataset.csv")
    st.title("English to Hindi Dataset Viewer")
    st.dataframe(df.head())
else:
    st.error("dataset.csv not found and could not be generated.")
