import glob
import os

li = glob.glob(r'C:\Users\Administrator\PycharmProjects\smeoa\cases\*.py')
for i in li:
    print(i)
    if i != '__init__.py':
        os.system('python3 %s >>log.txt 2>&1'%i)
        