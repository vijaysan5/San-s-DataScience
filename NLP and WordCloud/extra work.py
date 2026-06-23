

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

df=pd.read_csv("dataset/forecasting_dataset.csv",parse_dates=["Date"])
df.set_index("Date",inplace=True)

for lag in range(1,13):
    df[f"lag_{lag}"]=df["Sales"].shift(lag)

df.dropna(inplace=True)

x=df.drop("Sales",axis=1)
y=df["Sales"]

model=XGBRegressor(n_estimators=100)
model.fit(x,y)
# Forecast next 12 months
future_preds = []
last_known = df.copy()


for i in range(12):
    last_row = last_known.iloc[-1]
    input_data = last_known.iloc[-1:][[f"lag_{j}" for j in range(1, 13)]].copy()


    # Shift lag features
    for j in range(12, 1, -1):
        input_data[f"lag_{j}"] = input_data[f"lag_{j-1}"]
    input_data["lag_1"] = last_row["Sales"]


    # Predict next value
    next_pred = model.predict(input_data)[0]
    future_preds.append(next_pred)

    # Append prediction for next step
    new_row = pd.DataFrame({
        "Sales": [next_pred],
        **{f"lag_{j}": input_data.iloc[0][f"lag_{j}"] for j in range(1, 13)}
    }, index=[last_known.index[-1] + pd.DateOffset(months=1)])

    last_known = pd.concat([last_known, new_row])

# Create future index
future_dates = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=12, freq="M")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Sales"], label="Historical")
plt.plot(future_dates, future_preds, label="Forecast", linestyle="--", color="red")
plt.title("Forecasting Sales with XGBoost")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
