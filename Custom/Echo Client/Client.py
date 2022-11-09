import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message=int(input("Write a msg: "))
    custom=int(message)*3
    s.sendall(str(custom).encode())
    print("original Message",custom)
    data = s.recv(100024)

print(f"Echo From Server {data.decode()}")