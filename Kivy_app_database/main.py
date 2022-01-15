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
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior

Builder.load_file('design.kv')

# Screens defined in kivy must be defined as classes within python file
# Each inherits from 'Screen' class
# RootWidget inherits from 'screenmanager' as it is highest level of hierarchy
# 'pass' means do nothing, often used for stub programs
class LoginScreen(Screen):
    def login_user(self, uname, pword):
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.login_feedback.text = ""

        with open("users.json","r") as file:
            users=json.load(file)
        
        # if blank values supplied, prompt for real values
        if uname=='' or pword=='':
            self.ids.login_feedback.text = "Please supply a userid and password"
            self.manager.current = "login_screen_success"
        # if supplied, check if supplied username is a key in the users file
        else:
            if uname in users and users[uname]['password'] == pword:
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
                with open("users.json","r") as file:
                    users=json.load(file)

                # first, check to see if user already exists
                if uname in users:
                    self.ids.login_feedback.text = "Username already exists - please try another"
                    self.ids.username.text = ""
                    self.ids.password.text = ""
                    self.ids.password_confirm.text = ""
                else:
                    #add a new user to this list as a dictionary element with key 'uname'
                    # take current time from 'datetime' class and format the output
                    users[uname] = {'username': uname, 'password': pword,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

                    with open("users.json","w") as file:
                        json.dump(users, file)
                    
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
