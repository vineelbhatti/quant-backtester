import pandas as pd
from src.backtest.trade import Trade

def run_backtest(data, entry_threshold, exit_threshold):
    holding = False
    entry_price = 0.0
    entry_date = None
    trades = []

    for date, row in data.iterrows():
        pct_from_ma = row["PctFromMA"]
        if pd.isna(pct_from_ma):
            continue

        if not holding and pct_from_ma < entry_threshold:
            holding = True
            entry_price = row["Close"]
            entry_date = date
        elif holding and pct_from_ma >= exit_threshold:
            trades.append(Trade(
                entry_date=str(entry_date),
                entry_price=entry_price,
                exit_date=str(date),
                exit_price=row["Close"],
            ))
            holding = False
    return trades
