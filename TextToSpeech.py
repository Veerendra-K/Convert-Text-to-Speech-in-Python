#Create the GUI application main window.
#By importing toolkit interface(tkinter module as tk)
import tkinter as tk

#From tkinter module importing all the packages
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.ttk import Combobox

#importing a text-to-speech converter library in Python
#Note: it works offline as well not required data connection
import pyttsx3

#importing Google Text Translater(gTTS)API for converting text into speech
#Note: it works only when Data/Internet is connected
from gtts import gTTS

#This module is imported so that we play the converted audio  
import os
from playsound import playsound

#Generates the random number series for saving audio file(mp3)
import random


#imported all the required modules

#variable created for Tk() called 'root' 
root = Tk()
#Title given for Python GUI window.
root.title("Text to Speech Converter")
#Size assigned to GUI window
root.geometry("1000x580+200+80")
#If we use arguments as FALSE so that we can't do window Minimization/Maximization.
#If you wanna change window size use TRUE then only it can be changable/Re-sizable
root.resizable(False, False)
#Added Background color
root.configure(bg="#fff300")


#tts nothing but it is just text to speech
tts = pyttsx3.init()
def speaknow():
    text = text_box.get(1.0, END)
    gender= gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')
    final = gTTS(text = text)
    v = random.randint(1,10000000)
    audio_file = str(v) + '.mp3'
    final.save(audio_file)
    #playsound(audio_file)  #==> Not required actually! if u gonna use this, You will ear both the voices! It'll play(speak) GUI's sound as well as ur system music player sound(together).
    #os.remove(audio_file)  #==> It will remove converted mp3 from files.
    #tts.save_to_file(text, "C:\\Users\\Veerendra\\Desktop\\audio.mp3") if you wanna save that converted mp3 file in particular location u can use this line of code.
    

    def setvoice():
        if(gender == 'Male'):
            tts.setProperty('voice', voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()

    if(text):
        if(speed == 'Fast'):
            tts.setProperty('rate',250)
            setvoice()
        elif(speed == 'Medium'):
            tts.setProperty('rate',150)
            setvoice()
        else:
            tts.setProperty('rate',80)
            setvoice()



#Here I added random logo(G-down) to GUI window
logo = PhotoImage(file = "F:\MyMemories\img\logo.png")
Label(root, image = logo, bg = "#fff300").place(x=750, y=510)

#Then here I'm going to change default'=FALSE' icon of GUI window.
logo_image = PhotoImage(file = "F:\\MyMemories\\img\\icon2.png")
root.iconphoto(False, logo_image)



#Frame added at the upper of page
upper_frame = tk.Frame(root, bg="#14A7DD", width = 1200, height = 130)
upper_frame.place(x=0, y=0)

#picture added on upper_frame which is looks like speech icon
picture = PhotoImage(file = "F:\\MyMemories\\img\\frame-img.png")
Label(upper_frame, image = picture, bg="#14A7DD").place(x=130, y=10)

Label(upper_frame, text="Text to Speech Converter",  font="TimesNewroman 40 bold", bg="#14A7DD", fg='white').place(x=250, y=35)



#Text box created for taking inputs from the User
text_box = Text(root, font="calibri 20", bg="white", relief = GROOVE, wrap= WORD, bd=0)
text_box.place(x=30, y=150, width=940, height=180)




#Creating box which is called gender_box with option to select gender
gender_box = Combobox(root, values=['Male', 'Female'], font="Robote 12", state='r', width=12)
gender_box.place(x=340, y=400)
gender_box.set('Select')

#Creating another box called speed_box with option to select speed
speed_box = Combobox(root, values=['Fast', 'Medium', 'Slow'], font="Robote 12", state='r', width=12)
speed_box.place(x=540, y=400)
speed_box.set('Select')

#Adding some Text to gender_box & speed_box 
Label(root, text="Select Voice", font='TimesNewroman 15 bold', bg="#fff300", fg="#000").place(x=340, y=370)
Label(root, text="Select Speed", font='TimesNewroman 15 bold', bg="#fff300", fg="#000").place(x=540, y=370)



#Creating Play button for output/Sound
play_button = ImageTk.PhotoImage(file="F:\\MyMemories\\img\\playbtn.png")
play_btn = Button(root, text="Play", compound= LEFT, image= play_button, bg='white', width = 110, height = 60, font="arial 14 bold", borderwidth='0.1c', command=speaknow)
play_btn.place(x=425, y=455)



