import os
import gdown
import pandas as pd
import streamlit as st

FILE_ID = "1H8btGV5afUQirVrnqTS3RgPSZudxyL6n"
DATA_PATH = "data/amibroker_all_data.txt"


@st.cache_data
def load_data():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_PATH):

        url = f"https://drive.google.com/uc?id={FILE_ID}"

        gdown.download(url, DATA_PATH, quiet=False)

    df = pd.read_csv(
        DATA_PATH,
        sep=",",
        header=None
    )

    df.columns = [
        "ticker",
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    df["date"] = pd.to_datetime(df["date"])

    return df