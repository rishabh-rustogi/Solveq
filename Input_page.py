import tkinter as tk  
from tkinter import *
import cv2
from tkinter import ttk
from tkinter import font  as tkfont 
from PIL import ImageTk, Image
from tkinter import filedialog
from utility_functions import is_connected
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
from tkinter import messagebox 
from PIL import ImageDraw
import requests
import json
import base64
import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

from utility_functions import split
import globalinit


# Images location
image_loc = "images/"

# Sound clip location
sound_loc = "soundclips/"

class Input_Page(tk.Frame):

    def __init__(self, parent, controller,video_source=0):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Set page background color
        self.configure(background="#232323")
        frame1 = Frame(self,background="#232323")
        frame1.pack(fill=X)

        cap = cv2.VideoCapture(image_loc + 'Comp_6.gif')
        
   
        # Check if camera is opened
        if (cap.isOpened()== False):  
          print("Error opening video file") 
   
        # Read until video is completed and capture frame-by-frame  
        while cap.isOpened(): 
            ret, frame = cap.read()

            if ret == True: 
                # Display the frame captures
                cv2.imshow('Frame', frame) 

                # Press "Q" to exit
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    break

            # Break the loop 
            else:  
                break
   
        # When done release the video capture object 
        cap.release() 
   
        # Closes all the CV2 frames 
        cv2.destroyAllWindows() 

        # Create frame for signout button
        button = ttk.Button(frame1, text="Sign Out", command=lambda: controller.show_frame("Login_Page"))
        button.pack(side="right")

        # Display welcome message
        welcome = "Welcome onboard"
        label = tk.Label(frame1, text=welcome, font=tkfont.Font(family='Helvetica', size=12,weight="bold"),fg="#FFFFFF", bg="#232323")
        label.pack(side="left", fill="x", pady=10)

        # SoleQ logo
        path = image_loc + "logo.png"

        # Display the SolveQ logo at the top of the page
        canvas = Canvas(self,width = 256,height = 150,bd=0,bg="#232323",highlightthickness=0)
        canvas.pack(pady=10)
        canvas.image = ImageTk.PhotoImage(Image.open(path))
        canvas.create_image(0,0,image=canvas.image,anchor='nw')
        
        self.frame12 = Frame(self,background="#232323")
        self.frame12.pack(fill=X)

        # Display the capture icon
        self.loadimage1 = tk.PhotoImage(file=image_loc + "capt.png")
        capture_image = tk.Button(self.frame12,image=self.loadimage1,command = self.capture,bg="#232323")
        capture_image["border"]="0"
        capture_image.pack(side="left", pady=40,padx=25)

        # Display the speakup icon
        self.loadimage3 = tk.PhotoImage(file=image_loc + "speakup.png")
        file_opener = tk.Button(self.frame12, image=self.loadimage3,command = self.audio_text,bg="#232323")
        file_opener["border"] = "0"
        file_opener.pack(side="left",pady=40,padx=35)

        # Display the select-image icon
        self.loadimage2 = tk.PhotoImage(file=image_loc + "select.png")
        file_opener = tk.Button(self.frame12, image=self.loadimage2,command = self.open_file,bg="#232323")
        file_opener["border"] = "0"
        file_opener.pack(side="left",pady=40,padx=45)
        
        # Create Blank frame
        self.frame_a = Frame(self,background="#232323")
        self.frame_a.pack(fill=X)
        self.frame_com = Frame(self,background="#232323")
        self.frame_com.pack(fill=X)

    # Open image file
    def open_file(self):
        result = filedialog.askopenfile(initialdir=".",title="Select File", filetypes=(("JPEG files",".jpg"),("PNG files",".png"),("all files",".*")))

        # If image exists then convert the image
        if result != None :
            self.convert(result.name)
        else :
            # Else print an error
            print("[INFO] No files selected... ")

    # Capture image from camera
    def capture(self):

        # Start CV2 video capture
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Capture the image with space until "q" is pressed
        while(True):
            ret, frame_cam = cap.read()
            rgb = cv2.cvtColor(frame_cam, cv2.COLOR_BGR2BGRA)
            cv2.imshow('framej', rgb)  
            cv2.putText(frame_cam, "Type q to Quit:",(50,700), font, 1,(255,255,255),2,cv2.LINE_AA)

            if not ret:
                break
            # Monitor keystrokes
            k = cv2.waitKey(1)

            # If "q" is pressed exit the loop, else if space is pressed capture the image
            if k & 0xFF == ord('q'):
                print("Quitting...")
                break
            elif k & 0xFF == ord(' '):
                print("Captured")
                out = cv2.imwrite('capture.png', frame_cam)
                break

        # When done release the video capture object 
        cap.release() 
   
        # Closes all the CV2 frames 
        cv2.destroyAllWindows() 

        # Convert the captured image
        self.convert('capture.png')

    # Get equation from speech
    def audio_text(self):

        # Check if the system is connected to the internet
        if is_connected():
            
            # Initialize the Speech Recognizer object
            r = sr.Recognizer()
            text=''

            # Initialize recognizer (source is taken as microphone)
            with sr.Microphone() as source:     
                r.adjust_for_ambient_noise(source) 
                print("[INFO] Speak the Equation...")
                audio = r.listen(source)    
            try:
                print("[INFO] Listening...")
                # Audio is converted to text
                text = r.recognize_google(audio)    

                # Audio is set to English
                targetLanguage = 'en'

                # Convert the text to english
                tts = gTTS(text, targetLanguage)  

                # play the recorded voice and then delete it
                tts.save("equation.mp3")
                playsound("equation.mp3")
                os.remove("equation.mp3")
                print("Removed")

            except sr.UnknownValueError:
                # If the voice is not clear
                playsound(sound_loc + "not_recog.mp3")
                print("[INFO] Could not recognize your voice...")

            except sr.RequestError as e:
                # If Google Speech Recognizer service is not longer available
               print("[INFO] Could not request results from Google Speech Recognition service; {0}".format(e))
            
            # Create image of the equation from the text
            img = Image.new('RGB', (100, 30), color = (73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10,10), text, fill=(255,255,0))

            # Save the image as capture.png
            img.save('capture.png')
            print("[INFO] Converting...")

            # Convert the new image created
            self.convert('capture.png')
        else:
            # If the system is not connected to the internet
            messagebox.showinfo("Connection Error", "Check your connection and try again")
        
    # Pass the Capture image to Mathpix function 
    def convert(self,loc):
        print("[INFO] Mathpix Running...")
        self.mathpix(loc)

    # Mathpix API to convert image to proper LATEX format (Any input source -> image -> Latex format -> Solve equation)
    def mathpix(self,loc):

        # Check if the system is connected to the internet
        if is_connected():

            # Image file location
            file_path = loc
            
            # Prepare image to pass to the mathpix api
            image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()

            (app_key, app_id) = globalinit.retMathpixKeys()

            # Pass the image using app_id and app_key to Mathpic API and retieve the json
            lateximage = requests.post("https://api.mathpix.com/v3/latex",
                data=json.dumps({'src': image_uri}),
                    headers={"app_id": app_id, "app_key": app_key, 
                            "Content-type": "application/json"})

            # get the json object
            temp = json.dumps(json.loads(lateximage.text), indent=4, sort_keys=True)
            resp = json.loads(temp)

            # Get the confidence parameter
            self.confidence = resp['latex_confidence']

            #Split the latex text into two part using "=" as delimiter 
            part1,part2 = split(resp['latex'])
            params = {part1:part2}

            # Check if the confidence parameter is 0
            if resp['latex_confidence'] == 0:
                messagebox.showerror(title='Invalid Image', message='The Image can not be converted. Please try once again.')
            else :

                # Remove the captured image
                if os.path.exists('capture.png'):
                    os.remove('capture.png')
                
                # Encode the latex equation
                url_params = urllib.parse.urlencode(params)
                
                # Read Woflram Alpha api id
                app_id = globalinit.retWolfAppID()

                # Create the URL for wolfram alpha API specific to our latex equation using appid
                self.string = "http://api.wolframalpha.com/v2/query?appid=" + app_id + "&input=solve+" + url_params

                # Call the Wolfram API function
                self.wolf(self.string)
        else:
            # If the system is not connected to the internet
            messagebox.showinfo("Connectivity", "Check your internet Connection")

    # It requests data from wolfram alpha and save all the result in a desired format
    def wolf(self, string):
        
        # Create request object for the URL
        req = Request(string)

        # Request html from the URL
        try : 

            html_page = urlopen(req)

            # Initialize result image counter
            count = 0
            soup = BeautifulSoup(html_page, "lxml")

            # Create container lists for step by step result
            img_links = []
            txt_links = []
        except :
            print("[INFO] Slow internet Connection")
        
        # Get all link on the HTML page
        for links in soup:
            s = str(links)
        tmp_text = [m.start() for m in re.finditer('false" id=',s)]
        tmp_image = [m.start() for m in re.finditer('src=',s)]

        # Get all images 
        for link in soup.findAll('img') :

            # Create a dummy name for a new result image
            name = "pic"+str(count)+".gif"

            # Retrieve the image
            urllib.request.urlretrieve(link.get('src'), name)

            # Append image to the container list
            img_links.append(name)

            # Increment the counter by 1
            count = count + 1
            
        # Populate the link container list
        for link in soup.findAll('pod') :
            txt_links.append(link.get('title'))

        # Initialize counters
        ta=0
        tb=0

        # Add results images to global variable pics
        for i in range(len(tmp_text)+len(tmp_image)) :  
            if tmp_text[ta]<tmp_image[tb] :
                globalinit.pics.append(txt_links[ta])
                ta+=1
            else :
                globalinit.pics.append(img_links[tb])
                tb+=1
            if ta==len(tmp_text) :
                for j in range(len(tmp_image)-tb) :
                    globalinit.pics.append(img_links[tb])
                    tb+=1
                break
            elif tb==len(tmp_image) :
                for j in range(len(tmp_text)-ta) :
                    globalinit.pics.append(txt_links[ta])
                    ta+=1
                break
                
        print("Saved")

        # Set background color
        self.frame_com = Frame(self,background="#232323")
        self.frame_com.pack(fill=X)

        # Create message container
        self.con = StringVar()

        # Print the confidence level in massage
        self.con.set('Confidence Level = '+str('%.2f' % self.confidence))
        label = tk.Label(self.frame_com, textvariable=self.con, font=tkfont.Font(family='Helvetica', size=12, slant="italic"),fg="#FFFFFF",bg="#232323")
        label.pack(side="left", fill="x", pady=0)

        self.frame_but = Frame(self,background="#232323")
        self.frame_but.pack(fill=X)

        # Button to call destroy function
        temp_button = tk.Button(self.frame_but, text = "Results",command = self.destroy,height=3,width=10)
        temp_button.pack(side="top")

    # Clear up memory
    def destroy(self) :
        try :
            self.frame_but.pack_forget()
            self.frame_com.pack_forget()
            self.frame_mathpix.pack_forget()
            self.frame_sol.pack_forget()

            # Go to the result page
            self.controller.show_frame("Result_Page")
            for files in globalinit.pics :
                if os.path.exists(files):
                    os.remove(files)
                else :
                    print(files,' Not found')
        except :
            print(Exception)
            pass
        
        # Got to the result page
        self.controller.show_frame("Result_Page")