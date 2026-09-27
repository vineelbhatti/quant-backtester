# backtests/management/commands/run_backtest.py
from django.core.management.base import BaseCommand
from src.config import TICKER, START_DATE, END_DATE, MA_WINDOW, ENTRY_THRESHOLD, EXIT_THRESHOLD
from src.data.fetch import get_price_data
from src.strategy.mean_reversion import add_signal
from src.backtest.engine import run_backtest
from src.backtest.metrics import calculate_metrics
from backtests.models import BacktestResult

class Command(BaseCommand):
    help = "Runs the mean-reversion backtest and saves the result to the database."

    def handle(self, *args, **options):
        data = get_price_data(TICKER, START_DATE, END_DATE)
        data = add_signal(data, MA_WINDOW)
        trades = run_backtest(data, ENTRY_THRESHOLD, EXIT_THRESHOLD)
        summary = calculate_metrics(trades)

        result = BacktestResult.objects.create(
            ticker=TICKER,
            start_date=START_DATE,
            end_date=END_DATE,
            ma_window=MA_WINDOW,
            entry_threshold=ENTRY_THRESHOLD,
            exit_threshold=EXIT_THRESHOLD,
            num_trades=summary.num_trades,
            total_return=summary.total_return,
            average_return=summary.average_return,
            sharpe_ratio=summary.sharpe_ratio,
            max_drawdown=summary.max_drawdown,
        )

        self.stdout.write(self.style.SUCCESS(f"Saved backtest result: {result}"))