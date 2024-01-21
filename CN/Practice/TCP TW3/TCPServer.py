import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("localhost",2))
server_socket.listen(1)
print("TCP server is listening")

try:
    while True:
        client_socket,client_address=server_socket.accept()
        print(f"received from client address: {client_address}")
        data=client_socket.recv(1024)
        print(f"received data from client:{data.decode()}")
        client_socket.sendall(b"hello,client")
except:        
    client_socket.close()