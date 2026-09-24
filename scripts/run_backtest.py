from src.config import TICKER, START_DATE, END_DATE, MA_WINDOW, ENTRY_THRESHOLD, EXIT_THRESHOLD
from src.data.fetch import get_price_data
from src.strategy.mean_reversion import add_signal
from src.backtest.engine import run_backtest
from src.backtest.metrics import calculate_metrics

def main():
    data = get_price_data(TICKER, START_DATE, END_DATE)
    data = add_signal(data, MA_WINDOW)
    trades = run_backtest(data, ENTRY_THRESHOLD, EXIT_THRESHOLD)
    summary = calculate_metrics(trades)

    print(f"Ticker: {TICKER}")
    print(f"Period: {START_DATE} to {END_DATE}")
    print(f"Number of trades: {summary.num_trades}")
    print(f"Average return per trade: {summary.average_return:.2%}")
    print(f"Total return: {summary.total_return:.2%}")
    print(f"Sharpe ratio: {summary.sharpe_ratio:.2f}")
    print(f"Max drawdown: {summary.max_drawdown:.2%}")

if __name__ == "__main__":
    main()