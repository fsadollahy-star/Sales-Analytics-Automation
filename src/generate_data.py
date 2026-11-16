
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = ROOT / "data" / "sales.csv"

regions = ["North", "South", "East", "West"]

products = {
    "Electronics": {
        "Laptop": (800, 550),
        "Mouse": (25, 10),
        "Monitor": (250, 160),
    },
    "Furniture": {
        "Desk": (300, 180),
        "Chair": (150, 85),
        "Bookshelf": (200, 120),
    },
    "Office Supplies": {
        "Notebook": (8, 3),
        "Pen Set": (12, 5),
        "Printer Paper": (15, 9),
    },
}

start_date = date(2025, 1, 1)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "order_id", "order_date", "region",
        "category", "product", "quantity",
        "unit_price", "unit_cost", "revenue",
        "cost", "profit"
    ])

    for i in range(1, 241):
        category = random.choice(list(products))
        product = random.choice(list(products[category]))
        unit_price, unit_cost = products[category][product]

        quantity = random.randint(1, 12)
        price = round(unit_price * random.uniform(0.9, 1.1), 2)

        revenue = round(quantity * price, 2)
        cost = round(quantity * unit_cost, 2)
        profit = round(revenue - cost, 2)

        order_date = start_date + timedelta(
            days=random.randint(0, 364)
        )

        writer.writerow([
            f"ORD-{i:04d}",
            order_date.isoformat(),
            random.choice(regions),
            category,
            product,
            quantity,
            price,
            unit_cost,
            revenue,
            cost,
            profit
        ])

print(f"Dataset created successfully: {OUTPUT_FILE}")
print("Total records: 240")
