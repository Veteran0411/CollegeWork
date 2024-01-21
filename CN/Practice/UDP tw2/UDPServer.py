import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('localhost',12345))
print(f"udp is waiting for response: ")
try:
    while True:
        data,client_address=server_socket.recvfrom(1024)
        print(f"data received from client: {data.decode()}")
except Exception as e:
        print(f"error occurred: {e}")
    
finally:
    server_socket.close()