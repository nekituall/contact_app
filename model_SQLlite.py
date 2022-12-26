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
      login TEXT NOT NULL
    )
    """)

    con.commit()
    con.close()


def add_contact(user):
    "Function to add contact into DB, no checks for input data"
    try:
        while True:
            print("Please fill in contact info:")
            surname = input("Type in Surname:  ")
            name = input("Type in Name:  ")
            secname = input("Type in Second name:  ")
            company = input("Type in company name:  ")
            job = input("Type in job:  ")
            email = input("Type in email:  ")
            tel = input("Type in phone number:  ")
            contact = [surname, name, secname, company, job, email, tel, "valid", user]
            choice = input(f"{contact} \nis this info correct? yes/no:     ")
            if choice == "yes" or choice == "y":
                insert_contact(contact)
                print("Contact has been added")
                add = input("Add more contact? yes/no:      ")
                if add != "yes" or "y":
                    break
            else:
                print('Okay, Let`s try again')
    except Exception as e:
        print(f"{e} occured")


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
    res = cur.fetchall()
    print(res)
    con.commit()
    con.close()


def select_all(user):
    """This is select all func, login dependant """
    if user != "admin":
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE login = '{user}'")
        res = cur.fetchall()
        for i in res:
            print(i)
        con.commit()
        con.close()
    else:
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM contacts")
        res = cur.fetchall()
        for i in res:
            print(i)
        con.commit()
        con.close()


def order_by(user):
    """This is sor function for select"""
    var = int(input("You have requested sort function. Here are available columns :\n 1. Surname\n 2. Name\n 3. Second name\n"
                " 4. Company\n 5. Job\n 6. Email\n 7. Phone\n\nEnter column number:   "))


    def data(var):
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
        return col

    if user != "admin":
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        col = data(var)
        cur.execute(f"SELECT * FROM contacts WHERE login = '{user}' ORDER BY {col}")
        res = cur.fetchall()
        for i in res:
            print(i)
        con.commit()
        con.close()
    else:
        con = sqlite3.connect("connect_app.db")
        cur = con.cursor()
        data(var)
        cur.execute(f"SELECT * FROM contacts ORDER BY {var}")
        res = cur.fetchall()
        for i in res:
            print(i)
        con.commit()
        con.close()


# create_db()
# user = "vasya"
# order_by(user)


def search_name():
    pass