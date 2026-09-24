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