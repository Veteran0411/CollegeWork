import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    while True:
        message=input("enter the message u want to send: ")
        print(f"sending: {message}")
        client_socket.sendto(message.encode("utf-8"),("localhost",12345))
except Exception as e:
    print(f"error occurred: {e}")

finally:
    client_socket.close()