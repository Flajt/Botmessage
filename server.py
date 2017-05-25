import socket
import threading

s=socket.socket()
host="192.168.178.45"
port=6666


s.bind((host, port))
while True:
    s.listen(100)

    c, addr=s.accept()
    message=c.recv(1024)
    message=c.decode(message)


if message=="setup":        #Regestrieren auf dem Server mit Identifikations nummer (soll individuell zugeteilt werden)
    setup()

if message=="login":        #soll Adresse der Personen abrufen
    login()

if login.check()==True:

    if message=="get_message":  #soll alle messages abrufen
        get_message()

        if message=="delete":       #soll für die Konto löschung sein
        delete()

        if message=="send":
            send()
