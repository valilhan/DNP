import socket
import os
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port = 12300
hostname = socket.gethostname()
buff_size = 1024
address = (hostname, port)
start_seqno = 0
fileName = 'some.txt'
filePath = './Client/'+fileName
filesize = os.path.getsize(filePath)
start_message = f"s | {start_seqno} | {fileName} | {filesize}"
print("Start send message")
#  a | next_seqno | buf_size
#  a | next_seqno
client_socket.sendto(start_message.encode(), address)
answer_from_server, serverAddress = client_socket.recvfrom(buff_size)
answer_from_server = answer_from_server.decode()
answer_massage = answer_from_server.split(' | ')
active = answer_massage[0]
seqno = int(answer_massage[1])
if len(answer_massage) == 3:
    buff_size = int(answer_massage[2])
with open(filePath, 'r', encoding='utf-8') as f:
    for i in range(0, filesize, buff_size):
        print(f.tell())
        if i != 0:
            answer_from_server, serverAddress = client_socket.recvfrom(buff_size)
            answer_from_server = answer_from_server.decode()
            answer_massage = answer_from_server.split(' | ')
            active = answer_massage[0]
        data_chunks = f.read(buff_size)
        message = f"d | {seqno + 1} | " + data_chunks
        client_socket.sendto(message.encode(), serverAddress)
client_socket.close()




