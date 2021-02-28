import socket

ip = "localhost"
port = 1234

client = socket.socket()
client.connect((ip, port))

response = client.recv(1024)
print("[server] : ", response.decode())

name = str(input("insert you name: "))
client.send(name.encode())

while True:
    msg = str(input("Isert you message, or 'exit' to close: "))
    if msg == "exit":
        break
    client.send(msg.encode())

    response = client.recv(1024)
    print("[server] : ", response.decode())
client.close()
  