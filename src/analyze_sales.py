
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "sales.csv"

REQUIRED_COLUMNS = [
    "order_id", "order_date", "category",
    "quantity", "revenue", "cost", "profit"
]


def analyze_sales(df):
    missing = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])

    total_orders = df["order_id"].nunique()
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    total_units = df["quantity"].sum()

    profit_margin = (
        total_profit / total_revenue * 100
        if total_revenue else 0
    )

    average_order_value = (
        total_revenue / total_orders
        if total_orders else 0
    )

    category_summary = (
        df.groupby("category")
        .agg(
            orders=("order_id", "nunique"),
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
            units_sold=("quantity", "sum")
        )
        .sort_values("revenue", ascending=False)
    )

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_units": total_units,
        "profit_margin": profit_margin,
        "average_order_value": average_order_value,
        "category_summary": category_summary
    }


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE)
    result = analyze_sales(df)

    print("\n========== SALES ANALYTICS ==========")

    for key, value in result.items():
        if key != "category_summary":
            print(f"{key}: {value}")

    print("\n========== CATEGORY ANALYSIS ==========")
    print(result["category_summary"].round(2))
