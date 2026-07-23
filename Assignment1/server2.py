import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 8005))
server_socket.listen()
print("Server is listening...")

client, addr = server_socket.accept()
print("Povezan klijent:", addr)
    
while True:
     
     server_number = random.randint(1, 10)
     print("Server random broj:", server_number)
    
     data = client.recv(1024)

     if not data:
        print("Pokusajte ponovo...")
        break

     data = data.decode()

     if not data.isdigit():
        client.send("Invalid input".encode())
        continue

     client_number = int(data)

     if client_number < 1 or client_number > 10:
        client.send("Number must be between 1 and 10".encode())
        continue

     if client_number == server_number:
        client.send("True".encode())
        print("Broj pogodjen, kraj igre")
        break
     else:
        client.send("False".encode())


server_socket.close()
client.close()