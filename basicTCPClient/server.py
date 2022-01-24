# TCP server

import socket

HOST = '192.168.0.16'
port = 9090

# DEFINE tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind ip a dn port to server

server_socket.bind((HOST, port))

server_socket.listen(5)

while True:
    communication_socket, address = server_socket.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode()
    print(f"Message from the client is: {message}")
    communication_socket.send(f"Got your message".encode())

