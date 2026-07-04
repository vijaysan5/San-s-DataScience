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
        Rating TEXT,
        Gender TEXT,
        Quantity TEXT
    )
""")
con.commit()

# Update :
def Detailz(Branch, City, Rating, Gender, Quantity):
    csr.execute("""
        INSERT INTO smart
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(Branch) DO UPDATE SET
            City = excluded.City,
            Gender = excluded.Gender
    """, (Branch, City, Rating, Gender, Quantity))
    con.commit()

for x, row in smark.iterrows():
    if x == x:
        Detailz(row["Branch"], row["City"], row["Rating"], row["Gender"], row["Quantity"])
        print("--------------")
        break

def read_detail(Branch):
    csr.execute("SELECT * FROM smart WHERE Branch = ?", (Branch,))
    detz = csr.fetchone()
    if detz :
        print(f"Supermarket Sales Detail:-----\n~Branch In: {detz[0]}\n~City: {detz[1]}\n~Rating: {detz[2]}\n~Gender: {detz[3]}\n~Quantity: {detz[4]}\n")
        return detz
    else:
        print(f"Supermarket Sales Detail:-----\n '{Branch}' is Not Found.")
        return None
def main():
    read_detail("A")
    read_detail("B")
    read_detail("C")

if __name__ == "__main__":
    main()
    con.close()
