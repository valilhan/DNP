import socket
import os

socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port = 12300
buff_size = 1024
socket.bind(('', port))
address_file = dict()
print("The server is ready to receive")
# s | seqno | filename | total_size
# d | seqno | data_bytes
while True:
    message_from_client, address = socket.recvfrom(buff_size)
    message_from_client = message_from_client.decode()
    message = message_from_client.split(' | ')
    active = message[0]
    if active == 's':
        seqno = int(message[1])
        filename = message[2]
        filepath = './Server/' + filename
        total_size = message[3]
        address_file[address] = filepath
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('')
        message_to_client = f'a | {seqno + 1} | {buff_size}'.encode()
        socket.sendto(message_to_client, address)
    elif active == 'd':
        seqno = int(message[1])
        data_chunks = message[2]
        filepath = address_file[address]
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(data_chunks)
        message_to_client = f'a | {seqno + 1} | {buff_size}'.encode()
        socket.sendto(message_to_client, address)

