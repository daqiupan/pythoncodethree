import time ,threading
def cat():
    f=open(r'D:\daqiu.txt','a')
    t1=time.time()
    for i in range(1000):
        f.write('daqiu')
    f.close()
def __del__(self):
    t2=time.time()
    print(t2 - self.t1)
