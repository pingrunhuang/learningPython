import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ""
# the reason why we have while loop here is for recieving data from server streamingly
while True:
    res = s.recv(8)
    # this block indicate when do we exit the receiving process
    if len(res) <= 0:
        break
    else:
        full_msg += bytes.decode(res, 'utf-8')
if full_msg:
    print(full_msg)