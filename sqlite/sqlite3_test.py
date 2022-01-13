import sqlite3 #comes pre-installed

#1. connect
conn = sqlite3.connect("lite.db")

#2. create cursor
cur = conn.cursor()

#3. write sql query
cur.execute("CREATE TABLE IF NOT EXISTS mytable (item TEXT, quantity INTEGER, price REAL)")
#cur.execute("DROP TABLE mytable")
cur.execute("INSERT INTO mytable VALUES('Item 1',10,9.99")

#4. commit changes
conn.commit()

#5. close connection
conn.close