import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


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