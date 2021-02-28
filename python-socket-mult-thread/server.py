import socket
import os
from _thread import start_new_thread
     
ip = "localhost"
port = 1234

global number_of_connections
number_of_connections = 0

server  = socket.socket()
server.bind((ip, port))
server.listen(5)

def handle_client(socket_client):
    global number_of_connections

    msg = "You are connected!"
    socket_client.send(msg.encode())

    name = socket_client.recv(1024)
    print("[#] client name:", name.decode())

    while True:
        request = socket_client.recv(1024)
        print("[{}] : ".format(name.decode()), request.decode())

        msg = request.decode()
        msg = msg.upper()
        socket_client.send(msg.encode())
       
        if not request:
            print("[#] {} desconnected".format(name.decode()))
            number_of_connections -= 1
            print("[#] clients connected : ", number_of_connections)
            break
    socket_client.close()

def engine():
    global number_of_connections

    print("[#] waiting for clients...")
  
    while True:
        client, address = server.accept()
        connection = (address[0], address[1])


        print("[#] new connection {} : {}".format(address[0], address[1]))
        start_new_thread(handle_client, (client, ))
        number_of_connections += 1
        print("[#] clients connected : ", number_of_connections)
    server.close()
 
engine()
