# Mutual Fund Analytics Capstone Project

## Project Overview

The Mutual Fund Analytics Capstone Project is an end-to-end financial analytics solution developed to analyze mutual fund performance, investor behavior, SIP trends, portfolio risk, and industry growth. The project combines data engineering, exploratory data analysis, performance evaluation, advanced risk analytics, and business intelligence dashboards to generate actionable investment insights.

The project was completed as part of the Bluestock Fintech Mutual Fund Analytics Capstone Program.

---

## Project Objectives

* Clean and validate mutual fund datasets.
* Perform exploratory data analysis (EDA).
* Evaluate fund performance using financial metrics.
* Analyze investor behavior and SIP trends.
* Compute advanced risk metrics such as VaR and CVaR.
* Build a simple mutual fund recommendation engine.
* Develop interactive Power BI dashboards.
* Generate business insights and recommendations.

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* SQLite

### Visualization

* Matplotlib
* Seaborn
* Plotly
* Power BI

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```text
Mutual_Funds_Analytics
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── dashboard
│   └── bluestock_mf_dashboard.pbix
│
├── reports
│   ├── Final_Report.pdf
│   ├── Dashboard.pdf
│   ├── page1.png
│   ├── page2.png
│   ├── page3.png
│   └── page4.png
│
├── recommender.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd Mutual_Funds_Analytics
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Execute Main Pipeline

```bash
python run_pipeline.py
```

### Run Individual Notebooks

Open Jupyter Notebook and execute:

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

---

## Fund Recommendation System

Run:

```bash
python recommender.py
```

The system recommends top-performing mutual funds based on risk grade and Sharpe Ratio.

---

## Dashboard

The Power BI dashboard contains four pages:

### Page 1 – Industry Overview

* AUM Growth
* SIP Growth
* Industry KPIs

### Page 2 – Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* Performance Metrics

### Page 3 – Investor Analytics

* Investor Demographics
* State-wise Investments
* Transaction Analysis

### Page 4 – SIP & Market Trends

* SIP Inflows
* Category-wise Inflows
* Market Trends

### Open Dashboard

Navigate to:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Open using Microsoft Power BI Desktop.

---

## Key Features

* Data Cleaning and Validation
* SQLite Database Design
* Exploratory Data Analysis
* Fund Performance Evaluation
* VaR & CVaR Risk Analysis
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* Power BI Dashboard

---

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard
* Dashboard Screenshots
* Processed Datasets
* Analytics Notebooks
* GitHub Repository

---

## Author

**Namitha Theresa VJ**

Mutual Fund Analytics Capstone Project
Bluestock Fintech
