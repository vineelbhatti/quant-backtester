import pytest
import pandas as pd
from src.strategy.mean_reversion import add_signal

def test_add_signal_adds_expected_columns():
    data = pd.DataFrame({"Close": [100, 102, 104, 103, 105]})
    result = add_signal(data, window=3)
    assert "MA" in result.columns
    assert "PctFromMA" in result.columns

def test_add_signal_computes_correct_values():
    data = pd.DataFrame({"Close": [100, 102, 104]})
    result = add_signal(data, window=3)

    expected_ma = (100 + 102 + 104) / 3
    assert result["MA"].iloc[2] == pytest.approx(expected_ma)

    expected_pct = (104 - expected_ma) / expected_ma
    assert result["PctFromMA"].iloc[2] == pytest.approx(expected_pct)