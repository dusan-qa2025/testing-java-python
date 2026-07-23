import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8005))
server.listen()
print('Server is listening...')

connection, address = server.accept()
print("Connection accepted from:", address)
time.sleep(2)

data = connection.recv(1024)
decoded_data = data.decode("utf-8")
print("Received data from client:", decoded_data)

time.sleep(2)

connection.close()
server.close()


