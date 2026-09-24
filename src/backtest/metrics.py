from dataclasses import dataclass
import numpy as np
from src.backtest.trade import Trade

@dataclass
class PerformanceSummary:
    num_trades: int
    total_return: float
    average_return: float
    sharpe_ratio: float
    max_drawdown: float

def calculate_metrics(trades):
    if not trades:
        return PerformanceSummary(
            num_trades=0, total_return=0.0, average_return=0.0,
            sharpe_ratio=0.0, max_drawdown=0.0,
        )

    returns = np.array([t.pnl for t in trades])

    average_return = returns.mean()
    std_return = returns.std()
    sharpe_ratio = average_return / std_return if std_return != 0 else 0.0

    cumulative = np.cumprod(1+returns)
    running_max = np.maximum.accumulate(cumulative)
    drawdowns = (cumulative - running_max) / running_max
    max_drawdown = drawdowns.min()

    return PerformanceSummary(
        num_trades=len(trades),
        total_return=cumulative[-1] - 1,
        average_return=average_return,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown,
    )