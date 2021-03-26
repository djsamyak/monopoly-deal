import socket
import os
from _thread import *

def multi_threaded_client(connection):
    connection.send(str.encode('[UPDATE] Connected to Server'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print(f'[UPDATE] Server has started on {socket.gethostbyname(socket.gethostname())}\n')
ServerSideSocket.listen(5)

while True:
    Client, address = ServerSideSocket.accept()
    print(type(Client))
    print(f'Connected to {socket.gethostbyaddr(Client.getpeername()[0])[0]} on {address[0]}:{str(address[1])}')
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print(f'Thread Number: {str(ThreadCount)}\n')
ServerSideSocket.close()