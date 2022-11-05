from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class DataTableWithData(MDDataTable):
    
    def __init__(self, screen):

        self.screen = screen
        self.create_data_table()
        self.add_datatable_to_screen()   
        
    def add_row(self, index, price, amount):
        self.table.add_row((index, price, amount))   
    
    
    def create_data_table(self):
        
        self.table = MDDataTable(
            use_pagination = True,
            rows_num = 50,
            size_hint = (0.9, 0.85),
            pos_hint = {"center_x" : 0.5, "center_y" : 0.47},
            column_data = [
                ("Nazwa", dp(100)),
                ("Kwota", dp(50)),
                ("Ilość", dp(50))])
        
    def add_datatable_to_screen(self):
        self.screen.add_widget(self.table)