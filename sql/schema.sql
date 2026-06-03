CREATE TABLE dim_fund (
amfi_code TEXT PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
risk_category TEXT
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
nav_date DATE,
nav REAL,
FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code TEXT,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
state TEXT,
city TEXT,
kyc_status TEXT,
FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
alpha REAL,
beta REAL,
sharpe_ratio REAL,
sortino_ratio REAL,
expense_ratio_pct REAL,
FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE dim_benchmark (
benchmark_id INTEGER PRIMARY KEY AUTOINCREMENT,
benchmark_name TEXT,
benchmark_return REAL
);
