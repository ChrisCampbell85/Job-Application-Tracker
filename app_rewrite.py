from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db, delete_from_db, columns
from tkcalendar import DateEntry
from configs import format_string
from PIL import ImageTk, Image

DB_COLUMNS = columns

class Create:
    def __init__(self, root, mainMenuFrame):
        self.scrolledtext_variables = []
        self.entry_variables = []
        self.date_variables = []
        self.frame = Frame(root)
        self.frame.pack()
        self.mainMenuFrame = mainMenuFrame
        ttk.Label(self.frame, text='Hello').pack()
        self.create_menu()
        self.save_entries()
        self.backButton()
        self.quitButton()

    def __str__(self):
        return 'Create Application'
    
    def create_menu(self):
        """Populates Toplevel frame of Create class"""
        self.create_label()
        self.create_misc_details()
        self.create_date_entry()

    def create_label(self):
        columns = DB_COLUMNS[:4]               
        for title in columns:
            title = format_string(title)
            ttk.Label(self.frame, text=title, font='30').pack()
            entry_variable = StringVar()
            ttk.Entry(self.frame, textvariable=entry_variable).pack()
            self.entry_variables.append(entry_variable)

    def create_misc_details(self):
        title = format_string(DB_COLUMNS[-2])
        ttk.Label(self.frame, text=title, font='30').pack()
        scroll_text = ScrolledText(self.frame, width=40, height=10)
        scroll_text.pack()
        self.scrolledtext_variables.append(scroll_text)

    def create_date_entry(self):
        title = format_string(DB_COLUMNS[-1])
        ttk.Label(self.frame, text=title, font='30').pack()
        date_entry = DateEntry(self.frame)
        date_entry.pack()
        self.date_variables.append(date_entry)

    def save_entries(self):
        """Button that saves entry objects to database"""
        button = ttk.Button(self.frame, text='Save', command=self.save_handler)
        button.pack()

    def save_handler(self):
        converted = self.convert()
        populate_db(converted)
        self.frame.destroy()

    def convert(self):
        """Converts all the entry objects to string for populate_db.py"""
        converted_variables = []
        for item in self.entry_variables:
            converted_variables.append(item.get())
        for item in self.scrolledtext_variables:
            converted_variables.append(item.get('1.0', 'end-1c'))
        # date output converted to str > year/month/day
        for item in self.date_variables:
            converted_variables.append(str(item.get_date()))

        return converted_variables
        
    def backButton(self):
        ttk.Button(self.frame, text='Back', command=self.backToMenu).pack()

    def backToMenu(self):
        self.frame.pack_forget()
        self.mainMenuFrame.pack()

    def quitButton(self):
        ttk.Button(self.frame, text='Quit', command=self.frame.quit).pack()

class App:
    def __init__(self):
        self.clsName = Create
        self.root = Tk()
        self.configureRoot()
        self.frame = Frame(master=self.root)
        self.frame.pack()
        self.homeButtons()
        self.root.mainloop()

    def configureRoot(self):
        self.root.title('Application Tracker')
        self.root.geometry('300x360')

    def homeButtons(self):
            ttk.Button(self.frame, text=self.clsName.__str__(self), command=self.changeFrame).pack()
            
    def changeFrame(self):
        self.frame.pack_forget()
        self.clsName(self.root, self.frame)

        # self.buttons[]
         # Hide frame2
        

app = App()