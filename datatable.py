from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class DataTableWithData(MDDataTable):
    
    def __init__(self, screen):

        self.screen = screen
        self.create_data_table()
        self.add_datatable_to_screen()   
        
    def add_row(self, index, description, amount, pricePerPiece, vat, priceNetto):
        self.table.add_row((index, description, amount, pricePerPiece, vat, priceNetto))   
        
    def clear_data_table(self):
        
        tableLen = len(self.table.row_data)
        for i in range(tableLen):
            self.table.remove_row(self.table.row_data[-1])
    
    
    def create_data_table(self):
        
        self.table = MDDataTable(
            use_pagination = True,
            rows_num = 50,
            size_hint = (0.9, 0.8),
            pos_hint = {"center_x" : 0.5, "center_y" : 0.5},
            column_data = [
                ("Index", dp(40)),
                ("Opis", dp(80)),
                ("Ilość", dp(30)),
                ("Cena jednostkowa", (40)),
                ("vat", (30)),
                ("Wartość netto", (45))])
        
    def add_datatable_to_screen(self):
        self.screen.add_widget(self.table)