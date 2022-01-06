import psycopg2 as ps2

class Database:

    # Define constructor for database objects
    # when object is instantiated, 'self' is passed over so must be included in constructor
    # any additional paramateres are added aftwerwards
    def __init__(self,dbconn):
        self.conn=ps2.connect(dbconn)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    # Define the following founctions to be implemented in GU script - 
    # "View all","Search entry","Add entry","Update","Delete","Close"
    def view_all(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search_entry(self,title="", author="", year="", isbn=""): #supplying empty values to cater for the user entering nothing in those fields
        if year=="":
            year=-1
    
        if isbn=="":
            isbn=-1
        
        self.cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def add_entry(self,title, author, year, isbn):
        self.cur.execute("SELECT COALESCE(MAX(id),0) FROM book")
        my_id=self.cur.fetchone()[0]+1
        self.cur.execute("INSERT INTO book (id,title, author, year, isbn) VALUES (%s,%s,%s,%s,%s)",(my_id,title, author, year, isbn))
        self.conn.commit()

    def update_entry(self,id,title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title, author, year, isbn,id))
        self.conn.commit()

    def delete_entry(self,id):
        self.cur.execute("DELETE FROM book WHERE id = %s",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()