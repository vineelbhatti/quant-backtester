import pytest
from src.backtest.trade import Trade
from src.backtest.metrics import calculate_metrics

def make_trade(pnl_pct):
    entry = 100.0
    exit_ = entry * (1+pnl_pct)
    return Trade(entry_date="2024-01-01", entry_price=entry, exit_date="2024-01-02", exit_price=exit_)

def test_calculate_metrics_basic_scenario():
    trades =[make_trade(0.10), make_trade(-0.10)]
    summary = calculate_metrics(trades)

    assert summary.num_trades == 2
    assert summary.average_return == pytest.approx(0.0)
    assert summary.sharpe_ratio == pytest.approx(0.0)
    assert summary.max_drawdown == pytest.approx(-0.10, abs=1e-4)
    assert summary.total_return == pytest.approx(-0.01, abs=1e-4)

def test_calculate_metrics_empty_trades():
    summary = calculate_metrics([])
    assert summary.num_trades == 0
    assert summary.sharpe_ratio == 0.0