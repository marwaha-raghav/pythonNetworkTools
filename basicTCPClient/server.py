# TCP server

import socket
import threading

HOST = '192.168.0.16'
port = 9090

# DEFINE tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind ip a dn port to server

server_socket.bind((HOST, port))

server_socket.listen(5)

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        communication_socket, address = server_socket.accept()
        print(f"Connected to {address}")
        communication_socket.send('NICK'.encode('ascii'))
        # message = communication_socket.recv(1024).decode()
        # print(f"Message from the client is: {message}")
        # communication_socket.send(f"Got your message".encode())
        nickname = communication_socket.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(communication_socket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the server.".encode('ascii'))
        communication_socket.send("Connected to the server".encode())

        thread = threading.Thread(target=handle, args=(communication_socket,))
        thread.start()


print("Server Listening")
receive()






