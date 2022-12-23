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
    cur.execute("INSERT INTO contacts (surname, name, secname, company, job, email, phone, active, user) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", contact)
    con.commit()
    con.close()


def update_contact(contact, arg1, arg2):
    """Modify selected contact on cases in args"""
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute(f"UPDATE contacts SET {arg1} WHERE {arg2}")
    con.commit()
    con.close()

def delete_contact(contact, arg1, arg2):
    """Delete selected contact """
    con = sqlite3.connect("connect_app.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM contacts WHERE {arg1} = {arg2}")
    con.commit()
    con.close()






def view_del():
    pass


def view_all():
    pass


def sort_by():
    pass

def filter_by():
    pass


def search_name():
    pass