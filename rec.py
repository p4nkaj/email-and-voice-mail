import easyimap
from tkinter import *

def recv():

    top=Tk()
    top.geometry("300x200")
    top.title("your mail")
    def recvv():
        try:
            login=t1.get()
            password=t2.get()
            no=t3.get()
            nom=int(no)
            imapper = easyimap.connect('imap.gmail.com', login, password)
            for mail_id in imapper.listids(limit=nom):
                mail = imapper.mail(mail_id)
                print(mail.from_addr)
                print(mail.to)
                print(mail.cc)
                print(mail.title)
                print(mail.body)
                print(mail.attachments)
        except:
            print("cant fatch all data due to security reason please try again")
        top.mainloop()
    t1=StringVar()
    t2=StringVar()
    t3=StringVar()
    login_id=Label(text="EMAIL ID:").grid(row=0,column=0,padx=10,pady=10)
    login_id_entry=Entry(text="",textvariable=t1).grid(row=0,column=1,padx=12,pady=12)
    password_id=Label(text="PASSWORD:").grid(row=1,column=0,padx=10,pady=10)
    password_id_entry=Entry(text="",show="*",textvariable=t2).grid(row=1,column=1,padx=12,pady=12)
    no_id=Label(text="NO OF MAIL:").grid(row=2,column=0,padx=10,pady=10)
    no_id_entry=Entry(text="",textvariable=t3).grid(row=2,column=1,padx=12,pady=12)

    button=Button(text="RECIEVE",bg="RED",command=recvv).grid(row=4,column=0,padx=10,pady=10)



