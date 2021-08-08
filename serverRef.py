import socket
import tkinter as tk
import json
import time
import schedule
import threading
import sys
import os
from _thread import *
from tkinter import *
from tkinter import messagebox
import getAPI#file local
import getDatabase#file local

#define
BUTTON_COLOR = "#EEE8AA"
HEADER_COLOR = "#9966FF"

#define
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
filename='login.json'

global checkShutdown
checkShutdown = 0
def btnOut_click():
    global checkShutdown
    checkShutdown = 1
    sys.exit(0)
    
def btnRenew_click():
    print("Renewed!")

def getAPIdata():
    getAPI.getData()
    schedule.every(30).seconds.do(getAPI.getData)
    while True:
        if checkShutdown == 1:
            break
        schedule.run_pending()
        time.sleep(1)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        data = conn.recv(1024)
        #dang nhap
        if data==b'login':
            filesize = os.path.getsize(filename)
            if filesize == 0:
                print("Chua co tai khoan nao duoc dang ki")
                conn.send(b'fail')
                conn.recv(1024)
                conn.send(b'ok')
            else:
                conn.send(b'success')
                username1= conn.recv(1024)
                conn.send(b'ok')
                password1= conn.recv(1024)
                conn.send(b'ok')
                username=username1.decode(FORMAT)
                password=password1.decode(FORMAT)
                with open(filename, "r") as readinfo:
                    datastore = json.load(readinfo)
                check=False
                for person in datastore['user']:
                    if person['username']== username:
                        if person['password'] == password:
                            check=True
                  # kiem tra dang nhap     
                if check == True:
                    conn.recv(1024)
                    conn.send(b'yes')
                else:
                    conn.recv(1024)
                    conn.send(b'no')
        #dang ki
        elif data== b'signup':
            conn.send(b'ok')
            username1= conn.recv(1024)
            conn.send(b'ok')
            password1= conn.recv(1024)
            conn.send(b'ok')
            username=username1.decode(FORMAT)
            password=password1.decode(FORMAT)
            check=True
            filesize = os.path.getsize(filename)
            conn.recv(1024)
            if filesize==0:
                conn.send(b'yes')
                data = {}
                data['user'] = []
                data['user'].append({
                        'username': username,
                         'password': password
                    })
                with open ('login.json' , 'w') as writefile:
                    json.dump(data, writefile)
            else: 
                with open("login.json", "r") as readinfo:
                    datastore = json.load(readinfo)
                for person in datastore['user']:
                    if person['username'] == username:
                        check=False
                if check==True:
                    conn.send(b'yes')
                    data = {}
                    data['user'] = []
                    for person in datastore['user']:
                        data['user'].append({
                            'username' : person['username'],
                            'password': person['password'],
                        })
    
                    data['user'].append({
                        'username': username,
                         'password': password
                    })
                    with open ('login.json' , 'w') as writefile:
                        json.dump(data, writefile)
                elif check== False:
                    conn.send(b'no')
        elif data == b'search':
            conn.send(b"ok")
            name_search1 = conn.recv(1024)
            name_search = name_search1.decode(FORMAT)
            if name_search[0:3].lower() == "vn/":
                name_search_VN = name_search.replace(name_search[0:3],"")
                name_clear = clearNameInVN(name_search_VN)
                print(name_clear)
                province_info = getDatabase.readDataInVN(name_clear)
                print(province_info)
                conn.send(province_info.encode())
            else:
                print(name_search)
                country_info = getDatabase.readDataByCountry(name_search)
                print(country_info)
                conn.send(country_info.encode())
        elif data==b'exit':
            break
    conn.close()
    sys.exit(0)

def clearNameInVN(name_search):
    if len(name_search) > 3 or name_search.lower() == "hue":
        if name_search.lower() == "hue" or name_search.lower() == "thua thien hue":
            return "Thua Thien - Hue"
        elif name_search.lower() == "ba ria vung tau" or name_search.lower() == "vung tau" or name_search.lower() == "ba ria":
            return "Ba Ria - Vung Tau"
        elif name_search.lower() == "tp hcm" or name_search.lower() == "tp.hcm" or name_search.lower() == "tphcm":
            return "TP. Ho Chi Minh"
        else:
            return name_search
    else:
        pass


def showUIServer():
        global window
        window = Tk()
        window.title('Server')
        window.geometry('400x450')
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

def runServer():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    thread1 = threading.Thread(target=showUIServer)
    thread1.start()
    while True:
        if checkShutdown == 1:
            break
        conn, addr = server.accept()
        thread2 = threading.Thread(target=handle_client, args=(conn, addr))
        thread2.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 4}")
        if threading.activeCount() - 4 == 0:
            break

    thread1.join()
    thread2.join()
    

    

    