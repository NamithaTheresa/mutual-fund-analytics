"""
Mutual Fund Analytics Project

Purpose:
Load processed data into SQLite database.

Author: Namitha Theresa VJ
"""
import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav_df = pd.read_csv("data/processed/clean_nav_history.csv")
trans_df = pd.read_csv("data/processed/clean_investor_transactions.csv")
perf_df = pd.read_csv("data/processed/clean_scheme_performance.csv")

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

# Write tables
fund_df.to_sql("dim_fund", engine, if_exists="replace", index=False)

nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)

trans_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully!")