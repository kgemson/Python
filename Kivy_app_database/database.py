import psycopg2 as ps2
from datetime import datetime

class Database:

    def __init__(self,dbconn):
        self.conn=ps2.connect(dbconn)
        
    def open_connection(self):
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def user_exists(self,uname):
        self.cur.execute("SELECT COUNT(1) WHERE EXISTS(SELECT username FROM public.kivy_app_users WHERE username = %s)",(uname,))
        res=self.cur.fetchone()
        if res[0]==1:
            return True
        else:
            return False

    def check_user_credentials(self,uname,pword):
        self.cur.execute("SELECT COUNT(1) WHERE EXISTS(SELECT username FROM public.kivy_app_users WHERE username = %s and password = %s)",(uname,pword))
        res=self.cur.fetchone()
        if res[0]==1:
            return True
        else:
            return False

    def add_new_user(self,uname,pword):
        self.cur.execute("INSERT INTO public.kivy_app_users(username,password,created) VALUES (%s,%s,CURRENT_TIMESTAMP)",(uname,pword))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()