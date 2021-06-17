import tkinter as tk  
from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont 
from PIL import ImageTk, Image
import globalinit 
import os

# Images location
image_loc = "images/"

class Result_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Set page background color
        self.configure(background="#232323")
        frame1 = Frame(self,background="#232323")
        frame1.pack(fill=X)

        # Create frame for signout button
        button = ttk.Button(frame1, text="Sign Out", command=lambda: controller.show_frame("Login_Page"))
        button.pack(side="right")

        # Display welcome message
        temp_name = "Welcome on-board"
        label = tk.Label(frame1, text=temp_name, font=tkfont.Font(family='Helvetica', size=12, weight="bold"), bg="#232323")
        label.pack(side="left", fill="x", pady=10)

        # SoleQ logo
        path = image_loc + "logo.png"

        # Display the SolveQ logo at the top of the page
        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')

        # Create Blank frame
        self.frame = Frame(self,background="#232323")
        self.frame.pack(fill=X)
        self.button = ttk.Button(self.frame, text="Answer", command=self.show)
        self.button.pack(side="left",padx=50,pady=100)
            

    # Display the result
    def show(self):   

        # Create button for new equation solving
        self.button2 = ttk.Button(self.frame, text="New", command=self.destroy_ans)        
        self.button2.pack(side="left",padx=50,pady=100)
        
        # Attempt to display result
        try :            
            result_image=[]
            w=[]
            number=0

            # Display the result images in format
            for i in globalinit.pics :
                if '.gif' in i and i!='pic0.gif':
                    result_image.append(PhotoImage(file = i))
                    w.append(Label(self.frame, image=result_image[number]))
                    w[number].photo = result_image[number]
                    w[number].pack(side="left",padx=10)
                    number+=1
            self.button.pack_forget()
        except :
            print("Error")
            pass
        
        # Remove result.gif if it exists now
        if os.path.exists("result.gif"):
            os.remove("result.gif")
        
    # Clear up the page
    def destroy(self) :

        # Clear the global variable list pics
        globalinit.pics.clear()
        try :
            self.frame.pack_forget()
            self.controller.show_frame("Input_Page")
        except :
            pass

    # Clear up the result
    def destroy_ans(self) :

        # Delete images from gobal varianle lists pics and clear it
        for i in globalinit.pics:
            if '.gif' in i :
                os.remove(i)
        globalinit.pics.clear()

        # Clear up the result page and go to the input page for next equation
        try :
            self.frame.pack_forget()
            self.frame = Frame(self,background="#232323")
            self.frame.pack(fill=X)
            self.button = ttk.Button(self.frame, text="Answer", command=self.show)
            self.button.pack(side="left",padx=50,pady=100)
            self.controller.show_frame("Input_Page")
        except :
            pass