from kivy.lang import Builder
from kivymd.app import MDApp
from wordle import WordCheck
from spellchecker import SpellChecker
#from csv import reader
import random
#from kivy.core.spelling import Spelling

class MainApp(MDApp):
    def build(self):
        self.title = "Word Guess"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.build_label_button_array()
        self.get_answer_from_file()
        self.spell = SpellChecker()
#        return Builder.load_file('layout.kv')
        return super().build()

    guesses_submitted = 0
    max_guesses = 6
    guess = ""
    game_over = False
    current_letter = 0
    invalid_word = False

    label_array = []
    button_array = []

    # function to switch from light to dark theme, or vice versa
    def change_theme(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    # function to initialise button and letter arrays so we can set colours etc
    def build_label_button_array(self):
        for i in range(0,30):
          exec(f'self.label_array.append(self.root.ids.letter{i+1})')

        for i in range(0,26):
          exec(f'self.button_array.append(self.root.ids.button{i+1})')

    # randomly select a word from answer file
    def get_answer_from_file(self):
        #answerlist = pd.read_csv("answerlist.csv",header=None)
        #answerlist = answerlist.sample(n=1)
        #self.answer = answerlist.values[0][0]

        with open("answerlist.csv", "r") as csv_file:
            words = csv_file.read().split()
            self.answer = random.choice(words)

    # function to print each submitted letter onto next available label
    def write_label(self,mytext):
        if self.game_over != True:
            for i in range(self.guesses_submitted * 5,(self.guesses_submitted * 5) + 5):
                if self.label_array[i].text == "":
                    self.label_array[i].text = mytext
                    self.current_letter = self.current_letter + 1
                    break

    # function to reset everything after end of game
    def play_again(self):
        for i in range(0,30):
            self.label_array[i].text = ""
            self.label_array[i].background_color = (.7,.7,.7, 1)

        for j in range(0,26):
            self.button_array[j].text_color = (1, 1, 1, 1)

        self.guesses_submitted = 0
        self.guess = ""
        self.game_over = False
        self.current_letter = 0
        self.invalid_word = False
        self.root.ids.restart_button.disabled = True
        self.root.ids.feedback.text = ""

        # get a new word
        self.get_answer_from_file()

    # function to clear letters - only want to go back as far as start of current line
    def backspace(self):
        # after an invalid entry, need to reset background colour of letters to original grey, and reset feedback message
        if self.invalid_word == True:
            for i in range(self.current_letter-5,self.current_letter):
                self.label_array[i].background_color = (.7,.7,.7,1)
            self.invalid_word = False
            self.root.ids.feedback.text = ""

        # reset each letter in turn
        if self.current_letter > (self.guesses_submitted * 5):
            self.label_array[self.current_letter-1].text = ""
            self.current_letter = self.current_letter - 1

    # function triggered by pressing 'enter' button. Takes submitted letters, forms a word from them, then calls function to check it
    def enter(self):
        # need to ensure we are at the end of a line
        if self.current_letter % 5 == 0 and self.current_letter != 0 and self.current_letter > self.guesses_submitted * 5:
            self.guess = ""
            guess_letter_list = []
            for i in range(self.current_letter-5,self.current_letter):
                guess_letter_list.append(self.label_array[i].text)
            
            self.guess = ''.join(guess_letter_list).lower()

            # check word is a valid guess, and if so, check to see how it compares with the answer
            if (self.check_guess_valid(self.guess)):
                self.compare_guess()
            else:
                self.invalid_guess()

    # loop round until word found or max guesses exhausted
    def compare_guess(self):
        self.guesses_submitted = self.guesses_submitted + 1

        # create WordCheck instance, where answer and guess are compared
        # string returned contains certain characters if letter is correct or in wrong place
        myWordCheck = WordCheck()
        check_value = myWordCheck.check_guess(self.guess, self.answer)

        for i in range((self.guesses_submitted * 5) - 5, self.guesses_submitted * 5):
            check_index = i - (self.guesses_submitted * 5)
            # if letter is correct and in right place, change bgcolor to green
            if check_value[check_index] =='X':
                self.label_array[i].background_color = (102/255, 205/255, 0, 1)
            # otherwise, if correct but in wrong place, set it to yellow
            elif check_value[check_index] =='@':
                self.label_array[i].background_color = (1, 191/255, 0, 1)
            else:
                # letter not in word, so change bgcolor to dark grey 
                self.label_array[i].background_color = (.3,.3,.3,1)

                # then set colour of button with that text value to different colour
                for j in range(0,26):
                    if self.button_array[j].text == self.guess[check_index].upper():
                        self.button_array[j].text_color = (.7, .7, .7, 1)

        # After going through whole or guess, reset bgcolor / text colour of buttons to original values if any letters 
        # are found on the word (i.e. if background is green or yellow). This is required as guessing same letter more 
        # than once can cause buttons to be incorrectly greyed out
        for k in range((self.guesses_submitted * 5) - 5, self.guesses_submitted * 5):
            if self.label_array[k].background_color == [102/255, 205/255, 0, 1] or self.label_array[k].background_color == [1, 191/255, 0, 1]:
                # change colour of button with that text value to different colour
                for l in range(0,26):
                    if self.button_array[l].text == self.label_array[k].text.upper():
                        self.button_array[l].text_color = (1, 1, 1, 1)
        
        # if all letters are matched, display message and end game
        if check_value == 'XXXXX':
            self.game_over = True
            self.root.ids.feedback.text = "You win!"
            self.root.ids.restart_button.disabled = False
            
        # otherwise check to see if all guesses are exhausted and end game if so
        else:
            if self.guesses_submitted == self.max_guesses:
                self.root.ids.feedback.text = "Unlucky! Answer was " + self.answer.upper()
                self.game_over = True
                self.root.ids.restart_button.disabled = False

    def check_guess_valid(self,guess):
        if guess in self.spell:
        #if self.spell.check(guess):
            return True
        else:
            return False

    def invalid_guess(self):
        self.invalid_word = True
        self.root.ids.feedback.text = "Guess invalid! Please submit a valid word"
        for i in range(self.current_letter-5,self.current_letter):
            self.label_array[i].background_color = (1,0,0,1)

if __name__ == "__main__":
    MainApp().run()