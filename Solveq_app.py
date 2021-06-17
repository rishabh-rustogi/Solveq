import tkinter as tk  
from tkinter import *
from tkinter import font  as tkfont 
from Login_page import Login_Page
from Result_page import Result_Page
from Input_page import Input_Page
import globalinit
from utility_functions import donothing, confirm_exit

# Frame Class
class SolveQApp(tk.Tk):

    # Initialize the Solveq Application Container
    def __init__(self, *args, **kwargs):

        # Initialize the tkinter app with arguments
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set the font settings
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        # Initialize the container to store different pages of the app
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Put pages in set location 
        self.frames = {}
        for F in (Login_Page, Result_Page, Input_Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the login page
        self.show_frame("Login_Page")

    # Show the requested page
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class SolveQAppInit():
    def __init__(self):

        # Initialize the global variable list
        globalinit.init()
        
        # Initialize the SolveQApp
        self.app = SolveQApp()

        # Set the application size
        self.app.geometry("800x600+600+200")
        self.app.resizable(0,0)

        # Set application title
        self.app.title('SolveQ')

        # Set application properties
        menubar = Menu(self.app)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=confirm_exit)
        menubar.add_cascade(label="File", menu=filemenu)
        

    def startApplication(self):
        
        # Start the application
        self.app.mainloop()