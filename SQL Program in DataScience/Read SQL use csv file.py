import sqlite3 as sq

con = sq.connect("Supermarket.db")
cur = con.cursor()

cur.execute("SELECT * FROM smart")

row = cur.fetchall()

for read in row:
    print(read)
