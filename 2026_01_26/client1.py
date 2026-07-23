import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8005))

client.sendall(b'Hello, server!')

client.close()
