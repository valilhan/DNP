import socket
import os

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port = 12300
hostname = '127.0.0.1'
buffsize = 1024
address = (hostname, port)
seqno = 0
filename = 'some.txt'
filesize = os.path.getsize(filename)
start_message = f"s | {filename} | {filesize}"
client_socket.sendto(start_message.encode(), address)
answer_from_server, serverAddress = client_socket.recvfrom(buffsize)
print(answer_from_server.decode())
client_socket.close()



