

import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "143.198.72.111"
port = 8757
s.bind((host, port))
print(socket.gethostname())
s.listen(5)

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
    c.send(''.join(socket.gethostname(), "says:", random.randint(0, 100)))
    c.close()