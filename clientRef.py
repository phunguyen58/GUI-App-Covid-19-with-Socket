import socket
import pycountry#can tai
#define
PORT = 5566
SIZE = 1024
FORMAT = "utf-8"

def doConnect(host_IP, test):
    try:
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host_IP,PORT))
        print(f"[CONNECTED] Client connected to server at {HOST}:{PORT}")
        test = True
    except:
        test = False

def doLogin(username, password):
    client.send(b'login')
    check=client.recv(1024)
    if check ==b'fail':
        print('Chua co tai khoan nao duoc dang ki')
        client.send(b'ok')
        client.recv(1024)
    elif check ==b'success':
        client.send(username.encode())
        client.recv(1024)
        client.send(password.encode())
        client.recv(1024)
        client.send(b'ok')
        result= client.recv(1024)
    if result == b'yes':
        print("Dang nhap thanh cong")
        check_login = True
    elif result==b'no':
        print("Dang nhap that bai")
        check_login = False
    return check_login            

def doSingup(username, password):
    client.send(b'signup')
    client.recv(1024)
    client.send(username.encode())
    client.recv(1024)
    client.send(password.encode())
    client.recv(1024)
    client.send(b'ok')
    result= client.recv(1024)
    if result== b'yes':
        print('Dang ki thanh cong')
        check_signup = True
    elif result == b'no':
        print('Dang ki khong thanh cong')
        check_signup = False
    return check_signup

def clearName(text):
    text_clear = ""
    if len(text) == 2 and text.lower() != "vn" and text.lower() != "us" and text.lower() != "uk":
        text_clear = pycountry.countries.get(alpha_2 = text).name
    else:
        if text.lower() == "viet nam" or text.lower() == "vn":
            text_clear = "Vietnam"
        elif text.lower() == "united states of america" or text.lower() == "us" or text.lower() == "usa":
            text_clear = "USA"
        elif text.lower() == "uk" or text.lower() == "united of kingdom":
            text_clear = "UK"
        elif text.lower() == "south korea" or text.lower() == "korea":
            text_clear = "S. Korea"
        elif text.lower() == "congo":
            text_clear = "DRC"
        else:
            text_clear = text  
    return text_clear

def doSearch(search_text):
    client.send(b'search')
    client.recv(1024)
    if search_text[0:3].lower() == "vn/":
        print("Search in Vietnam")
        client.send(search_text.encode())
        province_info1 = client.recv(1024)
        province_info = province_info1.decode(FORMAT)
        return province_info
    else:
        print("Search whole of the world")
        search_text_clear = clearName(search_text)
        print(search_text_clear)
        client.send(search_text_clear.encode())
        country_info1 = client.recv(1024)
        conutry_info = country_info1.decode(FORMAT)
        return conutry_info

def doExit():
    print("Send exit")
    client.send(b'exit')
