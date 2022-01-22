import json
from datetime import datetime

class Database():

    def __init__(self):
        pass
    
    def open_connection(self):
        with open("users.json","r") as file:
            self.users=json.load(file)

    def user_exists(self,uname):
        return uname in self.users

    def check_user_credentials(self,uname,pword):
        return uname in self.users and self.users[uname]['password'] == pword

    def add_new_user(self,uname,pword):
        self.users[uname] = {'username': uname, 'password': pword,'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json","w") as file:
            json.dump(self.users, file)