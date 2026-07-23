import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8005))

while True:
    number = input("Unesite broj (1-10):")
    client_socket.send(number.encode())

    response = client_socket.recv(1024).decode()
    print("Odgovor servera:", response)

    if response == "True":
        print("Pogodili ste broj!")
        break


client_socket.close()