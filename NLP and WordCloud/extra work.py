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




import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        full_name TEXT,
        email TEXT,
        age INTEGER
    )
''')
conn.commit()

# Insert or update user (like write/overwrite)
def write_user(username, full_name, email, age):
    cursor.execute('''
        INSERT INTO users (username, full_name, email, age)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
            full_name = excluded.full_name,
            email = excluded.email,
            age = excluded.age
    ''', (username, full_name, email, age))
    conn.commit()
    print(f"User '{username}' saved or updated.\n")

 

# Read user details
def read_user(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if user:
        print(f"User: {user[0]}\nFull Name: {user[1]}\nEmail: {user[2]}\nAge: {user[3]}\n")
        return user
    else:
        print(f"User '{username}' not found.\n")
        return None



# Test the functions
def main():
    # write_user("alice", "Alice Johnson", "alice@example.com", 28)

    # write_user("bob", "Bob Smith", "bob@example.com", 35)
    read_user("bob")

    

if __name__ == "__main__":
    main()
    conn.close()
