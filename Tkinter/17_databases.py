import os
from tkinter import Tk
import sqlite3

dirname = os.path.dirname(__file__)
os.chdir(dirname)


root = Tk()
root.geometry("400x400")

# database
conn = sqlite3.connect('address_book.db')  # create or connect a DB
this_cursor = conn.cursor()  # create a cursor

# create table
this_cursor.execute("""
    --sql
    CREATE TABLE addresses (
        first_name text,
        last_name text,
        city text,
        us_state text,
        zipcode integer
        ) 
    ;
    """)

conn.commit()  # commit changes to DB
conn.close()  # close connection to DB


root.mainloop()
