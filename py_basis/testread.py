text = '\nhello\nSam\nthird'
 # 'w'=write 讀取内容的形式打开
#my_file = open('my file.txt','a')#  'a'=append 以增加内容的形式打开
#my_file.write(text)
my_file.close()

file = open('my file.txt','r')
content = file.readlines()
#content = file.readline(2) # 逐行輸出
python_list = [1,2,3,4,5,'fef','efwege']
print(content) 
