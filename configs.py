from tkinter import ttk

def format_string(input: str, column=True):

        if column:
                input = input.title().replace('_', ' ')
        else:
                input = input.capitalize().replace('_', ' ') 
        
        return input

def style_tbutton():
        style = ttk.Style()
        style.configure("TButton", padding=10, expand=1,
        background="#ccc")
        style.map("TButton",
        foreground=[('pressed', 'red'), ('active', 'green')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
