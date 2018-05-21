import threading,time
def loop():
    print(threading.current_thread().name)
    for i in range(5):
        print(threading.current_thread().name,i)
loop()
