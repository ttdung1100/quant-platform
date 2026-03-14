import streamlit as st
import pandas as pd

from quantlib.data_engine import load_data

st.title("Stock Analysis")

data_path = load_data()

df = pd.read_csv(data_path)

st.write(df.head())