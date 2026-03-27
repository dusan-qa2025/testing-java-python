import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 8005))
server.listen()

klijent, adresa = server.accept()
klijent.send(b"Unesite prvi broj: ")

prviBroj = int(klijent.recv(32).decode("utf-8"))

klijent.send(b"Unesite drugi broj: ")

drugiBroj = int(klijent.recv(32).decode("utf-8"))

rezultat = format(prviBroj + drugiBroj)

klijent.send(bytes(rezultat, "utf-8"))