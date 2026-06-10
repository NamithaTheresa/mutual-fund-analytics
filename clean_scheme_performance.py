"""
Mutual Fund Analytics Project

Purpose:
Clean and process scheme performance data.

Author: Namitha Theresa VJ
"""
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert performance columns to numeric
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with invalid return values
df = df.dropna(subset=[
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
])

# Flag negative Sharpe ratios
df["negative_sharpe_flag"] = df["sharpe_ratio"] < 0

# Validate expense ratio range (0.1% - 2.5%)
df["expense_ratio_valid"] = (
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
)

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("Cleaning Complete")
print("Rows:", len(df))

print("\nNegative Sharpe Ratio Funds:")
print(df["negative_sharpe_flag"].sum())

print("\nInvalid Expense Ratios:")
print((~df["expense_ratio_valid"]).sum())