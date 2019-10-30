import speech_recognition as sr
import pyttsx
from text_speech import *

import threading
from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("Automation", )
    root.geometry("500x300")

    heading = Label(root, text="Voice Input", font=("bold", 20))
    heading.grid(row=0, column=3)

    name = Label(root, text="subject", )
    name.grid(row=4, column=2)
    name_field = Entry(root)
    name_field.insert(END, '')
    name_field.grid(row=4, column=3, ipadx="100")   

    submit = Button(root, text="speak", fg="WHITE", bg="GREEN", command=speech_to_text)
    submit.grid(row=20, column=2)

    
    
    
    root.mainloop()




def speech_to_text():
 
 r = sr.Recognizer()
 with sr.Microphone() as source:
     text_to_speech("say something now")
     audio = r.listen(source)

 try:
     # for testing purposes, we're just using the default API key
     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
     # instead of `r.recognize_google(audio)`
     print("You said: " + r.recognize_google(audio))
 except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
 except sr.RequestError as e:
     print("Could not request results from Google Speech Recognition service; {0}".format(e))
 return str(r.recognize_google(audio))
