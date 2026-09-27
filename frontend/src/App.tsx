import { useState, useEffect } from "react";
import type { BacktestResult } from "./types";

function App() {
  const [results, setResults] = useState<BacktestResult[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/backtests/results/")
      .then((response) => response.json())
      .then((data) => setResults(data))
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Backtest Results</h1>
      <ul>
        {results.map((result) => (
          <li key={result.id}>
            {result.ticker} — Sharpe: {result.sharpe_ratio.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;