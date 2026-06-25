""" 

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
plt.show() """







print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

# Dimension

# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("dataset/dim_reduction_dataset.csv")
# X=df.drop(columns=["target"])
# # print(X)
# xs=StandardScaler().fit_transform(X)
# print(xs)
# pca=PCA(n_components=2)
# xp=pca.fit_transform(xs)
# print(xp)
# plt.scatter(xp[:,0],xp[:,1])
# plt.show() 


#Association rule mining

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

df=pd.read_csv("dataset/supermarket_transactions.csv")
print(df)
transactions=df["Items"].apply(lambda x:x.split(","))
print(transactions)


te=TransactionEncoder()
te_data=te.fit_transform(transactions)
df_encoded=pd.DataFrame(te_data,columns=te.columns_)
print(df_encoded)

freq=apriori(df_encoded,min_support=0.05,use_colnames=True)
rule=association_rules(freq,metric="lift",min_threshold=1)

print(rule[["antecedents","consequents","support","confidence","lift"]]
      .sort_values(by="lift",ascending=False).head(10))
