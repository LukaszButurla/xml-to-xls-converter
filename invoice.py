import csv
import os

class Invoice:
    
    def __init__(self, datatable):
        self.datatableClass = datatable

    def open_file_to_read(self, pathToRead, directoryToSave):
            
            
            with open(pathToRead, "r", encoding="UTF-8") as fileRead:

                lines = fileRead.read()
                    
                amountOfSubjectsStart = lines.find("<LiczbaPozycji>")
                amountOfSubjectsEnd = lines.find("</LiczbaPozycji>")
                amountOfSubjects = lines[amountOfSubjectsStart+15:amountOfSubjectsEnd]
                    
                self.listOfData = []
                self.datatableClass.clear_data_table()
                    
                try:
                    
                    for subject in range(int(amountOfSubjects)):

                    
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
                        self.listOfData.append([index, price, amount])
                                            
                        
                    else:
                        file = os.path.basename(pathToRead)
                        fileDot = file.find(".")
                        fileName = file[:fileDot] + ".xls"
                        pathToSave = os.path.join(directoryToSave, fileName)                   
                        
                        self.write_to_file(pathToSave)
                except:
                    print("Error")
                        
    def write_to_file(self, pathToSave):
            
        try:
            
            with open(pathToSave, "w+", encoding="utf-8", newline="") as f:
                        
                writer = csv.writer(f)
                
                for data in self.listOfData:
                    writer.writerow(data)
                        
        except:
            f.close()
            print("Error save")