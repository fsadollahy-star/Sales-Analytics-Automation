
import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "sales.csv"
OUTPUT_FILE = ROOT / "output" / "Sales_Report.xlsx"

# Load data
df = pd.read_csv(DATA_FILE)
df["order_date"] = pd.to_datetime(df["order_date"])

# Calculate KPIs
total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_units = df["quantity"].sum()
profit_margin = total_profit / total_revenue * 100

# Category analysis
category = df.groupby("category", as_index=False).agg(
    Revenue=("revenue", "sum"),
    Profit=("profit", "sum"),
    Units=("quantity", "sum")
)

# Monthly analysis
df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly = df.groupby("month", as_index=False).agg(
    Revenue=("revenue", "sum"),
    Profit=("profit", "sum")
)

# Create Excel workbook
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sales Data", index=False)
    category.to_excel(writer, sheet_name="Analysis", index=False)
    monthly.to_excel(
        writer, sheet_name="Analysis",
        index=False, startrow=len(category) + 4
    )

# Format workbook
wb = load_workbook(OUTPUT_FILE)

dashboard = wb.create_sheet("Dashboard", 0)

dashboard["A1"] = "SALES ANALYTICS DASHBOARD"
dashboard["A1"].font = Font(
    size=20, bold=True, color="FFFFFF"
)
dashboard["A1"].fill = PatternFill(
    "solid", fgColor="17365D"
)
dashboard.merge_cells("A1:D1")

kpis = [
    ("Total Revenue", total_revenue),
    ("Total Profit", total_profit),
    ("Total Orders", total_orders),
    ("Units Sold", total_units),
    ("Profit Margin (%)", round(profit_margin, 2))
]

for row, (label, value) in enumerate(kpis, start=3):
    dashboard.cell(row, 1, label)
    dashboard.cell(row, 2, value)
    dashboard.cell(row, 1).font = Font(bold=True)
    dashboard.cell(row, 2).font = Font(
        bold=True, color="008080"
    )
# Category chart
analysis = wb["Analysis"]

bar = BarChart()
bar.type = "col"
bar.title = "Revenue by Category"
bar.y_axis.title = "Revenue ($)"
bar.x_axis.title = "Category"
bar.legend = None

data = Reference(
    analysis, min_col=2, min_row=1, max_row=4
)

categories = Reference(
    analysis, min_col=1, min_row=2, max_row=4
)

bar.add_data(data, titles_from_data=True)
bar.set_categories(categories)

dashboard.add_chart(bar, "D3")


# Monthly revenue chart
line = LineChart()
line.title = "Monthly Revenue Trend"
line.y_axis.title = "Revenue ($)"
line.x_axis.title = "Month"
line.legend = None

monthly_data = Reference(
    analysis, min_col=2, min_row=8, max_row=20
)

monthly_categories = Reference(
    analysis, min_col=1, min_row=9, max_row=20
)

line.add_data(monthly_data, titles_from_data=True)
line.set_categories(monthly_categories)

dashboard.add_chart(line, "D20")
# Column widths
for ws in wb.worksheets:
    for col in ws.columns:
        max_length = max(
            len(str(cell.value or "")) for cell in col
        )
        ws.column_dimensions[
            get_column_letter(col[0].column)
        ].width = min(max_length + 3, 30)

dashboard.freeze_panes = "A3"

# Format KPI values
for cell in ["B3", "B4"]:
    dashboard[cell].number_format = '$#,##0.00'

dashboard["B5"].number_format = '#,##0'
dashboard["B6"].number_format = '#,##0'
dashboard["B7"].number_format = '0.00"%"'

wb.save(OUTPUT_FILE)

print("Dashboard created successfully!")
print(f"Output: {OUTPUT_FILE}")
