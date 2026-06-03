-- 1. Top 5 funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Funds with Expense Ratio < 1%

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 4. Transaction Count by State

SELECT state, COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 5. Total Investment by Transaction Type

SELECT transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Average 3-Year Return

SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 7. Top 10 Funds by Sharpe Ratio

SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Funds with Negative Sharpe Ratio

SELECT scheme_name
FROM fact_performance
WHERE sharpe_ratio < 0;

-- 9. Average AUM by Category

SELECT category,
AVG(aum_crore)
FROM fact_performance
GROUP BY category;

-- 10. Number of KYC Verified Investors

SELECT kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;
