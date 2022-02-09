from kivy.lang import Builder
from kivymd.app import MDApp
import random

class MainApp(MDApp):
    def build(self):
        self.title = "Noughts & Crosses"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layout.kv')

    to_start = "X"
    game_over = False
    X_score = 0
    O_score = 0
    empty_squares=[]

    # carry out steps to end game
    def end_game(self, btn_a, btn_b, btn_c):
        self.game_over = True
        btn_a.color = "red"
        btn_b.color = "red"
        btn_c.color = "red"

        self.disable_all_buttons()
        
        self.root.ids.score.text = f"{btn_a.text} wins!"
    
        if btn_a.text == 'X':
            self.X_score = self.X_score + 1
            self.to_start = "O"
        else:
            self.O_score = self.O_score + 1
            self.to_start = "X"

        self.root.ids.game_score.text = f"X wins: {self.X_score}  |  O wins: {self.O_score}"
        self.root.ids.restart.text = "Play again"

    def test(self):
        if self.game_over == True & self.game_over == True:
            pass

    # if game over and no winner, take action
    def no_winner(self):
        if self.game_over == False and \
            self.root.ids.button1.disabled == True and \
            self.root.ids.button2.disabled == True and \
            self.root.ids.button3.disabled == True and \
            self.root.ids.button4.disabled == True and \
            self.root.ids.button5.disabled == True and \
            self.root.ids.button6.disabled == True and \
            self.root.ids.button7.disabled == True and \
            self.root.ids.button8.disabled == True and \
            self.root.ids.button9.disabled == True:
                self.root.ids.score.text = "It's a tie - click 'Restart' to play again"
                self.game_over = True

    # check to see if game has been won, and end game if so
    def checkwin(self):
        # across
        if self.check_line(self.root.ids.button1,self.root.ids.button2,self.root.ids.button3):
            self.end_game(self.root.ids.button1,self.root.ids.button2,self.root.ids.button3)
        elif self.check_line(self.root.ids.button4,self.root.ids.button5,self.root.ids.button6):
            self.end_game(self.root.ids.button4,self.root.ids.button5,self.root.ids.button6)
        elif self.check_line(self.root.ids.button7,self.root.ids.button8,self.root.ids.button9):
            self.end_game(self.root.ids.button7,self.root.ids.button8,self.root.ids.button9)
        
        # down
        elif self.check_line(self.root.ids.button1,self.root.ids.button4,self.root.ids.button7):
            self.end_game(self.root.ids.button1,self.root.ids.button4,self.root.ids.button7)
        elif self.check_line(self.root.ids.button2,self.root.ids.button5,self.root.ids.button8):
            self.end_game(self.root.ids.button2,self.root.ids.button5,self.root.ids.button8)
        elif self.check_line(self.root.ids.button3,self.root.ids.button6,self.root.ids.button9):
            self.end_game(self.root.ids.button3,self.root.ids.button6,self.root.ids.button9)

        # diagonal
        elif self.check_line(self.root.ids.button1,self.root.ids.button5,self.root.ids.button9):
            self.end_game(self.root.ids.button1,self.root.ids.button5,self.root.ids.button9)
        elif self.check_line(self.root.ids.button3,self.root.ids.button5,self.root.ids.button7):
            self.end_game(self.root.ids.button3,self.root.ids.button5,self.root.ids.button7)

        # no-one wins...
        else:
            self.no_winner()

    def check_line(self, btn_a, btn_b, btn_c):
        return btn_a.text != "" and btn_a.text == btn_b.text and btn_a.text == btn_c.text

    def pick_O_square(self):
        # find which squares are still empty
        self.empty_squares = []
        for i in range(0,9):
            exec(f"self.check_disabled(self.root.ids.button{i+1},self.empty_squares)")

        # now randomly select one, if there are any
        if len(self.empty_squares)!= 0:
            btn = random.choice(self.empty_squares)
            btn.text = "O"
            btn.disabled = True

    def check_disabled(self,btn,empty_squares):
        if btn.disabled == False:
            empty_squares.append(btn)

    # disable all the buttons
    def disable_all_buttons(self):
        for i in range(0,9):
            exec(f"self.root.ids.button{i+1}.disabled = True")

    def press_button(self,btn):
        # set X's chosen square, and check to see if that has ended game
        btn.text = "X"
        btn.disabled = True
        self.root.ids.score.text = "O's turn!"

        self.checkwin()

        # if not, O chooses a square and checks if that has ended game
        if self.game_over != True:
            self.pick_O_square()
            self.root.ids.score.text = "X's turn!"
            self.checkwin()

    def reset(self):
        self.game_over = False
        self.root.ids.restart.text = "Restart"

        for i in range(0,9):
            exec(f"self.root.ids.button{i+1}.text = \"\"")
            exec(f"self.root.ids.button{i+1}.disabled = False")
            exec(f"self.root.ids.button{i+1}.color = text = \"green\"")

        self.root.ids.score.text = f"{self.to_start} goes first!"

        if self.to_start == 'O':
            self.pick_O_square()
            self.root.ids.score.text = "X's turn!"

if __name__ == '__main__':
    MainApp().run()