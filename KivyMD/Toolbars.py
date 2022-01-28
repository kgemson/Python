from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
Window.size = (600,600)

class ToolbarsApp(MDApp):
    def build(self):
        self.title = "Tutorial"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('Toolbars.kv')

    # Alternative call method - 
    # Run will automatically import 'Toolbars.kv' as it has the same name as the class (minus the 'app' part)
    #def build(self):
    #    self.title = "Tutorial"
    #    self.theme_cls.theme_style = "Light"
    #    return

if __name__ == "__main__":
    app = ToolbarsApp()
    app.run()

