#----------------------------------------------------------
# Developer ----- Bryce Martin
# Description --- This program will be able to work with
#                 databases via PostgreSQL
#----------------------------------------------------------
#the psycopg2 function is a python built in function

import psycopg2

def creat_table():
    #this will either connect to the database with the given name or create a new database
    connection = psycopg2.connect("dbname='database1' user= 'postgres' password ='bryce1jax' host= 'localhost' port = '5433'")
    cur = connection.cursor() #defines our cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #here we can execute SQL commands

    connection.commit() #then commit the changes
    connection.close() # dont forget to close the connection

def insert(item, quantity, price):
        connection = psycopg2.connect("dbname='database1' user= 'postgres' password ='bryce1jax' host= 'localhost' port = '5433'")
        cur = connection.cursor() #defines our cursor
        cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity, price)) #you can pass in parameters this way
        connection.commit()
        connection.close()

#a function to view the db
def view():
    connection = psycopg2.connect("dbname='database1' user= 'postgres' password ='bryce1jax' host= 'localhost' port = '5433'")
    cur = connection.cursor() #defines our cursor
    cur.execute("SELECT * FROM store") #selected everything from the db
    rows = cur.fetchall() #fetches everything
    connection.close()
    return rows

#a function to delete from the db
def delete(item):
    connection = psycopg2.connect("dbname='database1' user= 'postgres' password ='bryce1jax' host= 'localhost' port = '5433'")
    cur = connection.cursor() #defines our cursor
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) #selected everything from the db
    connection.commit()
    connection.close()

#a function to update the quantity and price of preexisting items
def update(quantity,price,item):
    connection = psycopg2.connect("dbname='database1' user= 'postgres' password ='bryce1jax' host= 'localhost' port = '5433'")
    cur = connection.cursor() #defines our cursor
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item)) #selected everything from the db
    connection.commit()
    connection.close()


#creat_table()

