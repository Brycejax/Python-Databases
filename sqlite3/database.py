#----------------------------------------------------------
# Developer ----- Bryce Martin
# Description --- This program will be able to work with
#                 databases via sqlite3
#----------------------------------------------------------
#the sqlite3 function is a python built in function

import sqlite3

def creat_table():
    #this will either connect to the database with the given name or create a new database
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor() #defines our cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #here we can execute SQL commands

    connection.commit() #then commit the changes
    connection.close() # dont forget to close the connection

def insert(item, quantity, price):
        connection = sqlite3.connect("lite.db")
        cur = connection.cursor() #defines our cursor
        cur.execute("INSERT INTO store VALUES (?,?,?)" ,(item, quantity, price)) #you can pass in parameters this way
        connection.commit()
        connection.close()

#a function to view the db
def view():
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor() #defines our cursor
    cur.execute("SELECT * FROM store") #selected everything from the db
    rows = cur.fetchall() #fetches everything
    connection.close()
    return rows

#a function to delete from the db
def delete(item):
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor() #defines our cursor
    cur.execute("DELETE FROM store WHERE item=?", (item,)) #selected everything from the db
    connection.commit()
    connection.close()

#a function to update the quantity and price of preexisting items
def update(quantity,price,item):
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor() #defines our cursor
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item)) #selected everything from the db
    connection.commit()
    connection.close()

update(11,6,"Water Glass")

print(view()) #returned as a list