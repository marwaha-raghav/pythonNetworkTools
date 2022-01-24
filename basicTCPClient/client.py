import socket
import threading

HOST = '192.168.0.16'
port = 9090

nickname = input("Enter your nickname: ")
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, port))

# socket.send("Hello server!".encode())
# print(socket.recv(1024).decode())


def receive():
    while True:
        try:
            message = socket.recv(1024).decode('ascii')
            if message == 'NICK':
                socket.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print("An error occured")
            socket.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        socket.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()





