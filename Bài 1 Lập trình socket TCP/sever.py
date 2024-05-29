import socket

def sever():
    # lay dia chi 
    host = '127.0.0.1'
    port = 12000

    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4, TCP
    sever_socket.bind((host, port)) # dk ten cho socket, rang buoc dia chi vao socket

    sever_socket.listen(3) # gioi han so client duoc ket noi trong 1 thoi diem
    connect, address = sever_socket.accept() # chap nhan ket noi moi

    while True:
        # nhan data gioi han luong data 2048 bytes
        data = connect.recv(2048).decode()
        if data.lower().strip() == "bye":  
           break # huy ket noi neu nhan dc bye 
        print("Tu nguoi ket noi: " + str(data))
        data = data.upper() # dua du lieu thanh chu hoa
        connect.sendall(data.encode()) # gui tra ban sua doi ve client

    connect.close() # dong ket noi

if __name__ == '__main__':
    sever()  