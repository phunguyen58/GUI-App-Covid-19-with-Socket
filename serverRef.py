import socket
import tkinter as tk
import getAPI
import time
import schedule
import sys
from tkinter import *
from tkinter import messagebox

global checkShutdown
checkShutdown = 0
def btnOut_click():
    global checkShutdown
    checkShutdown = 1
    sys.exit(0)
    
def btnRenew_click():
    print("Renewed!")

def showServerUI():
    #define color for UI
    BUTTON_COLOR = "#EEE8AA"
    HEADER_COLOR = "#9966FF"
    global window
    window = Tk()
    window.title('Server')
    window.geometry('400x450')
    # PORT = 5656
    # try:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     s.bind((socket.gethostname(), PORT))
    #     s.listen(1)
    #     print("HOST: ", s.getsockname())
    #     conn, addr = s.accept()
    #     with conn:
    #         print('Connected by', addr)
    #         while True:
    #             data = conn.recv(1024)
    # finally:
    #     s.close()
    #     sys.exit(0)
        
    #content UI in server
    header = Label(window, text = "SERVER MANAGER", fg=HEADER_COLOR, font=("Arial", 18))
    btnRenew = Button(window, text = "Renew", width = 6, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = btnRenew_click)
    textShowUser = Text(window, font=("Arial", 9), height = 20, width = 50)
    btnOut = Button(window, text = "Shut down server", width = 15, fg = "black", bg = BUTTON_COLOR, font=("Arial", 9), command = btnOut_click)
    #place content UI in server
    header.grid(row = 0, column = 1, pady = 10, padx = 85)
    btnRenew.grid(row = 1, column = 1)
    textShowUser.grid(row = 2, column = 1, pady = 10)
    btnOut.grid(row = 3, column = 1, pady = 5)
    window.mainloop()

def getAPIdata():
    getAPI.getData()
    schedule.every(5).seconds.do(getAPI.getData)
    while True:
        if checkShutdown == 1:
            break
        schedule.run_pending()
        time.sleep(1)