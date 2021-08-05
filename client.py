import socket
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Client')
window.geometry('400x200')

header = Label(window, text = "TRA CỨU COVID-19", fg="blue", font=("Arial", 20))
header.grid(row = 0, column = 1, pady = 15)

a = StringVar()
a.set("Nhập địa chỉ IP")
txtIP = Entry(window, width = 50, textvariable = a)
txtIP.grid(row = 1, column = 1, padx = 46)

def getValueTxtIP():
    inputValue = txtIP.get()
    return inputValue

def butConnect_Click():
    host = getValueTxtIP()
    test = True
    global client
    client = None
    # try:
    #     HOST = host
    #     PORT = 5656
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
    #     client.connect((HOST, PORT)) # tiến hành kết nối đến server
    # except:
    #     test = False
    #     client = None
    if test == False: 
        messagebox.showinfo("", "Kết nối với server không thành công")
    else:
        #messagebox.showinfo("", "Kết nối với server thành công")
        FormLogin()

def exit(window_name):
    window_name.destroy()

def btnLogin_click():
    pass

def btnSignup_click():
    pass

def FormLogin():
    window.withdraw()
    #window form login
    formLogin = Toplevel()
    formLogin.title("Login")
    formLogin.geometry("400x200")
    #content of form login
    formLogin_header = Label(formLogin, text = "Login", fg = "Blue", font = ("Arial", 20))
    text_username = StringVar(formLogin)
    text_username.set("Username")
    text_pass = StringVar(formLogin)
    text_pass.set("Password")
    formLogin_username = Entry(formLogin, width = 36, textvariable = text_username)
    formLogin_pass = Entry(formLogin, width = 36, textvariable = text_pass)
    formLogin_btnLogin = Button(formLogin, text = "Log in", width = 6, fg = "white", bg = "blue", font=("Arial", 9), command = btnLogin_click)
    formLogin_btnSignup = Button(formLogin, text = "Sign up", width = 6, fg = "white", bg = "blue", font=("Arial", 9), command = btnSignup_click)
    #place of content in form
    formLogin_header.grid(row = 0, column = 1, pady = 15)
    formLogin_username.grid(row = 1, column = 1, padx = 100)
    formLogin_pass.grid(row = 2, column = 1, pady = 10)
    formLogin_btnLogin.grid(row = 3, column = 1) 
    formLogin_btnSignup.grid(row = 4, column = 1, pady = 5) 
    #out window
    formLogin.protocol("WM_DELETE_WINDOW", lambda: exit(window))



btnConnect = Button(window, text = "Kết nối", fg = "white", bg = "blue", font=("Arial", 9), command = butConnect_Click)
btnConnect.grid(row = 2, column = 1, pady = 10)

window.mainloop()
