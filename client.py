import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('143.198.72.111', 8757))

s.send('hello from {0}'.format(socket.gethostname()).encode('utf-8'))

while True:
    recieve = s.recv(1024).decode('utf-8')
    # recieve = recieve.decode('utf-8')
    if len(recieve) > 0:
        print(recieve, type(recieve), len(recieve))
        # s.send('recieved'.encode('utf-8'))
        # break