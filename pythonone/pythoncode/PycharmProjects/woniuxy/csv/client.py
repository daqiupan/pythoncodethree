# import socket
# import threading
# class client:
#     def __init__(self):
#         client=socket.socket()
#         client.connect(('localhost',111))
#         self.client=client
#         self.see()
#     def see(self):
#         threading.Thread(target=self.send_msg).start()
#         threading.Thread(target=self.recv_msg).start()
#     def send_msg(self):
#         while 1:
#             i=input('输入：')
#             self.client.send(i.encode('GBK'))
#     def recv_msg(self):
#         while 1:
#             print(self.client.recv(1024).decode('GBK'))
# client()

import socket
from threading import Thread


class client:
    def __init__(self):
        client = socket.socket()
        client.connect(('localhost',666))
        self.client = client
        self.begin_thread()
    def begin_thread(self):
        t1 = Thread(target=self.recv_msg)
        t1.setDaemon(True)
        t1.start()
        t = Thread(target=self.send_msg)
        t.start()
        # self.send_msg()
    def send_msg(self):
        while 1:
            i = input('输入：')
            self.client.send(i.encode('GBK'))
            if i == 'quit':
                exit()
    def recv_msg(self):
        while 1:
            print(self.client.recv(1024).decode('GBK'))
client()

