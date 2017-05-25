import socket

s=socket.socket()
host="192.168.178.45"
port=6666

s.connect((host, port))

t=s.recv(1024)
t=t.decode("utf-8")
print(t)
