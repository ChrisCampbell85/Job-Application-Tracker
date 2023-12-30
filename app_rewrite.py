from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from interact_db import populate_db, read_data_from_db, delete_from_db, columns
from tkcalendar import DateEntry
from configs import format_string,style_tbutton
from PIL import ImageTk, Image

DB_COLUMNS = columns

class Create:
    def __init__(self, root, main_menu_frame, utility_buttons):
        self.entry_variables = []
        self.frame = Frame(root)
        self.frame.pack()
        self.main_menu_frame = main_menu_frame
        self.utility_buttons = utility_buttons
        ttk.Label(self.frame, text='Enter Job Application', font='30').pack(fill='y', pady=10)
        self.create_menu()
        self.save_entries()
        self.utility_buttons(self.frame, self.main_menu_frame).back_button()
        self.utility_buttons(self.frame, self.main_menu_frame).quit_button()

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
            ttk.Entry(self.frame, textvariable=entry_variable).pack(fill='x')
            self.entry_variables.append(entry_variable)

    def create_misc_details(self):
        title = format_string(DB_COLUMNS[-2])
        ttk.Label(self.frame, text=title, font='30').pack()
        self.scroll_text = ScrolledText(self.frame, width=40, height=10)
        self.scroll_text.pack()

    def create_date_entry(self):
        title = format_string(DB_COLUMNS[-1])
        ttk.Label(self.frame, text=title, font='30').pack()
        self.date_entry = DateEntry(self.frame)
        self.date_entry.pack()

    def save_entries(self):
        """Button that saves entry objects to database"""
        button = ttk.Button(self.frame, text='Save', command=self.save_handler)
        button.pack()

    def save_handler(self):
        """Converts all the entry objects to string for populate_db.py"""
        self.converted_variables = []
        self.convertEntry()
        self.convertScroll()
        self.convertDate()
        print(self.converted_variables)
        populate_db(self.converted_variables)
        self.save_complete()

    def save_complete(self):
        messagebox.showinfo('Well Done', 'Save Completed')
        self.utility_buttons.back_to_menu(self)
    
    def convertEntry(self):
        for item in self.entry_variables:
            self.converted_variables.append(item.get())

    def convertScroll(self):
        self.converted_variables.append(self.scroll_text.get('1.0', 'end-1c'))
    
    def convertDate(self):
        # date output converted to str > year/month/day
        self.converted_variables.append(str(self.date_entry.get_date()))

class Show:
    def __init__(self, root, main_menu_frame, utility_buttons) -> None:
        self.frame = Frame(root)
        self.frame.pack()
        self.main_menu_frame = main_menu_frame
        self.utility_buttons = utility_buttons
        table = read_data_from_db()
        sorted_table = self.sort_db_table(table)
        message, applications = self.create_message(sorted_table)
        self.create_display(message, applications)
        self.utility_buttons(self.frame, self.main_menu_frame).back_button()
        self.utility_buttons(self.frame, self.main_menu_frame).quit_button()
        
    def __str__(self):
        return "Show All"

    def sort_db_table(self, table): 
        """Matches each entry label with entry data. Returns list containing dict of database records"""
        sorted_database_list = []
        for item in table:
            entry = dict((zip(DB_COLUMNS, item)))
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

    def create_display(self, message, applications):
        """Insert message into Text widget, add a scrollbar"""
        position = 'position'
        if applications > 1:
            position = position + 's'
        else:
            position
        label_text = f'You have applied for {applications} {position}'
        ttk.Label(master=self.frame, text=label_text, font='8').pack()
        message_display = Text(master=self.frame, font='7', width=50)
        message_display.insert(END, message)
        message_scroll = ttk.Scrollbar(master=self.frame, command=message_display.yview)
        message_display.config(state='disabled', yscrollcommand=message_scroll.set)
        message_display.pack(side=LEFT)
        message_scroll.pack(side=RIGHT, fill=Y)
        
class UtilityButtons:
    def __init__(self, frame, main_menu_frame=None) -> None:
        self.frame = frame
        self.main_menu_frame = main_menu_frame
        
    def back_button(self):
        ttk.Button(self.frame, text='Back', command=self.back_to_menu).pack()

    def back_to_menu(self):
        self.frame.pack_forget()
        self.main_menu_frame.pack()

    def quit_button(self):
        ttk.Button(self.frame, text='Quit', command=self.frame.quit).pack()
    

class App:
    def __init__(self, utility_buttons):
        self.root = Tk()
        self.configureRoot()
        self.utility_buttons = utility_buttons
        self.frame = Frame(master=self.root)
        self.frame.pack(expand=TRUE)
        self.homeButtons()
        self.utility_buttons(self.frame).quit_button()
        self.root.mainloop()

    def configureRoot(self):
        self.root.title('Application Tracker')
        self.root.geometry('700x620')

    def homeButtons(self):
        style_tbutton()
        createButton = ttk.Button(self.frame, text=Create.__str__(self), command=lambda: self.changeFrame(Create)).pack(fill='both', padx=1, pady=10)
        showButton = ttk.Button(self.frame, text=Show.__str__(self), command=lambda: self.changeFrame(Show)).pack(fill='both', padx=1, pady=10)
         
    def changeFrame(self, cls):
        self.frame.pack_forget()
        cls(self.root, self.frame, UtilityButtons)
        

app = App(UtilityButtons)