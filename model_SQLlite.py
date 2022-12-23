import sqlite3
from sqlite3 import Error
login = "user"

def connect_db():
    try:
        con = sqlite3.connect("connect_app.db")
        print("Connection to SQLite DB established successfully!")
    except Error as e:
        print(f"The error '{e}' occurred")

    cur = con.cursor()   #создаем обьект курсор для запросов

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
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
    return cur

def add_contact(cur,login):
    "function to add contact into DB, no checks for input data"
    try:
        while True:
            surname = input("Type in Surname:  ")
            name = input("Type in Name:  ")
            secname = input("Type in Second name:  ")
            company = input("Type in company name:  ")
            job = input("Type in job:  ")
            email = input("Type in email:  ")
            tel = input("Type in phone number:  ")
            cont = (surname, name, secname, company, job, email, tel, "valid", login)
            choice = input(f"{cont} \nis this info correct? yes/no:     ")
            if choice == "yes" or choice == "y":
                cur.execute("INSERT INTO contacts VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", cont)
                print("Contact has been added")
                add = input("Add more contact? yes/no:      ")
                if add != "yes" or "y":
                    break
            else:
                print('Okay, Let`s try again')
    except Exception as e:
        print(f"{e} occured")

cur = connect_db()
add_contact(cur,login)

def edit_contact():
    pass


def del_contact():
    pass


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