import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(("localhost", 8005))

prviBroj = input(klijent.recv(256).decode("utf-8"))
klijent.send(bytes(prviBroj, "utf-8"))

drugiBroj = input(klijent.recv(256).decode("utf-8"))
klijent.send(bytes(drugiBroj, "utf-8"))


print("Rezultat je: ", klijent.recv(256).decode("utf-8"))