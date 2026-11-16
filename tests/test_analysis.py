import pandas as pd
import pytest

from src.analyze_sales import analyze_sales


def test_sales_analysis():
    df = pd.DataFrame({
        "order_id": [1, 2, 3],
        "order_date": ["2025-01-01", "2025-01-02", "2025-01-03"],
        "category": ["A", "B", "A"],
        "quantity": [1, 2, 3],
        "revenue": [100, 200, 300],
        "cost": [60, 120, 180],
        "profit": [40, 80, 120]
    })

    result = analyze_sales(df)

    assert result["total_orders"] == 3
    assert result["total_revenue"] == 600
    assert result["total_profit"] == 240
    assert result["total_units"] == 6
    assert result["profit_margin"] == 40
    assert result["average_order_value"] == 200


def test_missing_column():
    df = pd.DataFrame({
        "order_id": [1],
        "revenue": [100]
    })

    with pytest.raises(ValueError):
        analyze_sales(df)