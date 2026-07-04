import pandas as pan
import sqlite3 as sq

smark = pan.read_csv("San's  DataScience Folder/SQL Program in DataScience/supermarket_sales - Sheet1.csv")


# for column in smark.columns:
    # print(column)


con = sq.connect("Supermarket.db")
csr = con.cursor()

# Create Table :
csr.execute("""
    CREATE TABLE IF NOT EXISTS smart (
        Branch TEXT PRIMARY KEY,
        City TEXT,
        Payment TEXT,
        Gender TEXT,
        Quantity TEXT
    )
""")
con.commit()

# Update :
def Detailz(Branch, City, Payment, Gender, Quantity):
    csr.execute("""
        INSERT INTO smart
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(Branch) DO UPDATE SET
            City = excluded.City,
            Payment = excluded.Payment,
            Gender = excluded.Gender,
            Quantity = excluded.Quantity
    """, (Branch, City, Payment, Gender, Quantity))
    con.commit()

for x, row in smark.iterrows():
    if x == x:
        # print(row["Branch"], row["City"], row["Payment"], row["Gender"], row["Quantity"])

    
