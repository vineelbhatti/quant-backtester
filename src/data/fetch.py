import yfinance as yf
import pandas as pd

def get_price_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    if data.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    return data