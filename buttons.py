from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db, delete_from_db ,columns
from tkcalendar import DateEntry
from configs import format_string

""" Functions for HomePage button callbacks """

db_columns = columns

class Create:
    """Creates Toplevel for application entry"""
    def __init__(self):
        """Creates Toplevel for entries and Date Appiled and Save buttons"""
        self.scrolledtext_variables = []
        self.entry_variables = []
        self.date_variables = []
        frame = Toplevel()
        label = 'Enter Job Application'
        ttk.Label(frame, text=label, font='30').grid()
        frame.focus()
        self.create_menu(frame)
        self.save_entries(frame)
        self.back_button(frame)
                
    def create_menu(self, frame):
        """Populates Toplevel frame of Create class"""
        self.create_label(frame)
        self.create_misc_details(frame)
        self.create_date_entry(frame)

    def create_label(self, frame):
        columns = db_columns[:4]               
        for title in columns:
            title = format_string(title)
            ttk.Label(frame, text=title, font='30').grid(padx=100, pady=10)
            entry_variable = StringVar()
            ttk.Entry(frame, textvariable=entry_variable).grid(sticky='we', padx=9)
            self.entry_variables.append(entry_variable)

    def create_misc_details(self, frame):
        title = format_string(db_columns[-2])
        ttk.Label(frame, text=title, font='30').grid(padx=100, pady=10)
        scroll_text = ScrolledText(frame, width=40, height=10)
        scroll_text.grid()
        self.scrolledtext_variables.append(scroll_text)

    def create_date_entry(self, frame):
        title = format_string(db_columns[-1])
        ttk.Label(frame, text=title, font='30').grid()
        date_entry = DateEntry(frame)
        date_entry.grid()
        self.date_variables.append(date_entry)

    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = ttk.Button(frame, text='Save', command=lambda: self.save_handler(frame))
        button.grid(row=60, sticky=SE)

    def save_handler(self, frame):
        converted = self.convert()
        populate_db(converted)
        frame.destroy()

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

    def back_button(self, frame):
        ttk.Button(frame, text='Go Back', command=frame.destroy).grid(row=60, sticky=W)

        
class Display:
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
        frame.focus()

    def sort_db_table(self, table): 
        """Matches each entry label with entry data. Returns list containing dict of database records"""
        sorted_database_list = []
        for item in table:
            entry = dict((zip(db_columns, item)))
            sorted_database_list.append(entry)
        
        return sorted_database_list

    def create_message(self, sorted_table):
        """Creates string to view in Text widget"""
        message = ''
        for application in sorted_table:
            message += '\n'
            for label, entry in application.items():
                label = format_string(label)
                entry = format_string(entry, column=False)
                text_label = f'{label}: {entry}\n'
                message += text_label
        applications = len(sorted_table)

        return (message, applications)

    def create_display(self, frame, message, applications):
        """Insert message into Text widget, add a scrollbar"""
        position = 'position'
        if applications > 1:
            position = position + 's'
        else:
            position
        label_text = f'You have applied for {applications} {position}'
        ttk.Label(master=frame, text=label_text, font='8').pack()
        message_display = Text(master=frame, font='7')
        message_display.insert(END, message)
        message_scroll = ttk.Scrollbar(master=frame, command=message_display.yview)
        message_display.config(state='disabled', yscrollcommand=message_scroll.set)
        message_display.pack(side=LEFT)
        message_scroll.pack(side=RIGHT, fill=Y)
    
    # def yes_cancel(self, frame, position):
    #     return Positions.yes_cancel(self, frame, position)
    
    def back_button(self, frame):
        ttk.Button(master=frame, text='Go Back', command=frame.destroy).pack(padx=15)

class Search(Display):
    """Searchs specific queries from user and displays them"""
    def __init__(self):
        super().__init__()
    
    def read(self):
        frame = Toplevel()
        select_param = 'Select parameter to search:'
        enter_search = 'Enter search query for selection'
        ttk.Label(frame, text=select_param).pack(side=TOP, fill='both')
        radio_variable = self.create_menu(frame)
        ttk.Label(frame, text=enter_search).pack(side=TOP, fill='both')
        entry_variable = self.create_entry(frame)
        self.create_search_button(frame, radio_variable, entry_variable)
        self.back_button(frame)
        frame.focus()

    def create_menu(self, frame):
        radio_var = StringVar()
        for title in db_columns:
            title_clean = format_string(title)
            button = ttk.Radiobutton(frame, text=title_clean, variable=radio_var, value=title, width=30, padding=3)
            button.pack(side=TOP, anchor=W)
        return radio_var
    
    def create_entry(self, frame):
        entry_var = StringVar()
        ttk.Entry(frame, textvariable=entry_var).pack(fill='both', padx=15)
        return entry_var
    
    def create_search_button(self, frame, radio_variable, entry_variable):
        ttk.Button(frame, text='Run Search', command=lambda: self.create_query(param=radio_variable.get(), query=entry_variable.get())).pack()

    def create_query(self, param, query):
        print(f'Parameter: {param}\nSearched for: {query}')
        table = read_data_from_db(read_all=False, param=param, query=query)
        sorted_table = self.sort_db_table(table)
        message, applications = self.create_message(sorted_table)
        self.create_display(Toplevel(), message, applications)

class Positions(Display):

    def __init__(self) -> None:
        super().__init__()
    
    def read(self):
        """Displays all entries in database"""
        self.frame = Toplevel()
        table = read_data_from_db()
        sorted_table = self.sort_db_table(table)
        self.create_display(self.frame, sorted_table)
        self.back_button(self.frame)
        self.frame.focus()

    def create_message(self, application):
        message = ''
        for label, entry in application.items():
                label = format_string(label)
                entry = format_string(entry, column=False)
                text_label = f'{label}: {entry}\n'
                message += text_label

        return message
        
    def create_display(self, frame, sorted_table): # create frame to hold the labels of positions applied for with company in (): Dev (Hootsuite)
        for application in sorted_table:
            message = self.create_message(application)
            self.create_button(frame, message, application)
  
    def create_button(self, frame, message, application):
        position = application["position"]
        company = application["company"]
        button_text = f'{position}: {company}'
        ttk.Button(master=frame, text=button_text, command=lambda: self.button_info(message, position)).pack(padx=15, pady=5, fill='both')
    
    def button_info(self, message, position):
        frame = Toplevel()
        ttk.Label(master=frame, text=message, font='8').pack(padx=30)
        self.back_button(frame)
        self.delete(frame, position)
        frame.focus()
    # @classmethod
    def delete(self, frame, position):
        return ttk.Button(frame, text='Delete record', command=lambda: self.yes_cancel(frame, position)).pack()

    def yes_cancel(self, frame, position):
        title = 'Delete?'
        msg_box = messagebox.askokcancel(title=title, message='Are you sure?')
        if msg_box:
            delete_from_db(position)
            frame.destroy()
            self.frame.destroy()

class Update:
    def __init__(self):
        frame = Toplevel()
        

    def update(self):
        pass

            



