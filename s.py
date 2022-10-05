import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
client, addr = s.accept()
while True:
    data = client.recv(1024)
    if len(data) > 1024 or data == 'close':
        client.close()
        break
    else:
        client.send(data)
        print(data)
    s.close()
