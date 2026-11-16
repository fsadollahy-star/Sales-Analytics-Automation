
# Sales Analytics Automation

A Python-based sales data analysis and Excel dashboard automation project.

## Project Overview

This project analyzes sales data using Python and Pandas, generates key business performance metrics, and creates an automated Excel report with interactive-style dashboards and charts.

The project uses a synthetic sales dataset containing 240 records from January to December 2025.

## Features

- Generate synthetic sales data
- Analyze total revenue, profit, units sold, and profit margin
- Calculate average order value
- Summarize sales performance by product category
- Analyze monthly revenue trends
- Generate an Excel report automatically
- Create KPI summaries and charts in Excel
- Validate analysis functions using automated tests

## Technologies

- Python
- Pandas
- OpenPyXL
- Excel
- Pytest
- Git & GitHub

## Project Structure

```text
Sales_Analytics_Automation/
│
├── data/
│   └── sales.csv
│
├── output/
│   └── Sales_Report.xlsx
│
├── src/
│   ├── generate_data.py
│   ├── analyze_sales.py
│   └── build_dashboard.py
│
├── tests/
│   └── test_analysis.py
│
├── .gitignore
└── README.md
```

## How to Run

### 1. Install dependencies

```bash
pip install pandas openpyxl pytest
```

### 2. Generate the sales dataset

```bash
python src/generate_data.py
```

### 3. Run sales analysis

```bash
python src/analyze_sales.py
```

### 4. Build the Excel dashboard

```bash
python src/build_dashboard.py
```

### 5. Run automated tests

```bash
python -m pytest -v
```

## Output

The project generates an Excel report named `Sales_Report.xlsx`, containing:

- Dashboard: Key performance indicators and charts
- Sales Data: The original sales dataset
- Analysis: Category and monthly sales summaries

## Testing

Automated tests are included to verify the sales analysis calculations and input validation.

## Project Purpose

This project demonstrates practical skills in Python programming, data analysis, Excel automation, reporting, and software testing.
