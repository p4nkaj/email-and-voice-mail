from tkinter import *
import os
from login_page import *
from recv import *
def send():
    main_screen.destroy()
    after_login()
def rec():
    main_screen.destroy()
    after_rec()


def send_rec():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Choose type")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Send mail", height="2", width="30", command = send).pack()
    Label(text="").pack()
    Button(text="recieve mail", height="2", width="30", command=rec).pack()
 
    main_screen.mainloop()
 
 

