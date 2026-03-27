import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 8006))
server.listen()

klijent, adresa = server.accept()

klijent.send(b"Unesite broj godina:")

godine = int(klijent.recv(32).decode("utf-8"))
if godine > 0:
    if godine >= 18:
        klijent.send(b"Punoletna osoba")
    else:
        klijent.send(b"Maloletna osoba")
else:
    klijent.send(b"Unesite validnu vrednost")

klijent.close()
server.close()
