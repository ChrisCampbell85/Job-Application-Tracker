from tkinter import *
from tkinter import ttk



class Create:
    def __init__(self, root, mainMenuFrame):
        self.frame = Frame(root)
        self.frame.pack()
        self.mainMenuFrame = mainMenuFrame
        ttk.Label(self.frame, text='Hello').pack()
        self.backButton()
        self.quitButton()

    def __str__(self):
        return 'Create Application'
        
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
        self.configiureRoot()
        self.frame = Frame(master=self.root)
        self.frame.pack()
        self.homeButtons()
        self.root.mainloop()

    def configiureRoot(self):
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