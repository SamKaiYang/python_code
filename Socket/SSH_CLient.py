import socket
 
HOST = '192.168.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
 
def data_all(obj, lenth_size):
    data = ''                #用來儲存每一次迴圈時socket接收的資料，解決socket大概兩萬多位元組的緩衝瓶頸限制
    while lenth_size != 0:   #如果接收的資料長度不為0，開始執行接收資料處理策略
        if lenth_size <= 4096:    #這裡以4096為單位塊，作為每次的資料處理量大小
            data_recv = obj.recv(lenth_size)    #通過recv()接收資料
            lenth_size = 0    #通過這一步的處理，資料全部接收完畢，置lenth_size為0，結束迴圈，完成資料的接收處理工作
        else:
            data_recv = obj.recv(4096)    #以4096為單位塊，一次接收4096的資料量大小
            lenth_size -= 4096            #處理完一次4096位元組的資料後，將lenth_size減去4096
        data += data_recv                     #判斷外層，用本地的data來儲存接收到的資料，因為本地的data大小沒有限制，所以不存在data飽和無法繼續儲存資料的問題，但前面socket的recv()函式一次最多隻能接收的資料量大小是有限制的，這取決於socket的緩衝區大小，因此data_all函式的作用就是通過使用多次recv()函式，並且每次接收一定量的資料後就進行本地儲存，直到把所有的資料都接收完畢
    return (data)
 
while True:
    user_input = input('cmd to send:')#.strip()
    user_input = str(user_input)
    user_input = user_input.strip()
    if len(user_input) == 0:continue
    s.sendall(user_input)
 
    data_size = int(s.recv(1024))      #得到命令執行結果的大小長度，因為傳送過來的資料是字串，所以這裡要作型別轉換
    #data_size = s.recv(1024)
    print ('\033[32;1mdata size:\033[0m'),data_size    #列印命令執行結果的大小
    result = data_all(s, data_size)    #通過data_all函式來執行相應的資料接收處理策略
    print (result)                       #列印命令執行結果
 
s.close()                                  #關閉套接字
