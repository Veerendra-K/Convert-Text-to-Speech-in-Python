# Convert-Text-to-Speech-in-Python
- <strong>Text to speech is a process to convert any text into voice. Text to speech project takes words on digital devices and convert them into audio with a button click or finger touch. Text to speech python project is very helpful for people who are struggling with reading.</strong></br>


# ![Result image](https://github.com/Veerendra-K/Convert-Text-to-Speech-in-Python/blob/main/Results/Result.png "Result Image") #

# Project Prerequisites
- To implement this project, we will use the basic concepts of Python, Tkinter, gTTS, and playsound libraries.

  - Tkinter is a standard GUI Python library that is one of the fastest and easiest ways to build GUI applications using Tkinter.
  - gTTS (Google Text-to-Speech) is a Python library, which is a very easy library that converts the text into audio.
  - The playsound module is used to play audio files. With this module, we can play a sound file with a single line of code.
  
     # To install the required libraries, you can use pip install command:
  
                 pip install tkinter
                 pip install gTTS
                 pip install playsound
    
    
  # Text to Speech Python Project
  -  The objective of this project is to convert the text into voice with the click of a button. This project will be developed using Tkinter, gTTs, and playsound library.

  -  In this project, we add a message which we want to convert into voice and click on play button to play the voice of that text message.

           * Importing the modules
           * Create the display window
           * Define functions 
    
<h3><bold>So these are the basic steps that we will do in this Python project. Let’s start.</bold></h3>

# 1. Import Libraries
 - Let’s start by importing the libraries: tkinter, gTTS, and playsound
 
          from tkinter import *
          From gtts import gTTS
          From playsound import playsound
          
# 2. Initializing window

             root = Tk()
             root.title("Text to Speech Converter")
             root.geometry("1000x580+200+80")
             root.configure(bg="#fff300")
             root.resizable(False, False)
             
             
- <strong>Tk()</strong> to initialized tkinter which will be used for GUI</br>
- <strong>geometry()</strong> used to set the width and height of the window</br>
- <strong>configure()</strong> used to access window attributes</br>
- <strong>bg</strong> will used to set the color of the background</br>
- <strong>title()</strong> set the title of the window

