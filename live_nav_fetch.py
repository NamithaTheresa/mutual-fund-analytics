import requests
import pandas as pd

# HDFC Top 100
url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    "data/raw/HDFC_Top100_Live_NAV.csv",
    index=False
)

print("HDFC Top 100 saved")


# 5 additional schemes

schemes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"{name} saved")