import gdown
import os

def load_data():

    os.makedirs("data", exist_ok=True)

    file_path = "data/stock_data.txt"

    if not os.path.exists(file_path):

        url = "https://drive.google.com/uc?id=1H8btGV5afUQirVrnqTS3RgPSZudxyL6n"

        gdown.download(url, file_path, quiet=False)

    return file_path