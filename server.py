import socket

s = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection with {address} established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
