# echo-client.py

import socket
from turtle import st

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message=int(input("Write a msg: "))
    s.sendall(str(message).encode())
    print("original Message",int(message)+2)
    data = s.recv(1024)

print(f"Echo From Server {data.decode()}")