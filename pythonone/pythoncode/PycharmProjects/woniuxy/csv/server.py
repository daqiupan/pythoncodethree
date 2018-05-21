# import socket,threading
# class server:
#     def __init__(self):
#         server = socket.socket()
#         server.bind(('localhost',111))
#         server.listen(10)
#         self.server=server
#         self.get_con()
#     def get_con(self):
#         li=[]
#         while 1:
#             con,adder=self.server.accept()
#             # print(con,adder)
#             data='你已经连接成功！'
#             con.send(data.encode('GBK'))
#             # cat=con.recv(1024).decode('GBK')
#             # self.get_msg(con)
#             li.append(con)
#             threading.Thread(target=self.get_msg,args=(con,)).start()
#     def get_msg(self,con,li):
#         while 1:
#             re=con.recv(1024)
#             print(re.decode('GBK'))
#             for i in li :
#                 i.send(re)
# server().get_con()

import socket
from threading import Thread
import time
from DB_con import DB_MYSQL

class server:
    def  __init__(self):
        server = socket.socket()
        server.bind(('localhost',666))
        server.listen(5)
        self.server = server
        self.get_con()
    def get_con(self):
        li = []
        di = {}
        while 1:
            con,addr = self.server.accept()
            # print(con,addr)
            data = '欢迎来到大邱YY聊天室！请输入昵称：'
            con.send(data.encode('GBK'))     #告诉已经连接的客户端，输入昵称
            Thread(target=self.get_msg,args=(con,li,di,addr)).start()   #启动子线程，把剩下的事情交给子线程去完成
            #self.get_msg(con)
            li.append(con)     #添加已经连接的客户端对象到列表，方便后面群发消息
    def get_msg(self,con,li,di,addr):
        name = con.recv(1024).decode('GBK')    #接收客户端发过来的昵称
        di[addr] = name      #向字典里面添加当前的昵称并和addr(ip,port)对应
        while 1:
            redata = con.recv(1024).decode('GBK')
            if redata == 'quit':
                li.remove(con)
                print(di[addr]+'用户已退出聊天')
                di.pop(addr)
                break
            print(di[addr]+'于'+time.strftime('%X')+':\n'+redata)
            for i in li:
                #通过字典查询得到当前发送消息的客户端的昵称，并和消息连接，准备一起群发
                i.send((di[addr]+'于'+time.strftime('%X')+':\n'+redata).encode('GBK'))
                DB_MYSQL.change_db('insert into lianjie VALUES("%s","%s","%s")'%(name,redata,time))
server()