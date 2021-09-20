from tkinter import *
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db
from tkcalendar import DateEntry

""" Functions for HomePage button callbacks """

entrybox_labels = ['Company','Contact Details', 'Position', 'Hiring Platform', 'Misc Details', 'Date Applied']

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
        for title in entrybox_labels:
            if title != entrybox_labels[-1]:
                Label(frame, text=title).grid()
                entry_variable = StringVar()
                if title == entrybox_labels[-2]:
                    scroll_text = ScrolledText(frame, width=30, height=10)
                    scroll_text.grid()
                    self.scrolledtext_variables.append(scroll_text)
                else:
                    Entry(frame, textvariable=entry_variable).grid(sticky='we')
                    self.entry_variables.append(entry_variable)
            else:
                Label(frame, text=entrybox_labels[-1]).grid()
                date_entry = DateEntry(frame)
                date_entry.grid()
                self.date_variables.append(date_entry)
                

    def save_entries(self, frame):
        """Button that saves entry objects to database"""
        button = Button(frame, text='Save', command=lambda: populate_db(self.convert()))
        button.grid(row=60, sticky=SE)


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
        """Displays current entries in database"""
        # add scroll functionality!
        frame = Toplevel()
        table = read_data_from_db()
        print(table)
        sorted_table = self.sort_db_table(table)
        self.create_message(frame, sorted_table)


    def sort_db_table(self, table):
        """Matches each entry label with entry data"""
        zipped_list = []
        for item in table:
            entry = dict((zip(entrybox_labels, item)))
            zipped_list.append(entry)

        return zipped_list

    def create_message(self, frame, sorted_table):
        """Creates string to view in Message widget"""
        message = ''
        for application in sorted_table:
            message += '\n'
            for label, entry in application.items():
                text_label = f'\t{label}: {entry}\n'
                message += text_label
        application_number = len(sorted_table)
        Label(frame, text=f'You have applied for {application_number} postions').pack()
        # insert message into Text widget
        message_display = Text(frame)
        message_display.insert(END, message)
        message_display.pack()
    
        self.back_button(frame)
        
        # if scroll functionality is desired
        # canvas.bind_all("<MouseWheel>", lambda event: self.scrollable(event, canvas))
    
    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(side=BOTTOM, anchor=S)

    def scrollable(self, event, canvas):
        canvas.yview_scroll(int(-1*(event.delta/100)), "units")

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

class Test:
    def __init__(self) -> None:
        self.test()

    def test(self):
        pass


