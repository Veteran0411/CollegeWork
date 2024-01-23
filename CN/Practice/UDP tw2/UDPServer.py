import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(("localhost",1))
print("UDP server is listening")
try:
    while True:
        data,client_address=server_socket.recvfrom(1024)
        print(f"receiving from {client_address}")
        print(f"data is: {data.decode()}")
except:
    server_socket.close()
    
    