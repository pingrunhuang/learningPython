
import socket
import errno
import sys

IP = '127.0.0.1'
PORT = 1234
HEADERSIZE = 16

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

client_socket.setblocking(False)

my_username = input("username: ")
username = my_username.encode("utf-8")
username_header = f"{len(username)}:<{HEADERSIZE}".encode("utf-8")
client_socket.send(username_header + username)


while True:
    message = input(f"{my_username}> ")
    if message:
        message_length = len(message)
        message_header = f"{message_length}:<{HEADERSIZE}".encode("utf-8")
        client_socket.send(message_header+message.encode("utf-8"))

    
    try:
        while True:

            username_header = client_socket.recv(HEADERSIZE)

            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADERSIZE)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data, error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: {}'.format(str(e)))
        sys.exit()


