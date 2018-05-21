import socket
import sys
from threading import Thread

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class chatwindow(QWidget,QFont):
    def __init__(self):
        QWidget,QFont.__init__(self)
        self.setGeometry(300,100,500,400)#设置聊天框大小
        self.setWindowTitle('大邱YY聊天室')#聊天框的名字
        self.setFixedSize(self.width(),self.height())#禁止调整文本框大小化
        palette=QtGui.QPalette()
        icon=QtGui.QPixmap('D:\\qiu.png')#设置背景图片
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)
        self.UI()
        client=socket.socket()
        client.connect(('localhost',666))
        self.client=client
        Thread(target=self.send_msg).start()
        Thread(target=self.recv_msg).start()
        # self.show()

    def UI(self):
        label= QLabel('姓名：',self)
        label.setFont(QFont('宋体',16))#设置字体的大小和形体
        label.setGeometry(30,10,80,30)#定位
        labe2= QLabel('请输入：',self)
        labe2.setFont(QFont('宋体',15))#设置字体的大小和形体
        labe2.setGeometry(15,320,90,40)
        text=QLineEdit(self)
        text.setGeometry(90,320,300,40)#姓名框的大小
        self.text=text
        # text2=QTextEdit(self)#有浮标，能输入内容
        # text2.setGeometry(90,50,300,250)#文本框的大小
        coo=QTextEdit(self)
        coo.setGeometry(10,60,70,250)
        coo.append('会员专区')
        coo.setFont(QFont('宋体',38,))
        ceo=QTextEdit(self)
        ceo.setGeometry(400,8,100,50)
        ceo.append('*学习栏')
        ceo.setFont(QFont('宋体',18))
        cat=QTextEdit(self)
        cat.setGeometry(400,60,100,250)
        cat.append('他仗着勃勃之勇气与天命之雄心，罔顾不测之凶险。')
        cat.append('拼着血肉躯奋然与命运前行、死神与危机挑战')
        cat.append('这全是为了一块弹丸之地！')
        cat.append('真正的伟大，并不只是肯为轰轰烈烈之大事奋斗。')
        cat.append('而是肯为区区草莽力争一份荣耀。')
        cat.append('人年轻的时候应该浪迹天涯，用心去领略异国的风土人情，去感受聆听子夜的钟声。')
        self.msg=QTextBrowser(self)# 不能输入内容
        self.msg.setGeometry(90,60,300,250)#文本框的大小
        msg=QTextBrowser(self)
        msg.setGeometry(90,60,300,250)
        msg.setStyleSheet('QWdget{background-color:rgb(255,155,255,50%)}')
        self.msg=msg
        cat=QLineEdit(self)
        cat.setGeometry(90,10,300,30)
        bu=QPushButton('发送消息',self)#按钮
        bu.setGeometry(410,320,80,40)
        bu=QPushButton('关闭聊天',self)#按钮
        bu.setGeometry(410,360,80,40)
    # def send_msg(self):
        bu.clicked.connect(self.send_msg)
    def send_msg(self):
        self.msg.append(self.text.text())
        self.recv_msg()
    def recv_msg(self):
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    ch=chatwindow()
    ch.show()
    sys.exit(app.exec_())