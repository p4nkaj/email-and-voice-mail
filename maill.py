import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# smtp.mail.yahoo.com
import time
from tkinter import *
from tkinter import ttk
import math

def mailing():
    def sentBox():
        root.destroy()
        global main_screen
        main_screen = Tk()
        main_screen.geometry("350x200")
        main_screen.title("Success")
        Label(main_screen, text="Mail Sent ", bg="blue").pack()
        Label(main_screen, text="").pack()
        Button(text="Success", height="20", width="180", command=success).pack()
     
        main_screen.mainloop()
    def success():
        main_screen.destroy()


    class Application(Frame):
        """ Gui Application """
        
        def __init__(self, master):
            """ initialize the Frame """
            ttk.Frame.__init__(self, master)

            self.grid()
            self.create_widgets()

        def create_widgets(self):

            myfont = ('', 14, 'bold')
            # row 0
            #create first button
            self.btnConnect = Button(self,  font=myfont, text = "Send Mail", bg='red', fg='white', command=self.send_mail).grid(row=0, column=0, sticky=W)
            self.btnConnect = Button(self,  font=myfont, text = "multi mail", bg='red', fg='white', command=self.send_mail2).grid(row=1, column=0, sticky=W)

            self.label7 = Label(self, font=myfont, text='User name: ').grid(row=1, column=0, pady=10, padx=10, sticky=E)

            self.cbusername = ttk.Entry(self, font=myfont, width=40, textvariable=UN)
            
            self.cbusername.grid(row=1, column=1, pady=10, padx=10)

            self.label8 = Label(self, font=myfont, text='Password: ').grid(row=2, column=0, pady=10, padx=10, sticky=E)
            self.cbpassword = ttk.Entry(self, font=myfont, width=40, textvariable=PW)
            
            self.cbpassword.grid(row=2, column=1, pady=10, padx=10)
            self.cbpassword.config(show='*')


            # row 1
            # create label for To:
            self.label1 = Label(self, font=myfont, text='To: ').grid(row=3, column=0, pady=10, padx=10, sticky=E)

            # create combo box for the address
            self.cbToEmail = ttk.Combobox(self, font=myfont, width=40, textvariable=varTo)
            self.cbToEmail['values'] = ('pkjjass@gmail.com', 'admin@yahoos.com', 'bobhatesthat@yahoo.com', 'pankajjb93@gmail.com')
            self.cbToEmail.grid(row=3, column=1, pady=10, padx=10)
            
            # row 2
            # create label from
            self.label2 = Label(self, font=myfont, text='From: ').grid(row=4, column=0, pady=10, padx=10, sticky=E)

            # create combo box for the address
            self.cbFromEmail = ttk.Combobox(self, font=myfont, width=40, textvariable=varFrom)
            self.cbFromEmail['values'] = ('pankajjb93@gmail.com',
                                          'pkjjass@gmail.com',
                                          'evil_corp@yahoo.com')
            self.cbFromEmail.grid(row=4, column=1, pady=10, padx=10)
            
            # row 3
            # create label list of email addresses
            self.label3 = Label(self, font=myfont, text='Subject: ').grid(row=5, column=0, pady=10, padx=10, sticky=E)
            
            # create combo box for the address
            self.cbSubject = ttk.Combobox(self, font=myfont, width=40, textvariable=varSubject)
            self.cbSubject['values'] = ('hello testing', 'yo boy')
            self.cbSubject.grid(row=5, column=1, pady=10, padx=10)
            
            # row 4
            # create label list of email addresses
            self.label2 = Label(self, font=myfont, text='Address list name: ').grid(row=6, column=0, pady=10, padx=10, sticky=E)

            # create combo box for the address
            self.cbEmail_List = ttk.Combobox(self, font=myfont, width=40, textvariable=varEmail_List)
            self.cbEmail_List['values'] = ('adresses_email.txt',
                                           'Test_adresses_email.txt')
            self.cbEmail_List.grid(row=6, column=1, pady=10, padx=10)
            
            # row 5
            # create text box to hold the text for the letter
            self.text = Text(self, font=('', 12), width=90, height=25)
            self.text.grid(row=7, column = 0, columnspan=2, padx=5, pady=5, sticky='nsew')
            
            self.scrollb = Scrollbar(self, command=self.text.yview)
            self.scrollb.grid(row=7, rowspan=8, column=2, columnspan=2, pady=10, sticky='nse')
            self.text['yscrollcommand'] = self.scrollb.set

            



        def send_mail(self):
            
            from_address = varFrom.get() # get the address from the combobox who is sending the email example: 'sender_name@yahoo.com' 
            to_address = varTo.get() # get the address from the combobox for example: 'receiver_name@gmail.com'

                        
            text_Letter = self.text.get('1.0', END) # select all text in the listbox 


            
            U_N=UN.get()
            P_W=PW.get()
            subject_text = varSubject.get() # gets the contents of the combo box for the subject line
            
            username = U_N # use your email address as the username
            password = P_W # password used to login to your email account
     
            
            
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject_text 
            msg.attach(MIMEText(text_Letter))
            server = smtplib.SMTP(host='smtp.gmail.com',port=587) # for gmail use: smtp.gmail.com
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.sendmail(from_address,to_address,msg.as_string())
        
            
            server.quit()
            file = open(r"C:\Users\pk\Desktop\outlook\mailService.txt", "a")
            file.write(from_address + "\n")
            file.write(to_address+"\n")
            file.write(subject_text + "\n")
            file.write(text_Letter + "\n")
            file.close()

            sentBox()
        def send_mail2(self):

        
            
            
            from_address = varFrom.get() # get the address from the combobox who is sending the email example: 'sender_name@yahoo.com' 
            to_address = varTo.get() # get the address from the combobox for example: 'receiver_name@gmail.com'

            file_to_open = varEmail_List.get()# get address text file from combobox on form
            address_text = open(file_to_open,'r') # read the file
            my_addresses = address_text.readlines() # read each line in text file
            address_text.close() # close text file

            
            text_Letter = self.text.get('1.0', END) # select all text in the listbox 


            counter = 1 # create a varialbe to increase an integer
            # loop through all the addresses and print them
            for line in my_addresses:
                print (counter, line)
                counter +=1
       
            subject_text = varSubject.get() # gets the contents of the combo box for the subject line
            
            username = UN  # use your email address as the username
            password = PW # password used to login to your email account
     
            b=1 # create a counter set it to start at 1
            
            # how many email addresses to process
            list_length = len(my_addresses)
            t = list_length 
            print ('How many in the list', list_length)
            
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject_text 
            msg.attach(MIMEText(text_Letter))
            server = smtplib.SMTP(host='smtp.gmail.com',port=587) # for gmail use: smtp.gmail.com
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.sendmail(from_address,to_address,msg.as_string())
        
            for atoaddress in my_addresses: # loop through each email address
                ti = t % 12 # divide number by 12 send 12 at a time
                if ti == 0: # if when you divide the number by 12 you get zero
                    server.sendmail(from_address,atoaddress,msg.as_string())
                    print (b, ' sent ', atoaddress) # print the address that you sent the mail to
                    time.sleep(2)
                    server.quit() # quit or close the server
                    print ('it_quit')
                    time.sleep(8) # sleeps for 8 seconds
                    msg = MIMEMultipart() # re-connects and continues the main loop
                    msg['From'] = from_address
                    msg['To'] = to_address
                    msg['Subject'] = subject_text
                    msg.attach(MIMEText(text_Letter))
                    server = smtplib.SMTP(host='smtp.gmail.com',port=587) # for gmail use: smtp.gmail.com
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(username, password)
                    b+=1
                    t-=1
                else:
                    server.sendmail(from_address,atoaddress,msg.as_string())
                    print (b, ' sent ', atoaddress)
                    b+=1
                    t-=1
                    time.sleep(6)
            server.quit()
            sentBox()



    root = Tk()
       
    root.title("email program ")
    root.geometry("1040x825")
    """root.bind("", keydown)
    root.bind("", keyup)"""
    root.attributes("-topmost", True)
    UN = StringVar(root, value='your email address')
    PW = StringVar(root, value='your password')
    varTo = StringVar(root, value='to_address@gmail.com')
    varFrom = StringVar(root, value='from_address@yahoo.com')
    varText_Letter = StringVar()
    varSubject = StringVar(root, value='type subject')
    varEmail_List = StringVar(root, value='adresses_email.txt')
    app = Application(root)

    root.mainloop()

