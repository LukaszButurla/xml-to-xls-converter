from kivy.app import App
from kivy.core.window import Window

class MainWindow(App):
    
    Window.size = 1400, 900
    
    
if __name__ == "__main__":
    MainWindow().run()