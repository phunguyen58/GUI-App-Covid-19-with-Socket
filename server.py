import socket
from tkinter import *

window = Tk()
window.title('Sever')
window.geometry('200x88')
PORT = 5656
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), PORT))
    s.listen(1)
    print("HOST: ", s.getsockname())
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
finally:
    s.close()
    sys.exit(0)

window.mainloop()