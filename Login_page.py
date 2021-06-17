import tkinter as tk  
from PIL import ImageTk
import PIL.Image
from tkinter import *
import globalinit

# Images location
image_loc = "images/"

# Applicaiton starts with a login page
class Login_Page(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Set application backgroud color
        self.configure(background="#232323")

        # SolveQ logo
        path = image_loc + "logo.png"
        
        # Display the SolveQ logo at the top of the page
        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(PIL.Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')
        
        # Blank frame for padding
        frame0 = Frame(self,bg="#232323")
        frame0.pack(fill=X)
        frame0 = Frame(self,bg="#232323")
        frame0.pack(fill=X,padx=100,pady=30) 

        # Input field frame for username
        frame1 = Frame(self,bg="#232323")
        frame1.pack(fill=X,padx=100,pady=0) 
        lbl1 = Label(frame1, text="Username",font=" Helvetica",fg="#FFFFFF", width=10,bg="#232323")
        lbl1.pack(side=LEFT,padx=100,pady=0)
       
        # Get entry for Username
        self.user = Entry(frame1)
        self.user.pack(padx=1, pady=0,expand=False)

        # Input field frame for password
        frame2 = Frame(self,bg="#232323")
        frame2.pack(fill=X,padx=100,pady=0)
        lbl2 = Label(frame2, text="Password",font=" Helvetica",fg="#FFFFFF", width=10,bg="#232323")
        lbl2.pack(side=LEFT, padx=100, pady=0)        

        # Get entry for Password
        self.password = Entry(frame2,show="*")
        self.password.pack(padx=1, pady=0, expand=False)

        # Blank frame for padding
        frame4 = Frame(self,bg="#232323")
        frame4.pack(fill=X)
        
        # Create a frame to display massages on the login page
        self.var = StringVar()
        self.var.set('')
        lbl2 = Label(frame4, textvariable=self.var, width=300 , bg="#232323", fg="red")
        lbl2.pack(side=LEFT, padx=20, pady=10) 

        # Login button which calls the accept function for validity of password
        frame3 = Frame(self,bg="#232323")
        frame3.pack(fill=X)
        login_button = tk.Button(frame3, text="Login", command=self.accept,width=10, bg="#4A4A4A", fg="white")
        login_button.pack(side=BOTTOM, ipadx=17, ipady=5)


    def accept(self):

        # Get username and password from the input fields
        input_username = self.user.get()
        input_password = self.password.get()

        # Check if username and password pair in configure file 
        if globalinit.checkUserPass(input_username, input_password):

            # Set message to logged out incase user logout
            self.var.set('You have successfully logged out')

            # Got to the Input page frame
            self.controller.show_frame("Input_Page")

            # Delete the username and password variables
            self.user.delete(0,END)
            self.password.delete(0,END)

        else:
            # Set message to incorrect username/password
            self.var.set('The Username or Password is incorrect')
        
        # Delete the username and password variables
        self.user.delete(0,END)
        self.password.delete(0,END)