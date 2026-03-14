import streamlit as st
import pandas as pd

from quantlib.data_engine import load_data
from quantlib.risk_engine import calculate_var

st.title("Risk Model")

data_path = load_data()

df = pd.read_csv(data_path)

var = calculate_var(df)

st.write("Value at Risk:", var)