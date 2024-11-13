import pandas as pd
from pandasai import SmartDataframe

def load_csv_data(file):
    return pd.read_csv(file)

def initialize_smart_dataframe(data, model):
    return SmartDataframe(data, config={"llm": model})
