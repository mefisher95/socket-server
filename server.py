

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7000
s.bind((host, 1234))
print(socket.gethostname(), 1234)
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
    c.send(input().encode('utf-8'))
    c.close()