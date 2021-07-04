from tkinter import messagebox 
from tkinter import *
import socket

# split latex equation based on delimiter "="
def split(text):
    return text.split("=")

# Tkinter function
def donothing():
   filewin = Toplevel(app)
   button = Button(filewin, text="Do nothing button")
   button.pack()

# Exit confirmation message
def confirm_exit():
   result = messagebox.askokcancel("Exit Confirmation","Are you sure you want to exit?")
   if result==1:
    app.destroy()
    exit()

# Check if system connected to the internet
def is_connected():
    try:
        socket.create_connection(("www.google.com",80))
        return True
    except OSError:
        pass
    return False