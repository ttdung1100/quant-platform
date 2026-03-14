import streamlit as st
from quantlib.ai_prediction import predict_market

st.title("AI Research")

st.write("AI prediction module")

result = predict_market()

st.write(result)