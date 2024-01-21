import socket
try:
    while True:
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(("localhost",2))
        data=input("enter data to send: ").encode("utf-8")
        client_socket.sendall(data)
        data=client_socket.recv(1024)
        print(f"response from server: {data.decode()}")
except:       
    client_socket.close