import pandas as pan
import sqlite3 as sq

smark = pan.read_csv("San's  DataScience Folder/SQL Program/supermarket_sales - Sheet1.csv")


# for x in smark:
    # print(x, end=" - ")
# Branch,City,Customer type,Gender,Product

con = sq.connect("Supermarket.db")
csr = con.cursor()

# Create Table :
csr.execute("""
    CREATE TABLE IF NOT EXISTS smart (
        Branch TEXT PRIMARY KEY,
        City TEXT,
        Customer TEXT,
        Gender TEXT,
        Product TEXT
    )
""")
con.commit()

# Update :
def Detailz(Branch, City, Customer, Gender, Product):
    csr.execute("""
        INSERT INTO smart (Branch, City, Customer, Gender, Product)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
            City = excluded.City,
            Customer = excluded.Customer,
            Gender = excluded.Gender,
            Product = excluded.Product
    """, (Branch, City, Customer, Gender, Product))
    con.commit()
    print(f"Detailz : '{Branch}'s Data is Updated...")

def read_Detz(Branch):
    csr.execute("SELECT * FROM smart WHERE Branch = ?", (Branch,))
    detail = csr.fetchone()

    if detail:
