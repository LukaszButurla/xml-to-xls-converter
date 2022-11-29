import csv
import os
from invoice import Invoice
from converterPriceList import Convert_to_price_list

class Converter:
    
    def __init__(self, screen, datatableClass):
        self.screen = screen
        self.datatableClass = datatableClass
        self.invoice = Invoice(datatableClass)
        self.priceList = Convert_to_price_list()
        
        
    def convert_to_invoice(self, pathToRead, pathToSave):
        self.invoice.open_file_to_read(pathToRead, pathToSave)
            
    def convert_files(self, pathToRead, pathToSave):
        self.convert_to_invoice(pathToRead, pathToSave)
        self.priceList.get_values_from_invoice(pathToRead, pathToSave)
    
            
        
        
            
            