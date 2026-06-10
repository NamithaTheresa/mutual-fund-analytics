"""
Mutual Fund Analytics Project

Purpose:
Clean and process NAV history data.

Author: Namitha Theresa VJ
"""
import pandas as pd

# Load data

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column

df["date"] = pd.to_datetime(
    df["date"],
    format="mixed",
    errors="coerce"
)

# Sort values

df = df.sort_values(["amfi_code", "date"])

# Fill missing NAV values

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates

df = df.drop_duplicates()

# Keep only valid NAVs

df = df[df["nav"] > 0]

# Save cleaned file

df.to_csv(
"data/processed/clean_nav_history.csv",
index=False
)

print(df.shape)
print("NAV cleaning complete")
