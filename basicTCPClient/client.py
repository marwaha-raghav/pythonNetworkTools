import socket

HOST = '192.168.0.16'
port = 9090

socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,port))

socket.send("Hello server!".encode())
print(socket.recv(1024).decode())