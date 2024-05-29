import socket

def client():
    host = '127.0.0.1'
    port = 12000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
    client_socket.connect((host, port)) # connect toi sever

    message = input(' : ') # nhan data
    
    while True:
        # nhan bye de dong connect
        client_socket.send(message.encode()) # gui data
        data = client_socket.recv(2048).decode() # nhan data tu sever
        if not data:
           break # neu ko nhan dc data break
        print("Nhan tu sever: " + data) # in trong terminal
        message = input(' : ')
    
    client_socket.close() # dong ket noi

if __name__ == '__main__':
    client()