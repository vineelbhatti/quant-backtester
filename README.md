# Quant Backtester

A backtesting engine for evaluating systematic trading strategies, starting with a mean-reversion strategy on daily equity price data.

## Setup

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage

python -m scripts.run_backtest

## Running tests

pytest

## Project structure

- `src/data/` — fetches historical price data
- `src/strategy/` — computes trading signals
- `src/backtest/` — simulates trades and evaluates performance
- `tests/` — unit tests for each module

- ## Running the full stack
1. Start Postgres and create the database (`createdb quant_backtester`)
2. Copy `.env.example` to `.env` and fill in values
3. `python manage.py migrate`
4. `python manage.py run_backtest` (saves a result)
5. `python manage.py runserver`
6. In `frontend/`: `npm install && npm run dev`

## Known limitations
- Sharpe ratio is computed on per-trade returns, not annualized daily returns
- No transaction costs or slippage modeled
- Single ticker, single period, no out-of-sample split
