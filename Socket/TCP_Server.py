#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys


# 創建socket
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 獲取本地IP
host = '192.168.0.1'

port = 9999

# 允許地址重用
recSocket = serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 绑定端口	     
serversocket.bind((host, port))

# 設置最大連結數，其後排隊
serversocket.listen(5)

while True:
    # 建立客户端連結
    clientsocket,addr = serversocket.accept()      
    print("連接地址: %s" % str(addr))
    
    msg='歡迎小凱凱的python服務！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    ss = clientsocket.recv(1024)
    print (ss.decode('utf-8'))
    clientsocket.close()

    		
