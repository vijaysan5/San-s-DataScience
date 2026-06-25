
# Time Series > Data Analysis
""" import pandas as pan
import matplotlib.pyplot as mtpy

dts = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/time-series-data.csv")
print("Dataset :\n", dts.head())

# flow >>> dts["flow"] using plot
mtpy.plot(dts["timestamp"], dts["flow"], color="Red")
mtpy.show()

# temp >>> dts["temp"] using plot
mtpy.plot(dts["timestamp"], dts["temp"], color="green")
mtpy.show()
 """


# Forecasting :
import pandas as pan 
import numpy as num
import matplotlib.pyplot as mtpy
from xgboost import XGBRegressor

product = pan.read_csv("San's  DataScience Folder/001 ds excel csv files/monthly-beer-production-in-austr.csv", parse_dates=["Month"])
product.set_index("Month", inplace=True)

for lag in range(1, 15):
    product[f"lag_{lag}"] = product["Monthly beer production"].shift(lag)

product.dropna(inplace=True)

pro_a = product.drop(["Monthly beer production"], axis=1)
pro_b = product["Monthly beer production"]

pro_pre = XGBRegressor(n_estimators=100)
pro_pre.fit(pro_a, pro_b)

# next 12 months 
future = [ ]
pro_copy = product.copy()

for x in range(12):
    last_r = pro_copy.iloc[-1]
    in_data = pro_copy.iloc[-1:][[f"lag_{y}" for y in range(1, 15)]].copy()
    # print(in_data)

    # SHIFT LAG >>>
    for y in range(12, 1, -1):
        in_data[f"lag_{y}"] = in_data[f"lag_{y-1}"]
    in_data["lag_1"] = last_r["Monthly beer production"]
    # print(in_data["lag_1"])

    # NEXT Predict >>>
    next_pre = pro_pre.predict(in_data)[0]
    future.append(next_pre)
    # print("Future Predit :", future)
    # ---------------------------------------------
    new = pan.DataFrame({
        "Monthly beer production": [next_pre],
        **{f"lag_{y}": in_data.iloc[0][f"lag_{y}"] for y in range(1, 15)}
    }, index=[pro_copy.index[-1] + pan.DateOffset(months=1)])

    last_one = pan.concat([pro_copy, new])
    # print(last_one)

# Future :
future_data = pan.date_range(start=product.index[-1] + pan.DateOffset(months=1), periods=12, freq="ME")

# Plot
mtpy.figure(figsize=(10, 8))
mtpy.plot(product.index, product["Monthly beer production"], label="Historical")
mtpy.plot(future_data, future, label="Forecast", color= "Blue", linestyle="--")
mtpy.title("Forecasting >>> Monthly Production")
mtpy.xlabel("Month")
mtpy.ylabel("Monthly beer production")
mtpy.grid(True)
mtpy.show()