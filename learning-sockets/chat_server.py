"""
#Aligning the text and specifying a width:

>>>
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char


example of data structure for communication:
{"header": "22       ", "data": b"hello world"}
"""
import socket
# for monitor socket purpose 
import select

IP = '127.0.0.1'
PORT = 1234
HEADERSIZE = 16

def receive_msg(client_socket):
    try:
        msg_header = client_socket.recv(HEADERSIZE)
        if not msg_header:
            return None
        
        # at the very beginning of the connection, a message length always comes the first 
        msg_length = int(bytes.decode(msg_header, 'utf-8').strip())
        ret = {"header": msg_header, "data": client_socket.recv(msg_length)}
        return ret
    except:
        return None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
# {client_socket_obj: data_in_communication}
clients = {}

while True:
    # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    print("Server started")
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # means a new client connected to the chat server
            client_socket, client_addr = notified_socket.accept()
            print("{} joint chatting...".format(client_addr))
            user = receive_msg(client_socket)
            if not user:
                # some error happen in the client side 
                continue
            
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print('Accepted new connection from {}:{}, username: {}'.format(*client_addr, user['data'].decode('utf-8')))
        else:
            # in this case, we are going to handle the msg sent from the user
            msg = receive_msg(notified_socket)
            if not msg:
                # the client exits
                print("Closed connection from {}".format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print("Received message:{} from {}".format(msg['data'].decode("utf-8"), user['data'].decode("utf-8")))
            # broadcast to all the other client except the sender
            for client_socket in clients:
                if client_socket != notified_socket:
                    # this can ensure that we can receive 2 times at client side with each length of HEADER_LENGTH
                    client_socket.send(user['header'] + user['data'] + msg['header'] + msg['data'])
            
    for notified_socket in exception_sockets:
        print("Error connection from {}".format(clients[notified_socket]['data'].decode('utf-8')))
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        continue

