import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

def recommend_funds(risk):

    funds = performance[
        performance["risk_grade"] == risk
    ]

    top3 = (
        funds.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return top3[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]

print(recommend_funds("Moderate"))