export interface BacktestResult {
  id: number;
  ticker: string;
  start_date: string;
  end_date: string;
  ma_window: number;
  entry_threshold: number;
  exit_threshold: number;
  num_trades: number;
  total_return: number;
  average_return: number;
  sharpe_ratio: number;
  max_drawdown: number;
  created_at: string;
}