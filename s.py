import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen()
while True:
  conn, addr = s.accept()
  while True:
    if data == 'close':
      conn.close()
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
