from functools import partial
from tkinter import Button
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp


class MainWindow(MDApp):
    
    def add_row(self, name, price, amount, button):
        
        self.dataTable.add_row((name, price, amount))
        # return super().on_dismiss()
        
    def create_data_table(self):
        self.dataTable = MDDataTable(
            use_pagination = True,
            rows_num = 100,
            size_hint = (0.9, 0.8),
            pos_hint = {"center_x" : 0.5, "center_y" : 0.5},
            column_data = [
                ("Nazwa", dp(100)),
                ("Kwota", dp(50)),
                ("Ilość", dp(50))])

    def create_button_to_select_directory_to_open(self):
        self.labelSelectDirectoryInfo = Label(
            text = "Ścieżka pliku do otwarcia:",
            size_hint = (0.2, 0.02),
            pos_hint = {"center_x": 0.12, "center_y": 0.97},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.labelSelectDirectory = Label(
            text = r"C:\test\test\test\test.xml",
            size_hint = (0.3, 0.02),
            pos_hint = {"center_x": 0.12, "center_y": 0.93},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.btnSelectDirectoryToOpen = Button(
            text = "Wybierz",
            size_hint = (0.1, 0.05),
            pos_hint = {"center_x": 0.35, "center_y": 0.93})
        
    def create_button_to_select_directory_to_save(self):
        self.labelSaveDirectoryInfo = Label(
            text = "Ścieżka pliku do zapisu:",
            size_hint = (0.2, 0.02),
            pos_hint = {"center_x": 0.6, "center_y": 0.97},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.labelSaveDirectory = Label(
            text = r"C:\test\test\test\test.xml",
            size_hint = (0.3, 0.02),
            pos_hint = {"center_x": 0.6, "center_y": 0.93},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.btnSelectDirectoryToSave = Button(
            text = "Wybierz",
            size_hint = (0.1, 0.05),
            pos_hint = {"center_x": 0.83, "center_y": 0.93})
        
    def create_button_to_convert(self):
        self.btnConvert = Button(
            text = "Konwertuj",
            size_hint = (0.3, 0.075),
            pos_hint = {"center_x": 0.5, "center_y": 0.05}
        )
            
    def add_widgets_to_screen(self):
        self.screen.add_widget(self.dataTable)
        self.screen.add_widget(self.btnSelectDirectoryToOpen)
        self.screen.add_widget(self.labelSelectDirectoryInfo)
        self.screen.add_widget(self.labelSelectDirectory)
        self.screen.add_widget(self.labelSaveDirectory)
        self.screen.add_widget(self.labelSaveDirectoryInfo)
        self.screen.add_widget(self.btnSelectDirectoryToSave)
        self.screen.add_widget(self.btnConvert)
    
    def build(self):
        Window.size = 1400, 900     
        self.screen = Screen()
        # self.btnAdd = Button(text = "Add", size_hint = (0.2, 0.2), pos_hint = {"center_x": 0.9, "center_y": 0.9})
        # self.btnAdd.bind(on_press = partial(self.add_row, "Nazwa", "cena", "ilosc"))
        self.create_data_table()
        self.create_button_to_select_directory_to_open()
        self.create_button_to_select_directory_to_save()
        self.create_button_to_convert()
        self.add_widgets_to_screen()
        return self.screen
    

    
if __name__ == "__main__":
    MainWindow().run()