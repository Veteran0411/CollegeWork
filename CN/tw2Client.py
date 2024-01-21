import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address=("localhost",12345)

try:
    while True:
        message=input("enter message: ")

        print(f"sending {message}")
        sent=client_socket.sendto(message.encode(),server_address)

except Exception as e:
    print(f"An error occurred : ",e)

finally:
    print("closing socket")
    client_socket.close()