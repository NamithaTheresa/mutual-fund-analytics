import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# Keep only valid transaction types
valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]
df = df[df["transaction_type"].isin(valid_types)]

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.upper()
)

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("Cleaning Complete")
print("Rows:", len(df))
print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())