from functools import partial
from tkinter import Button
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from tkinter import filedialog
import os

from datatable import DataTableWithData
from converter import Converter


class MainWindow(MDApp):
    
            
    def select_file_window(self, btn):
        self.selectedFile = filedialog.askopenfilename(filetypes=[("Text files", "xml")])
        self.labelSelectDirectory.text = self.selectedFile
        
    def select_directory_to_save_window(self, btn):
        self.selectedDirectory = filedialog.askdirectory()
        self.labelSaveDirectory.text = self.selectedDirectory
    
    def Convert(self, btn):
        
        if self.selectedFile.endswith(".xml") and os.path.exists(self.selectedDirectory):
        
            self.converter.convert_files(self.selectedFile, self.selectedDirectory)
        
    def create_button_to_convert(self):
        self.btnConvert = Button(
            text = "Konwertuj",
            size_hint = (0.3, 0.075),
            pos_hint = {"center_x": 0.5, "center_y": 0.05}
        )
        self.btnConvert.bind(on_press = partial(self.Convert))

    def create_button_to_select_directory_to_open(self):
        self.labelSelectDirectoryInfo = Label(
            text = "Ścieżka pliku do otwarcia:",
            size_hint = (0.2, 0.02),
            pos_hint = {"center_x": 0.12, "center_y": 0.97},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.labelSelectDirectory = Label(
            text = r"",
            halign = "left",
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.22, "center_y": 0.93},
            color = (0, 0, 0, 1),
            font_size = 16,
            text_size = (500, 100))
        self.labelSelectDirectory.text_size = (None, None)
        
        self.btnSelectDirectoryToOpen = Button(
            text = "Wybierz",
            size_hint = (0.1, 0.05),
            pos_hint = {"center_x": 0.4, "center_y": 0.93})
        self.btnSelectDirectoryToOpen.bind(on_press = partial(self.select_file_window))
        
    def create_button_to_select_directory_to_save(self):
        self.labelSaveDirectoryInfo = Label(
            text = "Ścieżka pliku do zapisu:",
            size_hint = (0.2, 0.02),
            pos_hint = {"center_x": 0.6, "center_y": 0.97},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.labelSaveDirectory = Label(
            text = r"",
            size_hint = (0.3, 0.02),
            pos_hint = {"center_x": 0.6, "center_y": 0.93},
            color = (0, 0, 0, 1),
            font_size = 16)
        
        self.btnSelectDirectoryToSave = Button(
            text = "Wybierz",
            size_hint = (0.1, 0.05),
            pos_hint = {"center_x": 0.83, "center_y": 0.93})
        self.btnSelectDirectoryToSave.bind(on_press = partial(self.select_directory_to_save_window))
                    
    def add_widgets_to_screen(self):
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
        self.datatableClass = DataTableWithData(self.screen)
        self.converter = Converter(self.screen)
        self.selectedFile = ""
        self.selectedDirectory = ""
        self.create_button_to_select_directory_to_open()
        self.create_button_to_select_directory_to_save()
        self.create_button_to_convert()
        self.add_widgets_to_screen()
        return self.screen
    

    
if __name__ == "__main__":
    MainWindow().run()