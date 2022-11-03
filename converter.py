class Converter:
    
    def open_file_to_read(self, pathToRead):
        
        with open(pathToRead, "r", encoding="UTF-8") as fileRead:

            lines = fileRead.readlines()
            print(lines)