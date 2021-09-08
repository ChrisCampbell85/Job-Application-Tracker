from tkinter import *
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
from interact_db import *
from tkcalendar import Calendar, DateEntry

""" Functions for button callbacks """

# save entries into SQLite db

# homepage CRUD button funcs
# need to pass in homepage frame

entrybox_labels = ['Company','Contact Details', 'Position', 'Hiring Platform', 'Misc Details', 'Date Applied']
scrolledtext_variables = []
entry_variables = []

class Create:
    """Creates Toplevel for application entry"""
    def __init__(self):
        self.create()

    def create(self):
        frame = Toplevel()
        Label(frame, text='Enter Job Application').grid()
        self.create_entries(frame)
        self.save_entries(frame)
        self.date_applied_button(frame)
                
    def create_entries(self, frame):
        """Populates Toplevel frame of Create class"""
        for title in entrybox_labels:
            if title != entrybox_labels[-1]:
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                if title == entrybox_labels[-2]:
                    scroll_text = ScrolledText(frame, width=30, height=10)
                    scroll_text.grid()
                    scrolledtext_variables.append(scroll_text)
                else:
                    Entry(frame, textvariable=entry_variable).grid(sticky='we')
                    entry_variables.append(entry_variable)
        entry_variables.append(entrybox_labels[-1])
        print(scrolledtext_variables)
        print(entry_variables)
     
    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = Button(frame, text='Save', command=lambda: populate_db(self.convert()))
        button.grid(row=60, sticky=SE)

    def convert(self):
        """Converts all the entry objects to string for populate_db.py"""
        converted = []
        # currently skips last entry, need to constuct date selection option
        # placeholder used for now
        for item in entry_variables[:-1]:
            converted.append(item.get())
        for item in scrolledtext_variables:
            converted.append(item.get('1.0', 'end-1c'))
        converted.append(entry_variables[-1])
        return converted
            

    def date_applied_button(self, frame):
        Button(frame, text='Add Date Applied', command=lambda: self.calendar_selection(frame)).grid(row=60, sticky=S)
        
    def calendar_selection(self, frame):
        pass


        

        
# figure out how to do rowspans so info is side by side
class Read:
    def __init__(self):
        self.read()

    def read(self):
        frame = Toplevel()
        table = read_data_from_db()
        print(table)
        
class Update:
    def __init__(self):
        self.update()

    def update():
        frame = Toplevel()

class Delete:
    def __init__(self):
        self.delete()

    def delete():
        frame = Toplevel()

toplevels = {'Create': Create, 'Read': Read, 'Update': Update, 'Delete': Delete}

