from time import thread_time_ns
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to binary converter"
            self.input.hint_text = "Enter a decimal number: "
            self.input.text = ""
            self.label.text = ""
            self.converted.text = ""
     
        else:
            self.state = 0
            self.toolbar.title = "Binary to decimal converter"
            self.input.hint_text = "Enter a binary number: "
            self.input.text = ""
            self.label.text = ""
            self.converted.text = ""

    def convert(self, args): #'Button' code always requires two parms - 'self' and an 'args'
        # need to cater for user inputting invalid data
        try:
            # need to distinguish between floating point and whole numbers. First, whole numbers...
            if '.' not in self.input.text:
                if self.state == 0:
                    #convert binary to decimal
                    val = int(self.input.text,2)
                    self.label.text = "In decimal is: "
                    self.converted.text = str(val)
                else:
                    #convert decimal to binary
                    val = bin(int(self.input.text))[2:]  # bin values always start with '0b', so need to skip first two chars
                    self.label.text = "In binary is: "
                    self.converted.text = val

            # then floating point numbers...
            else:
                whole,frac = self.input.text.split('.')
                
                if self.state == 0 :
                    #convert binary to decimal
                    whole = int(whole,2)
                    
                    floating = 0
                    for idx,digit in enumerate(frac):
                        # floating points calculated by multiplying each digit by 2 to the power of (digit position * -1) and adding
                        # (index starts at zero so need to add 1)
                        floating += int(digit)*2**(-(idx+1))

                    self.label.text = "In decimal is: "
                    self.converted.text = str(whole + floating)
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

                    self.label.text = "In binary is: "
                    self.converted.text = str(whole +"."+"".join(floating))
        except ValueError:
            self.converted.text = ""
            if self.state == 0:
                self.label.text = "Please enter a valid binary number"
            else:
                self.label.text = "Please enter a valid decimal number"


    def build(self):
        screen = MDScreen()
        self.state = 0

        #UI Widgets go here
        self.toolbar = MDToolbar(title="Binary To Decimal converter")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x:self.flip()]]
        screen.add_widget(self.toolbar)
        
        screen.add_widget(Image(source="logo.png",pos_hint = {"center_x": 0.5,"center_y": 0.7}))

        self.input = MDTextField(
            hint_text = "Enter a binary number: ",
            text = "",
            halign="center",
            size_hint=(0.8,1),
            pos_hint = {"center_x": 0.5,"center_y": 0.45},
            font_size = 45
        )
        screen.add_widget(self.input)

        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5,"center_y": 0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5,"center_y": 0.3},
            theme_text_color = "Primary",
            font_style = "H3",
            font_size = 45
        )
        
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        #Convert button
        screen.add_widget(MDFillRoundFlatButton(
                text="Convert",
                font_size = 17,
                pos_hint = {"center_x": 0.5,"center_y": 0.15},
                on_press = self.convert
            )
        )

        return screen        

if __name__ == '__main__':
    ConverterApp().run()