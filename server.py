from CryptoLibrary import Encryption,RSA_encryption
import socket
import threading
import time


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()),999))

private = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDoLiYsRT56t1inNddmjUdlbT/UVsw3FZYQLSyhgnuxB8QZVx1v
AbVmTczRML3vpcG9VRPNJATAnIO8gce6L8MG9guL+PwU/LwezNLAorwxyHXOZAsH
NvWI9l0+a3Y1AuEH2AQNPBs4fOJPOY1u3QqmedOUgYKZXkKmV+H9auPu5QIDAQAB
AoGASh91k1uV20KOXG99cWF4IiLTJlyBfLJ5AngRkAxipb1HdxmPLYG7okoDMeOg
N5JQ/Dtdg3fUxpMRIYzDMScPWR047k4hhMTDDi4HiyVBtQKl0t5z47oZEWMpAdV7
hnDPjdaRHtAMoo5F0Vr8htxAfHZNEfrzjoO52UySWaQ8578CQQDoOiobitHGB2gn
BhToDEH1wUQwr/fEH7CcJf0MAV/8lTSJPY0O8j+nPj0kSZIbdMKsrBDpn2i3EJin
f6c++SmLAkEA//LBL5nJxxnK8H06lSsiVWJBSPwx/vwZmiw7K2bPn+PgM90W0cXT
TYiFQmwQepo01y/qnffWjXWkjijD7iH3TwJALkx6XKdej0amwzD5NhJLjD2N5M8Q
bK+MvHTucFhN1MPCh6IX32T4v9Uux29Li+HJdjeP36QCco0CglJ2+50dZQJAKiin
T5rqVKRX/DL0cluvhRbxH/+CkLif0vhUKrr9mh2j8YcKWjVWr9+764v3TuqVp5hZ
8fk/2v80wsHOPCxWGwJAeEp6/6CPBox47XaAqoJQ8Rzcl2kcOn1khbBapDnnIOeZ
xEnxvc7ynxU/AflgJwPSkojC9WobHlnsR+3PJwp5ug==
-----END RSA PRIVATE KEY-----'''

privateKey = RSA_encryption().import_rsa_private_key(private.encode())

def recvkey(conn):
    while True:
        try:
            encKey = conn.recv(128)
            key = RSA_encryption().rsa_decrypt(privateKey,encKey)
            cipher = Encryption(key)
            conn.send(b'r')
            if conn.recv(1) == b'r':
                return cipher
        except Exception as e:
            pass
        time.sleep(0.5)

def listen(server):
    server.listen()
    print("{+} Server is listening on "+socket.gethostbyname(socket.gethostname())+" ...")
    while True:
        conn,addr = server.accept()
        host = addr[0]
        print('New client connection '+ host+' !')
        cipher = recvkey(conn)
        t = threading.Thread(target=onConnect,args=(conn,host,cipher))
        t.start()

def onConnect(conn,host,cipher):
    while True:
        command = input(host+' -> ')
        sendMessage(conn,command,cipher)
        print(receive(conn,cipher).decode())

        
def sendMessage(conn,message,cipher):
    message = cipher.encrypt(message.encode())
    header = str(len(message))
    conn.send(header.encode())
    conn.send(message)
    
    
def receive(conn,cipher):
    while True:
        try:
            header = int(conn.recv(64).decode())
            return cipher.decrypt(conn.recv(header))
        except Exception as e:
            pass
        time.sleep(0.5)
    
listen(server)


