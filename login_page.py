from tkinter import*
from tkinter import ttk
from voice_project import *
from maill import *
from send import *
def after_login():
    
    def success():
        send_screen.destroy()
        mailing()
    def success2():
        send_screen.destroy()
        send_message()
    global send_screen
    send_screen = Tk()
    send_screen.geometry("350x200")
    send_screen.title("Success")
    Label(send_screen, text="choose mail type", bg="blue").pack()
    Label(send_screen, text="").pack()
    b=Button(text="voice", height="40", width="40", command=success2)
    photo=PhotoImage(file="voice.gif")
    b.config(image=photo)
    b.pack()
    c=Button(text="text", height="40", width="40", command=success)
    photo1=PhotoImage(file="images.gif")
    c.config(image=photo1)
    c.pack()
    send_screen.mainloop()
