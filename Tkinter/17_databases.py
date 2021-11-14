import os
from tkinter import Button, Entry, Label, Tk
import sqlite3
from tkinter.constants import END

dirname = os.path.dirname(__file__)
os.chdir(dirname)


root = Tk()
root.geometry("400x400")

# database
conn = sqlite3.connect('address_book.db')  # create or connect a DB
this_cursor = conn.cursor()  # create a cursor

# create table
# this_cursor.execute("""
#     --sql
#     CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         this_address text,
#         city text,
#         us_state text,
#         zipcode integer
#         )
#     ;
#     """)


# create submit function
def submit():
    conn = sqlite3.connect('address_book.db')  # create or connect a DB
    this_cursor = conn.cursor()  # create a cursor

    # insert into the table
    this_cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :this_address, :city, :us_state, :zipcode);",
                        {
                            'first_name': first_name.get(),
                            'last_name': last_name.get(),
                            'this_address': this_address.get(),
                            'city': city.get(),
                            'us_state': us_state.get(),
                            'zipcode': zipcode.get()
                        })

    conn.commit()  # commit changes to DB
    conn.close()  # close connection to DB
    # clear text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    this_address.delete(0, END)
    city.delete(0, END)
    us_state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')  # create or connect a DB
    this_cursor = conn.cursor()  # create a cursor

    # query the database
    this_cursor.execute("SELECT *, oid FROM addresses;")
    records = this_cursor.fetchall()

    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()  # commit changes to DB
    conn.close()  # close connection to DB


# create text boxes
first_name = Entry(root, width=30)
first_name.grid(column=1, row=0, padx=20)
last_name = Entry(root, width=30)
last_name.grid(column=1, row=1, padx=20)
this_address = Entry(root, width=30)
this_address.grid(column=1, row=2, padx=20)
city = Entry(root, width=30)
city.grid(column=1, row=3, padx=20)
us_state = Entry(root, width=30)
us_state.grid(column=1, row=4, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(column=1, row=5, padx=20)

# create textbox labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(column=0, row=0, padx=20)
last_name_label = Label(root, text="Last Name")
last_name_label.grid(column=0, row=1, padx=20)
this_address_label = Label(root, text="Address")
this_address_label.grid(column=0, row=2, padx=20)
city_label = Label(root, text="City")
city_label.grid(column=0, row=3, padx=20)
us_state_label = Label(root, text="State")
us_state_label.grid(column=0, row=4, padx=20)
zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(column=0, row=5, padx=20)

# create submit button
submit_btn = Button(root, text="Add Record to DB", command=submit)
submit_btn.grid(column=0, row=6, columnspan=2, padx=10, pady=10, ipadx=100)

# create query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(column=0, row=7, columnspan=2, padx=10, pady=10, ipadx=137)


conn.commit()  # commit changes to DB
conn.close()  # close connection to DB

root.mainloop()
