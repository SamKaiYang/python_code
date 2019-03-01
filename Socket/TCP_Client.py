import socket
import sys
import pickle
# 創建Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 獲取本地IP
host = '192.168.0.1' 

# 設置端口
port = 9999

# 連接端口，指定主機和端口
s.connect((host, port))


arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
data_string = pickle.dumps(arr)
s.send(data_string)

data = s.recv(4096)
data_arr = pickle.loads(data)

s.close()
print ('Received')
repr(data_arr)
