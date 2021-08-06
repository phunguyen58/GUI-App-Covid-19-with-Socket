import socket
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#define color for UI
BUTTON_COLOR = "#EEE8AA"
HEADER_COLOR = "#9966FF"

window = Tk()
window.title('Client')
window.geometry('400x200')

header = Label(window, text = "COVID-19 INFORMATION", fg=HEADER_COLOR, font=("Arial", 20))
header.grid(row = 0, column = 1, pady = 15)

a = StringVar()
a.set("Input IP Address")
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
        messagebox.showinfo("", "Can't connect to server!")
    else:
        messagebox.showinfo("", "Connected to server!")
        FormLogin()

btnConnect = Button(window, text = "Connect", fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = butConnect_Click)
btnConnect.grid(row = 2, column = 1, pady = 10)

def exit(window_name):
    window_name.destroy()

#function for form login
def formLogin_btnLogin_click():
    #send data toi server va tra ve thong bao neu ko thanh cong
    loginDone = "Ok"
    if loginDone == "Ok":
        formLogin.withdraw()
        FormUser()
    else:
        messagebox.showinfo("", "Username or password went wrong!")

def formLogin_btnSignup_click():
    formLogin.withdraw()
    FormSignup()
################################
#fucntion for form signup
def formSignup_btnSignup_click():
    #send data toi server va tra ve thong bao neu thanh cong
    signUpDone = "Ok"
    if signUpDone == "Ok":
        messagebox.showinfo("", "Created account done!")
    else:
        messagebox.showinfo("", "Can't create account! Username existed")

def formSignup_btnLoginBack_click():
    formSignup.withdraw()
    FormLogin()
################################
def FormSignup():
    global formSignup
    formSignup = Toplevel()
    formSignup.title("Sign up")
    formSignup.geometry("406x240")
    #content of form signup
    formSignup_header = Label(formSignup, text = "Create Account", fg = HEADER_COLOR, font = ("Arial", 20))
    text_username = StringVar(formSignup)
    text_username.set("Username")
    text_pass = StringVar(formSignup)
    text_pass.set("Password")
    formSignup_username = Entry(formSignup, width = 36, textvariable = text_username)
    formSignup_pass = Entry(formSignup, width = 36, textvariable = text_pass)
    formSignup_btnSignup = Button(formSignup, text = "Create account", width = 12, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = formSignup_btnSignup_click)
    formSignup_btnLogin = Button(formSignup, text = "Return to Log in", width = 12, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = formSignup_btnLoginBack_click)
    formSignup_btnOut = Button(formSignup, text = "Exit", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = lambda: exit(window))
    #place of content in form
    formSignup_header.grid(row = 0, column = 1, pady = 15)
    formSignup_username.grid(row = 1, column = 1, padx = 100)
    formSignup_pass.grid(row = 2, column = 1, pady = 10)
    formSignup_btnSignup.grid(row = 3, column = 1, pady = 5) 
    formSignup_btnLogin.grid(row = 4, column = 1) 
    formSignup_btnOut.grid(row = 5, column = 1, pady = 5)
    #out window
    formSignup.protocol("WM_DELETE_WINDOW", lambda: exit(window))

def FormLogin():
    window.withdraw()
    #window form login
    global formLogin
    formLogin = Toplevel()
    formLogin.title("Log in")
    formLogin.geometry("406x240")
    #content of form login
    formLogin_header = Label(formLogin, text = "Login", fg = HEADER_COLOR, font = ("Arial", 20))
    text_username = StringVar(formLogin)
    text_username.set("Username")
    text_pass = StringVar(formLogin)
    text_pass.set("Password")
    formLogin_username = Entry(formLogin, width = 36, textvariable = text_username)
    formLogin_pass = Entry(formLogin, width = 36, textvariable = text_pass)
    formLogin_btnLogin = Button(formLogin, text = "Log in", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = formLogin_btnLogin_click)
    formLogin_btnSignup = Button(formLogin, text = "Sign up", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = formLogin_btnSignup_click)
    formLogin_btnOut = Button(formLogin, text = "Exit", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = lambda: exit(window))
    #place of content in form
    formLogin_header.grid(row = 0, column = 1, pady = 15)
    formLogin_username.grid(row = 1, column = 1, padx = 100)
    formLogin_pass.grid(row = 2, column = 1, pady = 10)
    formLogin_btnLogin.grid(row = 3, column = 1) 
    formLogin_btnSignup.grid(row = 4, column = 1, pady = 5) 
    formLogin_btnOut.grid(row = 5, column = 1)
    #out window
    formLogin.protocol("WM_DELETE_WINDOW", lambda: exit(window))
#function for form user
def formUser_btnSearch_click():
    searchDone = "Ok1"
    if searchDone != "Ok":
        messagebox.showinfo("", "Can't search! Please input again")
    else:
        pass
################################
def FormUser():
    global formUser
    #window form user
    formUser = Toplevel()
    formUser.title("Log in")
    formUser.geometry("520x420")
    #cotent of form user
    text_search = StringVar(formUser)
    text_search.set("Input country or province in Vietnam")
    formUser_header = Label(formUser, text = "Covid-19 Information", fg = "#9966FF", font = ("Arial", 20))
    formUser_search = Entry(formUser, width = 50, textvariable = text_search)
    formUser_btnSearch = Button(formUser, text = "Search", width = 6, fg = "black", bg = "#EEE8AA", font=("Arial", 9), command = formUser_btnSearch_click)
    textInfo = StringVar(formUser)
    textInfo.set("Country:  Vietnam\nCases:  189066\nCases today:  4009\nDeaths:  2720\nToday deaths:  0\nRecovered:  58040\nActive:  128306\nCritical:  0\nCases per one million:  1923\nDeaths per one million:  28\nTotal test:  11890084\nTest per one million:  120963")
    formUser_showInfo = Label(formUser, textvariable = textInfo, fg = "black", font = ("Arial", 10), bg = "#EEE5DE", width = 50, anchor = N)
    formUser_Out = Button(formUser, text = "Exit", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = lambda: exit(window))
    #place content in form user window
    formUser_header.grid(row = 0, column = 1, pady = 20, padx = 120)
    formUser_search.grid(row = 1, column = 1, padx = 60)
    formUser_btnSearch.grid(row = 2, column = 1, pady = 10)
    formUser_showInfo.grid(row = 3, column = 1, padx = 32, pady = 5)
    formUser_Out.grid(row = 4, column = 1, pady = 5)
    #out window
    formUser.protocol("WM_DELETE_WINDOW", lambda: exit(window))

window.mainloop()
