# tcp client
import socket 

def start_client():
    while True:
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(("localhost",2))
        
        da=input("enter data to send to server: ").encode("utf-8")
        client_socket.sendall(da)
        data=client_socket.recv(1024)
        print(f"data received:{data.decode()}")
        client_socket.close()
    
if __name__=="__main__":
    start_client()
