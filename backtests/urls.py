from django.urls import path
from backtests.views import BacktestResultListView

urlpatterns = [
    path("results/", BacktestResultListView.as_view(), name="backtest-results"),
]