import socket # import thu vien

host = socket.gethostbyname(socket.gethostname()) # lay ip-address cua may
print(host)
for port in range(5000):
    try:
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tao socket
        sock.bind((host, port)) # dk ten cho host rang buoc dia chi voi host

    except:

        print('[OPEN] Port open : ', port) # in port len terminal

    sock.close() # dong ket noi    