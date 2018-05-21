import glob
import os
li=glob.glob(r'C:\Users\Administrator\PycharmProjects\woniuxy\测试\*.py')
for i in li :
    print(i)
    os.system('python %s >>log.txt 2>&1'%i)
