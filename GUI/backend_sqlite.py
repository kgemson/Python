import sqlite3

# Define database and connection
def connect():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

# Define the following founctions to be implemented in GU script - 
# "View all","Search entry","Add entry","Update","Delete","Close"
def view_all():
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    #conn.commit()
    conn.close()
    return rows

def search_entry(title="", author="", year="", isbn=""): #supplying empty values to cater for the user entering nothing in those fields
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def add_entry(title, author, year, isbn):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def update_entry(id,title, author, year, isbn):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()

def delete_entry(id):
    conn=sqlite3.connect("bookstore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

# declare call to connect function so that connection is established in 'import'
# note - need to re-establish connection in each function as we close each time
connect()

# test adding and viewing functions

#add_entry("Dracula","Bram Stoker",1895,2453678)
#delete_entry(4)
#print(search_entry(author="Bram Stoker"))
#update_entry(2,"Dracula","Ham Stroker",1895,2453678)
#print(view_all())
