import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    while True:
        message=input("enter the message").encode("utf-8")
        print(f"sending {message} to server: ")
        client_socket.sendto(message,("localhost",1))
except:
    print("error occured")
    client_socket.close()