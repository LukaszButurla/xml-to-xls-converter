class Converter:
    
    def __init__(self, screen, datatableClass):
        self.screen = screen
        self.datatableClass = datatableClass
            
    def open_file_to_read(self, pathToRead):
        
        with open(pathToRead, "r", encoding="UTF-8") as fileRead:

            lines = fileRead.read()
            
            amountOfSubjectsStart = lines.find("<LiczbaPozycji>")
            amountOfSubjectsEnd = lines.find("</LiczbaPozycji>")
            amountOfSubjects = lines[amountOfSubjectsStart+15:amountOfSubjectsEnd]
            
            for subject in range(int(amountOfSubjects)):
                
                try:
            
                    subjectStart = lines.find("<Pozycja>")
                    subjectEnd = lines.find("</Pozycja>")
                    subject = lines[subjectStart:subjectEnd]
                    
                    indexStart = subject.find("<Indeks>")
                    indexEnd = subject.find("</Indeks>")
                    index = subject[indexStart+8:indexEnd]
                    
                    amountStart = subject.find("<Ilosc>")
                    amountEnd = subject.find("</Ilosc>")
                    amount = subject[amountStart+7:amountEnd]
                    
                    priceStart = subject.find("<Cena>")
                    priceEnd = subject.find("</Cena>")
                    price = subject[priceStart+6:priceEnd]
                    
                    lines = lines[subjectEnd+10:]
                    
                    self.datatableClass.add_row(index, price, amount)
                
                except:
                    print("Error")
            
            