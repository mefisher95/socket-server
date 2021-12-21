

import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "143.198.72.111"
port = 8757
s.bind((host, port))
print(socket.gethostname())
s.listen(5)
conn_list = []

def manage_conn(new_con: tuple):
    conn_list.append(new_con)
    print(new_con)

while True:
    # now our endpoint knows about the OTHER endpoint.
    # clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established.")
    # clientsocket.send(bytes("Hey there!!!","utf-8"))
    # clientsocket.close()
    c, addr = s.accept()
    
    print("connected to ", addr)
    print(c.recv(1024))
    # c.send('we are talking...!!!'.encode('utf-8'))
    # manage_conn((c, addr))
    conn_list.append(addr)
    print(conn_list)
    c.send(' '.join([socket.gethostname(), "says:", str(random.randint(0, 100))]).encode('utf-8'))
    print(c)
    c.close()