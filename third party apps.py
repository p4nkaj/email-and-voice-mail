from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from tkinter import *


def first():
    ide=t1.get()
    psw=t2.get()
    driver=webdriver.Chrome("C:\software\chromedriver.exe")

    driver.get("https://accounts.google.com/signin")
    email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
    email_phone.send_keys(ide)
    driver.find_element_by_id("identifierNext").click()
    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    password.send_keys(psw)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(3)
    driver.get("https://myaccount.google.com/lesssecureapps")



top=Tk()
top.geometry("300x200")
top.title("your mail")
t1=StringVar()
t2=StringVar()

login_id=Label(text="EMAIL ID:").grid(row=0,column=0,padx=10,pady=10)
login_id_entry=Entry(text="",textvariable=t1).grid(row=0,column=1,padx=12,pady=12)
password_id=Label(text="PASSWORD:").grid(row=1,column=0,padx=10,pady=10)
password_id_entry=Entry(text="",show="*",textvariable=t2).grid(row=1,column=1,padx=12,pady=12)


button=Button(text="RECIEVE",bg="RED",command=first).grid(row=4,column=0,padx=10,pady=10)



