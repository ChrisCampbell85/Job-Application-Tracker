from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interact_db import *
from tkcalendar import Calendar, DateEntry

""" Functions for button callbacks """

# save entries into SQLite db

# homepage CRUD button funcs
# need to pass in homepage frame

entrybox_labels = ['Company','Contact Details', 'Position', 'Hiring Platform', 'Misc Details', 'Date Applied']

class Create:
    def __init__(self):
        self.entry_variables = []
        self.converted_entry_variables = []
        self.create()

    def create(self):
        frame = Toplevel()
        Label(frame, text='Enter Job Application').grid()
        self.create_entries(frame)
        self.save_entries(frame)
        self.date_applied_button(frame)
                
    def create_entries(self, frame):
        for title in entrybox_labels:
            if title != entrybox_labels[-1]:
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                # add logic/formatting for date applied
                if title == entrybox_labels[-2]:
                    scroll_text = ScrolledText(frame, width=30, height=10)
                    scroll_text.grid()
                    self.entry_variables.append(scroll_text)
                else:
                    Entry(frame, textvariable=entry_variable).grid(sticky='we')
                    self.entry_variables.append(entry_variable)

    def save_entries(self, frame):
        button = Button(frame, text='Save', command=lambda: populate_db(self.converted_entry_variables))
        button.grid(row=60, sticky=SE)

    def date_applied_button(self, frame):
        Button(frame, text='Add Date Applied', command=lambda: self.calendar_selection(frame)).grid(row=60, sticky=S)
        
    
    def calendar_selection(self, frame):
        pass

    def convert_entry_variables(self):
        self.converted_entry_variables = self.entry_variables.copy()
        for item in self.converted_entry_variables:
            item = item.get('1.0', 'end-1c')

        

        
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

