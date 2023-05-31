from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db, columns
from tkcalendar import DateEntry
from preprocessing import format_column_names

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
        Label(frame, text='Enter Job Application', font='30').grid()
        self.create_menu(frame)
        self.save_entries(frame)
        self.back_button(frame)
                
    def create_menu(self, frame):
        """Populates Toplevel frame of Create class"""
        self.create_label(frame)
        self.create_scroll(frame)
        self.create_date_entry(frame)

    def create_label(self, frame):
        columns = db_columns[:4]    # all labels               
        for title in columns:
            title = format_column_names(title)
            Label(frame, text=title, font='50').grid(padx=100, pady=10)
            entry_variable = StringVar()
            Entry(frame, textvariable=entry_variable).grid(sticky='we', padx=15)
            self.entry_variables.append(entry_variable)

    def create_scroll(self, frame):
        title = db_columns[-2]
        Label(frame, text=title, font='50').grid(padx=100, pady=10)
        scroll_text = ScrolledText(frame, width=100, height=20)
        scroll_text.grid()
        self.scrolledtext_variables.append(scroll_text)

    def create_date_entry(self, frame):
        title = db_columns[-1]
        Label(frame, text=title).grid()
        date_entry = DateEntry(frame)
        date_entry.grid()
        self.date_variables.append(date_entry)

    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = Button(frame, text='Save', font='11', command=lambda: self.save_handler(frame))
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
        # date output converted to str > year/month/day
        for item in self.date_variables:
            converted_variables.append(str(item.get_date()))

        return converted_variables

    def back_button(self, frame):
        Button(frame, text='Go Back', font='6', command=frame.destroy).grid(row=60, sticky=S)

        
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
        for application in sorted_table:
            message += '\n'
            for label, entry in application.items():
                label = format_column_names(label)
                entry = format_column_names(entry)
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
        Label(frame, text=f'You have applied for {applications} {position}', font='8').pack()
        message_display = Text(frame, font='7')
        message_display.insert(END, message)
        message_scroll = Scrollbar(frame, command=message_display.yview)
        message_display.config(state='disabled', yscrollcommand=message_scroll.set)
        message_display.pack(side=LEFT)
        message_scroll.pack(side=RIGHT, fill=Y)
    
    def back_button(self, frame):
        Button(frame, text='Go Back', font='2', command=frame.destroy).pack(side=BOTTOM)

class Search(Read):
    """Searchs specific queries from user and displays them"""
    def __init__(self):
        super().__init__()
    
    def read(self):
        frame = Toplevel()
        Label(frame, text='Select parameter to search:', font='11').pack(side=TOP)
        radio_variable = self.create_menu(frame)
        Label(frame, text='Enter search query for selection', font='3').pack(side=TOP)
        entry_variable = self.create_entry(frame)
        self.create_search_button(frame, radio_variable, entry_variable)
        self.back_button(frame)

    def create_menu(self, frame):
        radio_var = StringVar()
        for title in db_columns:
            title_clean = format_column_names(title)
            button = Radiobutton(frame, text=title_clean, font='15', variable=radio_var, value=title)
            button.pack(side=TOP, anchor=W)
        return radio_var
    
    def create_entry(self, frame):
        entry_var = StringVar()
        Entry(frame, textvariable=entry_var).pack()
        return entry_var
    
    def create_search_button(self, frame, radio_variable, entry_variable):
        Button(frame, text='Run Search', command=lambda: self.create_query(label=radio_variable.get(), query=entry_variable.get())).pack(anchor=SE)

    def create_query(self, label, query):
        print(f'Parameter: {label}\nSearched for: {query}')
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

