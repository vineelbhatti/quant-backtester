import pandas as pd
from src.backtest.engine import run_backtest

def test_run_backtest_executes_one_trade():
    data = pd.DataFrame({
        "Close":      [100, 95, 96, 99, 102],
        "PctFromMA":  [-0.01, -0.08, -0.03, -0.01, 0.02],
    }, index=pd.date_range("2024-01-01", periods=5))

    trades = run_backtest(data, entry_threshold=-0.05, exit_threshold=0.0)

    assert len(trades) == 1
    assert trades[0].entry_price == 95
    assert trades[0].exit_price == 102

def test_run_backtest_no_exit_produces_no_trades():
    data = pd.DataFrame({
        "Close":      [100, 95, 93, 90],
        "PctFromMA":  [-0.01, -0.08, -0.10, -0.12],
    }, index=pd.date_range("2024-01-01", periods=4))

    trades = run_backtest(data, entry_threshold=-0.05, exit_threshold=0.0)

    assert len(trades) == 0