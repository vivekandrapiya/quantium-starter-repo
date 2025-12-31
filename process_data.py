import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

csv_files = [
    DATA_DIR / "daily_sales_data_0.csv",
    DATA_DIR / "daily_sales_data_1.csv",
    DATA_DIR / "daily_sales_data_2.csv"
]

all_data = []

for file in csv_files:
    df = pd.read_csv(file)

    df["product"] = df["product"].str.strip().str.lower()

  
    df = df[df["product"] == "pink morsel"]

    if df.empty:
        continue

  
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .astype(float)
    )

    df = df.dropna(subset=["quantity", "price"])


    df["Sales"] = df["quantity"] * df["price"]

    df = df[["Sales", "date", "region"]]

    df.rename(columns={
        "date": "Date",
        "region": "Region"
    }, inplace=True)

    all_data.append(df)


final_df = pd.concat(all_data, ignore_index=True)


output_path = DATA_DIR / "output.csv"
final_df.to_csv(output_path, index=False)

print("output.csv created")
