# matplotlib是用來顯示GUI的函式庫
# serial則是用來跟Arduino溝通的函式庫
# struct跟pack則是在Serial傳輸資料時，打包資訊會用到的工具
from matplotlib.widgets import Slider 
import matplotlib.pyplot as plt
import serial
from struct import pack

# 在連接埠COM8建立一個鮑率為115200的Serial
# 這裡要提醒讀者，記得要把COM8改成您LattePanda上的COM port
ser = serial.Serial('COM6', 115200, timeout=0)

# 定義一個函式，將會根據i(馬達/拉桿編號)，回傳指定的函式
def send_ith(i):
    def send(val): # 定義一個函式，用來送出控制馬達角度的訊號
        data_header = bytes('s' + str(i), 'UTF8')
        data = int(val)
        ser.write(pack('<2si', data_header, data))
    return send


# 初始化伺服馬達控制拉桿的圖形化界面以及其對應的函式
a = []
s = []
for i in range(4):
    a.append(plt.axes([0.2, 0.2*(4 - i), 0.6, 0.07]))
    s.append(Slider(a[i], 'Servo' + str(i+1) + ' ', 0, 180, valfmt = '%d', valinit = 90))
    s[i].on_changed(send_ith(i))

plt.show()