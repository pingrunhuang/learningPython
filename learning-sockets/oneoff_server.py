import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print("Accepted connection from {}".format(address))
    msg = bytes("Hey there!!!!!", "utf-8")
    client_socket.send(msg)
    # mannually close the connection since the data already sent
    client_socket.close()

