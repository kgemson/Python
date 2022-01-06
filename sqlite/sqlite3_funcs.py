import sqlite3 #comes pre-installed

def create_table():
    #1. connect
    conn = sqlite3.connect("lite.db")
    #2. create cursor
    cur = conn.cursor()
    #3. write sql query
    cur.execute("CREATE TABLE IF NOT EXISTS mytable (item TEXT, quantity INTEGER, price REAL)")
    #cur.execute("DROP TABLE mytable")
    #4. commit changes
    conn.commit()
    #5. close connection
    conn.close

def insert_table(item,quantity,price):
    #1. connect
    conn = sqlite3.connect("lite.db")
    #2. create cursor
    cur = conn.cursor()
    #3. write sql query
    cur.execute("INSERT INTO mytable VALUES(?,?,?)",(item,quantity,price))
    #4. commit changes
    conn.commit()
    #5. close connection
    conn.close

def update_table(item,quantity):
    #1. connect
    conn = sqlite3.connect("lite.db")
    #2. create cursor
    cur = conn.cursor()
    #3. write sql query
    cur.execute("UPDATE mytable SET quantity = ? WHERE item = ?",(quantity,item))
    #4. commit changes
    conn.commit()
    #5. close connection
    conn.close

def delete_table(item):
    #1. connect
    conn = sqlite3.connect("lite.db")
    #2. create cursor
    cur = conn.cursor()
    #3. write sql query
    cur.execute("DELETE FROM mytable where item = ?",(item,)) #note - comma in '(item,)' is required
    #You need to pass in a sequence, and so require the comma to make your parameters a tuple. Without the comma, (item) is just a grouped expression, not a tuple, 
    #and thus the img string is treated as the input sequence. If you find it easier to read, you can also use a list literal: [item]

    #4. commit changes
    conn.commit()
    #5. close connection
    conn.close

def view_table():
    #1. connect
    conn = sqlite3.connect("lite.db")
    #2. create cursor
    cur = conn.cursor()
    #3. write sql query
    cur.execute("SELECT * FROM mytable")
    #4. fetch all
    myrows = cur.fetchall()
    #5. close connection
    conn.close

    return myrows

insert_table("Item 1",25,5.49)
#delete_table("Item 1")
update_table("Item 1",30)
print(view_table())