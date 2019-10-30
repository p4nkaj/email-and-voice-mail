from tkinter import*
from tkinter import ttk
from voice_project import *
from rec import *
from listmessages import *

def hello():
    after_rec()
def after_rec():
    
    def voice_rec():
        rec_screen.destroy()
        print("voice mail are offline rn try again in some time")
        sleep(5000)
        hello()
        
    def text_rec():
        rec_screen.destroy()
        recv()
    global rec_screen
    rec_screen = Tk()
    rec_screen.geometry("350x200")
    rec_screen.title("Choose recieve type")
    Label(rec_screen, text="choose recieving type", bg="blue").pack()
    Label(rec_screen, text="").pack()
    bt=Button(text="voice", height="40", width="40", command=voice_rec)
    photo=PhotoImage(file="voice.gif")
    bt.config(image=photo)
    bt.pack()
    ct=Button(text="text", height="40", width="40", command=text_rec)
    photo1=PhotoImage(file="images.gif")
    ct.config(image=photo1)
    ct.pack()
    rec_screen.mainloop()
