from sys import path
from kivy.config import Config

MAX_SIZE = (450, 600)
Config.set('graphics', 'width', MAX_SIZE[0])
Config.set('graphics', 'height', MAX_SIZE[1])

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import glob, random
from pathlib import Path
from hoverable import HoverBehavior
#from nodatabase import Database
from database import Database

Builder.load_file('design.kv')

dbconn="dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'"
#db = Database()
db = Database(dbconn)

# Screens defined in kivy must be defined as classes within python file
# Each inherits from 'Screen' class
# RootWidget inherits from 'screenmanager' as it is highest level of hierarchy
# 'pass' means do nothing, often used for stub programs
class LoginScreen(Screen):
    def login_user(self, uname, pword):
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.login_feedback.text = ""

        db.open_connection()
        
        # if blank values supplied, prompt for real values
        if uname=='' or pword=='':
            self.ids.login_feedback.text = "Please supply a userid and password"
        # if supplied, check if supplied username is a key in the users file
        else:
            if db.check_user_credentials(uname,pword):
                self.ids.login_feedback.text = ""
                self.ids.username.text = ""
                self.ids.password.text = ""
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_feedback.text = "Incorrect username or password - please retry"
                self.ids.username.text = ""
                self.ids.password.text = ""

    def sign_up(self):
        self.manager.current = "sign_up_screen"

class SignupScreen(Screen):
    def add_user(self, uname, pword, pword_confirm):
        if uname=="" or pword=="" or pword_confirm=="":
            self.ids.login_feedback.text = "Please enter values in all fields"
            self.ids.username.text = ""
            self.ids.password.text = ""
            self.ids.password_confirm.text = ""
        else:
            if pword == pword_confirm: 
                db.open_connection()

                # first, check to see if user already exists
                if db.user_exists(uname):
                    self.ids.login_feedback.text = "Username already exists - please try another"
                    self.ids.username.text = ""
                    self.ids.password.text = ""
                    self.ids.password_confirm.text = ""
                else:
                    #add a new user to this list as a dictionary element with key 'uname'
                    # take current time from 'datetime' class and format the output
                    db.add_new_user(uname, pword)
                    
                    # on success, switch to confirmation screen
                    self.ids.login_feedback.text = ""
                    self.ids.username.text = ""
                    self.ids.password.text = ""
                    self.ids.password_confirm.text = ""
                    self.manager.current = "sign_up_screen_success"
            else:
                self.ids.login_feedback.text = "Passwords do not match. Please retry."
                self.ids.password.text = ""
                self.ids.password_confirm.text = ""
    
    def return_to_login(self):
        self.ids.login_feedback.text = ""
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.password_confirm.text = ""
        self.manager.current = "login_screen"

class SignupScreenSuccess(Screen):
    def return_to_signin_screen(self):
        # after successful signup, return to login screen
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def logout_user(self):
        self.manager.transition.direction = 'left'
        self.ids.quotelabel.text = ""
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()

        # check which filenames are available
        available_feelings = glob.glob('quotes/*txt')
        # extract just the 'stem' from those
        available_feelings = [Path(filename).stem for filename in available_feelings]

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt",encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quotelabel.text = random.choice(quotes)
        else:
            self.ids.quotelabel.text = "Try another feeling"

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):    #inherited from App parent
        return RootWidget()
    
if __name__=="__main__":
    MainApp().run()
