from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db
from tkcalendar import DateEntry

""" Functions for HomePage button callbacks """

db_columns = ['company','contact_details','position','hiring_platform','misc_details','date_applied']

class Create:
    """Creates Toplevel for application entry"""
    def __init__(self):
        self.create()

    def create(self):
        """Creates Toplevel for entries and Date Appiled and Save buttons"""
        self.scrolledtext_variables = []
        self.entry_variables = []
        self.date_variables = []
        frame = Toplevel()
        Label(frame, text='Enter Job Application').grid()
        self.create_entries(frame)
        self.save_entries(frame)
        self.back_button(frame)
                
    def create_entries(self, frame):
        """Populates Toplevel frame of Create class"""
        for title in db_columns:
            if title != db_columns[-1]:
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                if title == db_columns[-2]:
                    scroll_text = ScrolledText(frame, width=30, height=10)
                    scroll_text.grid()
                    self.scrolledtext_variables.append(scroll_text)
                else:
                    Entry(frame, textvariable=entry_variable).grid(sticky='we')
                    self.entry_variables.append(entry_variable)
            else:
                Label(frame, text=db_columns[-1]).grid()
                date_entry = DateEntry(frame)
                date_entry.grid()
                self.date_variables.append(date_entry)
                

    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = Button(frame, text='Save', command=lambda: self.save_handler(frame))
        button.grid(row=60, sticky=SE)

    def save_handler(self, frame):
        populate_db(self.convert())
        frame.destroy()

    def convert(self):
        """Converts all the entry objects to string for populate_db.py"""
        
        converted_variables = []
        for item in self.entry_variables:
            converted_variables.append(item.get())
        for item in self.scrolledtext_variables:
            converted_variables.append(item.get('1.0', 'end-1c'))
        # date output converted to str, year/month/day
        for item in self.date_variables:
            converted_variables.append(str(item.get_date()))

        return converted_variables

    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).grid(row=60, sticky=S)

        
class Read:
    def __init__(self):
        self.read()

    def read(self):
        """Displays all entries in database"""
        frame = Toplevel()
        table = read_data_from_db()
        sorted_table = self.sort_db_table(table)
        message, applications = self.create_message(sorted_table)
        self.create_display(frame, message, applications)
        self.back_button(frame)

    def sort_db_table(self, table):
        """Matches each entry label with entry data"""
        zipped_list = []
        for item in table:
            entry = dict((zip(db_columns, item)))
            zipped_list.append(entry)
        print(zipped_list)
        return zipped_list

    def create_message(self, sorted_table):
        """Creates string to view in Text widget"""
        message = ''
        seperator = '-' * 30
        for application in sorted_table:
            message += f'{seperator}\n'
            for label, entry in application.items():
                text_label = f'{label}: {entry}\n'
                message += text_label
        applications = len(sorted_table)

        return (message, applications)

    def create_display(self, frame, message, applications):
        """Insert message into Text widget, add a scrollbar"""
        Label(frame, text=f'You have applied for {applications} postions').pack()
        message_display = Text(frame)
        message_display.insert(END, message)
        message_scroll = Scrollbar(frame, command=message_display.yview)
        message_display.config(state='disabled', yscrollcommand=message_scroll.set)
        message_display.pack(side=LEFT)
        message_scroll.pack(side=RIGHT, fill=Y)
    

    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(side=BOTTOM)

class ReadSearch(Read):
    """Searchs specific queries from user and displays them"""
    def __init__(self):
        super().__init__()

    # need to refactor
    def read(self):
        frame = Toplevel()
        Label(frame, text='Select parameter to search:').pack(side=TOP)
        radio_var = StringVar()
        for title in db_columns:
            button = Radiobutton(frame, text=title, variable=radio_var, value=title)
            button.deselect()
            button.pack(side=TOP, anchor=W)
        Label(frame, text='Enter search query for selection').pack(side=TOP)
        entry_var = StringVar()
        Entry(frame, textvariable=entry_var).pack()
        Button(frame, text='Run Search', command=lambda: self.create_query(radio_var.get(), entry_var.get())).pack(anchor=SE)
        self.back_button(frame)
        
    def create_query(self, label, query):
        print(label, query)
        table = read_data_from_db(read_all=False, label=label, query=query)
        sorted_table = self.sort_db_table(table)
        message, applications = self.create_message(sorted_table)
        self.create_display(Toplevel(), message, applications)


class Update:
    def __init__(self):
        self.update()

    def update(self):
        frame = Toplevel()

class Delete:
    def __init__(self):
        self.delete()

    def delete(self):
        frame = Toplevel()

