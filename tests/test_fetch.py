import pytest
from src.data.fetch import get_price_data

def test_price_data_returns_data_for_valid_ticker():
    data = get_price_data("AAPL", "2020-01-01", "2024-01-01")
    assert not data.empty
    assert "Close" in data.columns

def test_price_data_raises_on_invalid_ticker():
    with pytest.raises(ValueError):
        data = get_price_data("NOTREAL", "2020-01-01", "2024-01-01")