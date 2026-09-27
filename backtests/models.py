from django.db import models

# Create your models here.
from django.db import models

class BacktestResult(models.Model):
    ticker = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    ma_window = models.IntegerField()
    entry_threshold = models.FloatField()
    exit_threshold = models.FloatField()

    num_trades = models.IntegerField()
    total_return = models.FloatField()
    average_return = models.FloatField()
    sharpe_ratio = models.FloatField()
    max_drawdown = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} ({self.start_date} to {self.end_date}) - Sharpe: {self.sharpe_ratio:.2f}"