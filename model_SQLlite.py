import sqlite3
from sqlite3 import Error


def create_db():
    try:
        con = sqlite3.connect("connect_app.db")
        print("SQLite DB established successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
      contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
      surname TEXT NOT NULL,
      name TEXT NOT NULL,
      secname TEXT NOT NULL,
      company TEXT NOT NULL,
      job TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL,
      active TEXT NOT NULL,
      user TEXT NOT NULL
    )
    """)

    con.commit()
    con.close()


def insert_contact(contact):
    """Function to add contact into DB, no checks for input data"""
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contacts (surname, name, secname, company, job, email, phone, active, login) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", contact)
    con.commit()
    con.close()


def update_contact(contact, arg1, arg2):
    """Modify selected contact on cases in args"""
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute(f"UPDATE contacts SET {arg1} WHERE {arg2}")
    con.commit()
    con.close()

def delete_contact(contact):
    """Make selected contact invalid for listing"""
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute(f"UPDATE contacts SET active = 'invalid' WHERE {contact}")
    con.commit()
    con.close()


def select_del():
    """This is func for admin to see deleted contacts"""
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM contacts WHERE active = 'invalid'")
    con.commit()
    con.close()


def select_all(user):
    """This is select all func, login dependant """
    if user != "admin":
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE login = '{user}'")
        con.commit()
        con.close()
    else:
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM contacts")
        con.commit()
        con.close()


def order_by(user):
    """This is sor function for select"""
    var = int(input("You have requested sort function. Here are available columns :\n 1. Surname\n 2. Name\n 3. Second name\n"
                " 4. Company\n 5. Job\n 6. Email\n 7. Phone\n\nEnter column number:   "))
    if var == 1:
        col = "surname"
    elif var == 2:
        col = "name"
    elif var == 3:
        col = "secname"
    elif var == 4:
        col = "company"
    elif var == 5:
        col = "job"
    elif var == 6:
        col = "email"
    elif var == 7:
        col = "phone"
    else:
        print("Invalid column")
    if user != "admin":
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE login = '{user}' ORDER BY {var}")
        con.commit()
        con.close()
    else:
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM contacts ORDER BY {var}")
        con.commit()
        con.close()


user = "vasya"
order_by(user)

def filter_by():
    pass


def search_name():
    pass