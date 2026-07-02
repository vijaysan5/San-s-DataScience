import sqlite3 as sq

# Connect >>> SQLite >>> DB
con = sq.connect("Emp.db")
csr = con.cursor()

# Create a Table :
csr.execute("""
    CREATE TABLE IF NOT EXISTS emp (
        username TEXT PRIMARY KEY,
        firstname TEXT,
        lastname TEXT,
        age INTEGER,
        email TEXT
    )
""")
con.commit()

# Update Detailz :
def emp_detail(username, firstname, lastname, age, email):
    csr.execute("""
        INSERT INTO emp (username, firstname, lastname, age, email)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
            firstname = excluded.firstname,
            lastname = excluded.lastname,
            age = excluded.age,
            email = excluded.email
    """, (username, firstname, lastname, age, email))
    con.commit()
    print(f"User >>> '{username}s' Data is Updated...")

# Read emp Detailz :
def read_detail(username):
    csr.execute("SELECT * FROM emp WHERE username = ?", (username,))
    user = csr.fetchone()
    if user :
        print(f"EMP: {user[0]}\n~First Name: {user[1]}\n~Last Name: {user[2]}\n~Age: {user[3]}\n~Email ID: {user[4]}\n")
        return user
    else:
        print(f"EMP: '{username}' is Not Found.")
        return None

# Functions :
def main():
    emp_detail("dhiya", "DhiyaShree", "Vijayan", "23", "dhiyashree25@gmail.com")
    emp_detail("hanvi", "Hanvika", "Dhilip", "25", "hanvi25@gmail.com")
    emp_detail("kathir", "Kathiresh", "Kaviyarasu", "26", "kathir21@gamil.com")
    read_detail("dhiya")
    read_detail("hanvika")


if __name__ == "__main__":
    main()
    con.close()