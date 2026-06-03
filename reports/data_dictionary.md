# Data Dictionary

## 1. dim_fund

Source: 01_fund_master.csv

| Column Name        | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| amfi_code          | TEXT      | Unique AMFI scheme code     |
| fund_house         | TEXT      | Mutual fund company name    |
| scheme_name        | TEXT      | Scheme name                 |
| category           | TEXT      | Fund category (Equity/Debt) |
| sub_category       | TEXT      | Fund sub-category           |
| plan               | TEXT      | Direct/Regular plan         |
| launch_date        | DATE      | Scheme launch date          |
| benchmark          | TEXT      | Benchmark index             |
| expense_ratio_pct  | REAL      | Expense ratio percentage    |
| exit_load_pct      | REAL      | Exit load percentage        |
| min_sip_amount     | REAL      | Minimum SIP amount          |
| min_lumpsum_amount | REAL      | Minimum lump sum investment |
| fund_manager       | TEXT      | Fund manager name           |
| risk_category      | TEXT      | Risk classification         |
| sebi_category_code | TEXT      | SEBI category code          |

---

## 2. fact_nav

Source: clean_nav_history.csv

| Column Name | Data Type | Description     |
| ----------- | --------- | --------------- |
| amfi_code   | TEXT      | Fund identifier |
| date        | DATE      | NAV date        |
| nav         | REAL      | Net Asset Value |

---

## 3. fact_transactions

Source: clean_investor_transactions.csv

| Column Name        | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Investor identifier        |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | TEXT      | Scheme code                |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | REAL      | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier 1 / Tier 2 / Tier 3   |
| age_group          | TEXT      | Investor age group         |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Payment method             |
| kyc_status         | TEXT      | KYC verification status    |

---

## 4. fact_performance

Source: clean_scheme_performance.csv

| Column Name          | Data Type | Description                       |
| -------------------- | --------- | --------------------------------- |
| amfi_code            | TEXT      | Scheme code                       |
| scheme_name          | TEXT      | Scheme name                       |
| fund_house           | TEXT      | Fund house                        |
| category             | TEXT      | Fund category                     |
| plan                 | TEXT      | Direct/Regular                    |
| return_1yr_pct       | REAL      | 1-Year return (%)                 |
| return_3yr_pct       | REAL      | 3-Year return (%)                 |
| return_5yr_pct       | REAL      | 5-Year return (%)                 |
| benchmark_3yr_pct    | REAL      | Benchmark return (%)              |
| alpha                | REAL      | Alpha metric                      |
| beta                 | REAL      | Beta metric                       |
| sharpe_ratio         | REAL      | Sharpe ratio                      |
| sortino_ratio        | REAL      | Sortino ratio                     |
| std_dev_ann_pct      | REAL      | Annualized standard deviation     |
| max_drawdown_pct     | REAL      | Maximum drawdown (%)              |
| aum_crore            | REAL      | Assets Under Management (Crore ₹) |
| expense_ratio_pct    | REAL      | Expense ratio (%)                 |
| morningstar_rating   | INTEGER   | Morningstar rating                |
| risk_grade           | TEXT      | Risk grade                        |
| negative_sharpe_flag | BOOLEAN   | Indicates negative Sharpe ratio   |
| expense_ratio_valid  | BOOLEAN   | Expense ratio validation flag     |

---

## 5. dim_benchmark

Source: benchmark dataset

| Column Name      | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| benchmark_id     | INTEGER   | Benchmark identifier   |
| benchmark_name   | TEXT      | Benchmark index name   |
| benchmark_return | REAL      | Benchmark return value |

Day 2 Deliverable
