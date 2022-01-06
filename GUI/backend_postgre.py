import psycopg2 as ps2

# Define constructor for database objects
def connect():
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

# Define the following founctions to be implemented in GU script - 
# "View all","Search entry","Add entry","Update","Delete","Close"
def view_all():
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    #conn.commit()
    conn.close()
    return rows

def search_entry(title="", author="", year="", isbn=""): #supplying empty values to cater for the user entering nothing in those fields
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def add_entry(title, author, year, isbn):
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT COALESCE(MAX(id),0) FROM book")
    my_id=cur.fetchone()[0]+1
    cur.execute("INSERT INTO book (id,title, author, year, isbn) VALUES (%s,%s,%s,%s,%s)",(my_id,title, author, year, isbn))
    conn.commit()
    conn.close()

def update_entry(id,title, author, year, isbn):
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title, author, year, isbn,id))
    conn.commit()
    conn.close()

def delete_entry(id):
    conn=ps2.connect("dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id = %s",(id,))
    conn.commit()
    conn.close()

# make call to 'connect' function so that we establish connection when we import
connect()

# test adding and viewing functions within stub
#   add_entry("Dracula","Bram Stoker",1895,2453678)
#   delete_entry(4)
#   print(search_entry(author="Bram Stoker"))
#   update_entry(2,"Dracula","Ham Stroker",1895,2453678)
#   print(view_all())
