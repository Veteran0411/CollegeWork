# udp
import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address=("localhost",12345)
server_socket.bind(server_address)

print("udp is waiting for response...")

while True:
    data,client_address=server_socket.recvfrom(1024) # 1024 bytes of data is received at a time
    print(f'received from, {client_address}: {data.decode()}')
    
#close the socket (this will never be executed)
server_socket.close()