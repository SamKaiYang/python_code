import socket
import sys

# 創建Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 獲取本地IP
host = '192.168.0.1' 

# 設置端口
port = 9999

# 連接端口，指定主機和端口
s.connect((host, port))

# 接收小於 1024 字節的數據
msg = s.recv(1024)


#serversocket,addr = host
message = 'HIHIHIHIHI'
s.send(message.encode('utf-8'))
s.close()

print (msg.decode('utf-8'))
