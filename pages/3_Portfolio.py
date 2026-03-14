import streamlit as st
import pandas as pd

from quantlib.data_engine import load_data
from quantlib.portfolio_optimizer import optimize_portfolio

st.title("Portfolio Optimization")

data_path = load_data()

df = pd.read_csv(data_path)

weights = optimize_portfolio(df)

st.write(weights)