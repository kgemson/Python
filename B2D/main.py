from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
#from kivy.uix.image import Image
#from kivymd.uix.button import MDFillRoundFlatButton
#from kivymd.uix.textfield import MDTextField
#from kivymd.uix.label import MDLabel
#from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window

# set window size
#Window.size=(1080,2340)

class MainScreen(MDScreen):
    state = 0

    def flip(self):
        if self.state == 0:
            self.state = 1
            self.ids.toolbar.title = "Decimal to binary converter"
            self.ids.toplabel.text = "Enter a decimal number:"
            self.ids.input.hint_text = " : "
            self.ids.input.text = ""
            self.ids.bottomlabel.text = ""
            self.ids.converted.text = ""
        else:
            self.state = 0
            self.ids.toolbar.title = "Binary to decimal converter"
            self.ids.toplabel.text = "Enter a binary number:"
            self.ids.input.hint_text = " : "
            self.ids.input.text = ""
            self.ids.bottomlabel.text = ""
            self.ids.converted.text = ""

    def convert(self): #'Button' code always requires two parms - 'self' and an 'args' (apparently not true if using .kv file)
        # need to cater for user inputting invalid data
        try:
            # need to distinguish between floating point and whole numbers. First, whole numbers...
            if '.' not in self.ids.input.text:
                if self.state == 0:
                    #convert binary to decimal
                    val = int(self.ids.input.text,2)
                    self.ids.bottomlabel.text = "in decimal is: "
                    self.ids.converted.text = str(val)
                else:
                    #convert decimal to binary
                    val = bin(int(self.ids.input.text))[2:]  # bin values always start with '0b', so need to skip first two chars
                    self.ids.bottomlabel.text = "in binary is: "
                    self.ids.converted.text = val

            # then floating point numbers...
            else:
                whole,frac = self.ids.input.text.split('.')
                
                if self.state == 0 :
                    #convert binary to decimal
                    whole = int(whole,2)
                    
                    floating = 0
                    for idx,digit in enumerate(frac):
                        # floating points calculated by multiplying each digit by 2 to the power of (digit position * -1) and adding
                        # (index starts at zero so need to add 1)
                        floating += int(digit)*2**(-(idx+1))

                    self.ids.bottomlabel.text = "In decimal is: "
                    self.ids.converted.text = str(whole + floating)
                else:
                    #convert decimal to binary
                    decimal_places = 10 # need to set max decimal places so we don't get infinite values, e.g. 1/3
                    whole = bin(int(whole))[2:] # bin values always start with '0b', so need to skip first two char 
                    
                    frac = float("0."+frac)
                    floating = []
                    
                    # floating points calculated by multiplying fraction by 2 repeatedly - if result < 1, we store '0'.
                    # if result > 1, we store '1' and reduce result by 1
                    # we repeat this until doubling gives us zero
                    for i in range(decimal_places):
                        if frac*2 < 1.0:
                            floating.append('0')
                            frac*=2
                        elif frac*2 > 1.0:
                            floating.append('1')
                            frac = (frac*2) - 1
                        elif frac*2 == 1.0:
                            floating.append('1')
                            break

                    self.ids.bottomlabel.text = "In binary is: "
                    self.ids.converted.text = str(whole +"."+"".join(floating))
        except ValueError:
            self.ids.converted.text = ""
            if self.state == 0:
                self.ids.bottomlabel.text = "Please enter a valid binary number"
                self.ids.input.text = ""
            else:
                self.ids.bottomlabel.text = "Please enter a valid decimal number"
                self.ids.input.text = ""
    
class ConverterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('Converter.kv')

if __name__ == '__main__':
    ConverterApp().run()