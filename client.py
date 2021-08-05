import socket
import sys

print(socket)
host = socket.gethostname();
print(socket.gethostbyname(host))
# AF_INET == the address family ipv4
# SOCKET_STREAM == connection orientated TCP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
port = 777 # this is the default port for socket

try:
    host_ip = socket.gethostbyaddr('127.0.0.1')
    print(host_ip)

except socket.gaierror:
    print('weve had an error')
    sys.exit()

s.connect((host_ip[2][0], port))
s.send('hello from the client side'.encode('utf-8'))
print(s.recv(1024))
