import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):

    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("postgres", "postgres", "wfhdhf,fr", "127.0.0.1", "5432")


# def create_database(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
# create_database_query = "CREATE DATABASE contact_app"
# create_database(connection, create_database_query)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS contacts (
  id SERIAL PRIMARY KEY,
  surname TEXT NOT NULL,
  name TEXT NOT NULL, 
  secname TEXT NOT NULL,
  company TEXT NOT NULL,
  job TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
)
"""

execute_query(connection, create_users_table)















def add_contact():
    pass


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