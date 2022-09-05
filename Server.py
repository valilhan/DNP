import socket
import os

socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port = 12300
buff_size = 1024
socket.bind(('', port))
print("The server is ready to recieve")
while True:
    message_from_client, address = socket.recvfrom(buff_size)
    message_from_client = message_from_client.decode()
    message = message_from_client.split(' | ')
    print(message)

