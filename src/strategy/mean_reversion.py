import pandas as pd

def add_signal(data, window):
    data = data.copy()
    data["MA"] = data["Close"].rolling(window).mean()
    data["PctFromMA"] = (data["Close"] - data["MA"])/data["MA"]
    return data