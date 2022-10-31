from functools import partial
from tkinter import Button
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
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
                ("Ilość", dp(50))
            ])
    def add_widgets_to_screen(self):
        self.screen.add_widget(self.dataTable)
        self.screen.add_widget(self.btnAdd)
    
    def build(self):
        Window.size = 1400, 900     
        self.screen = Screen()
        self.btnAdd = Button(text = "Add", size_hint = (0.2, 0.2), pos_hint = {"center_x": 0.9, "center_y": 0.9})
        self.btnAdd.bind(on_press = partial(self.add_row, "Nazwa", "cena", "ilosc"))
        self.create_data_table()
        self.add_widgets_to_screen()
        return self.screen
    

    
if __name__ == "__main__":
    MainWindow().run()