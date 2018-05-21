# import time,threading
# def loop():
#     print('thread %s is is running...'%threading.current_thread().name)
#     for i in range(5):
#         print('thread %s >>>%s'%(threading.current_thread().name,i))
# loop()
# t=threading.Thread(target=loop())
# print('我是主线程!')
# t.start()
# t.join()
l=[1,1,2,3,4,2,3,6]
def dup(lists):
    L=[]
    for i in lists:
        if i not in L:
            L.append(i)
    return L
print(dup(l))