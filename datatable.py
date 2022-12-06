from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.label import Label

class DataTableWithData(MDDataTable):
    
    def __init__(self, screen):

        self.screen = screen
        self.create_data_table()
        self.add_datatable_to_screen()   
        self.add_label_with_vat_price()
        
    def add_values_from_file(self, pathToRead):
        
        
        with open(pathToRead, "r", encoding="UTF-8") as fileRead:

                lines = fileRead.read()
                    
                amountOfSubjectsStart = lines.find("<LiczbaPozycji>")
                amountOfSubjectsEnd = lines.find("</LiczbaPozycji>")
                amountOfSubjects = lines[amountOfSubjectsStart+15:amountOfSubjectsEnd]
                    
                self.clear_data_table()
                self.priceVatAll = 0
                    
                try:
                    
                    for subject in range(int(amountOfSubjects)):

                    
                        subjectStart = lines.find("<Pozycja>")
                        subjectEnd = lines.find("</Pozycja>")
                        subject = lines[subjectStart:subjectEnd]
                            
                        indexStart = subject.find("<Indeks>")
                        indexEnd = subject.find("</Indeks>")
                        index = subject[indexStart+8:indexEnd]
                        
                        descriptionFirstStart = subject.find("<Opis>")
                        descriptionFirstEnd = subject.find("</Opis>")
                        descriptionFirst = subject[descriptionFirstStart+6:descriptionFirstEnd]
                        
                        descriptionSecondStart = subject.find("<Opis1>")
                        descriptionSecondEnd = subject.find("</Opis1>")
                        descriptionSecond = subject[descriptionSecondStart+7:descriptionSecondEnd]
                        
                        description = "{}\n{}".format(descriptionFirst, descriptionSecond)
                        
                        amountStart = subject.find("<Ilosc>")
                        amountEnd = subject.find("</Ilosc>")
                        amount = subject[amountStart+7:amountEnd]
                        
                        priceStart = subject.find("<Cena>")
                        priceEnd = subject.find("</Cena>")
                        price = subject[priceStart+6:priceEnd]
                        
                        vatStart = subject.find("<Procent>")                        
                        vatEnd = subject.find("</Procent>")
                        vat = subject[vatStart+9:vatEnd]
                        
                        priceVatStart = subject.find("<WartoscVAT>")
                        priceVatEnd = subject.find("</WartoscVAT>")
                        priceVat = subject[priceVatStart+12:priceVatEnd]
                        
                        if "P" in vat.upper():
                            vat = vat[1:]
                            
                        priceNettoStart = subject.find("<WartoscNetto>")
                        priceNettoEnd = subject.find("</WartoscNetto>")
                        priceNetto = subject[priceNettoStart+14:priceNettoEnd]                                           
                            
                        lines = lines[subjectEnd+10:]
                        
                        self.priceVatAll += float(priceVat)
                            
                        self.add_row(index, description, amount, price, vat, priceVat, priceNetto)
                                            
                        
                    else:
                        self.labelVatPrice.text = "Podsumowanie wartość vat:\n{:.2f}".format(self.priceVatAll)
                except:
                    print("Error")
        
    def add_row(self, index, description, amount, pricePerPiece, vat, priceVat, priceNetto):
        self.table.add_row((index, description, amount, pricePerPiece, vat, priceVat, priceNetto))   
        
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
                ("Wartość vat", (45)),
                ("Wartość netto", (45))])
        
    def add_datatable_to_screen(self):
        self.screen.add_widget(self.table)
        
    def add_label_with_vat_price(self):
        
        self.labelVatPrice = Label(
            text = "Podsumowanie wartość vat:",
            halign = "left",
            size_hint = (0.2, 0.02),
            pos_hint = {"center_x": 0.75, "center_y": 0.07},
            color = (0, 0, 0, 1),
            font_size = 18)
        
        self.screen.add_widget(self.labelVatPrice)