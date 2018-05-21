import pymysql
'''
注册 OK
登录 OK

'''
# 创建连接游标
def concur():
	db=pymysql.connect('localhost','root','nwmykn','atm',charset='utf8')
	# 创建游标
	cur=db.cursor()
	return db,cur
#提交和关闭连接
def comclo(db,cur):
	db.commit()
	cur.close()
	db.close()
#注册验证
def get_db(name,password,phono):
	db,cur=concur()
	cur.execute("INSERT INTO user_info(name,name_passwd,phono) VALUES('%s','%s','%d');"%(name,password,phono))
	comclo(db,cur)	
# 注册
def signus():
	name=input('请输入你的用户名：')
	password=input('设置你的密码：')
	phono=int(input('你的电话号码：'))
	# 传递用户的信息存入数据库
	true=get_db_logon(name)
	if true>=1:
		print('用户已存在！')
		signus()
	get_db(name,password,phono)
#登录数据库验证
def get_db_logon(name,password=''):
	db,cur=concur()
	if password=='':
		result=cur.execute("SELECT * from user_info WHERE name='%s';"%name)
	else:
		result=cur.execute("SELECT * from user_info WHERE name='%s' and name_passwd='%s';"%(name,password))
	comclo(db,cur)
	return result
# 登录_用户密码验证
def logon(count):
	if count==3:
		print('错误次数过多，限制登录！')
		return
	name=input('请输入你的用户名(您有%d次机会)：'%(3-count))
	password=input('密码：')
	result=get_db_logon(name,password)
	# print(result)1表示查询有结果，0 无
	count+=1
	if result==1:
		print('登录成功！进入操作界面……')
		OperatingFace(name)
	else:
		print('用户名密码错误！')
		logon(count)
#操作界面
def OperatingFace(name):
	text=int(input('请确认你的操作(1：显示余额 2：转账 3：取款 4：存款 5：切换用户 6：注销):'))
	if text==1:
		balance=ShowBalance(name)
		print('余额：%d' %balance)
		OperatingFace(name)
	elif text==2: 
		Transfer(name)
		OperatingFace(name)
	elif text==3:
		RemoveMoney(name)
		OperatingFace(name)
	elif text==4:
		Addbalance(name)
		OperatingFace(name)
	elif text==5:
		print('退出当前用户中……')
		Switchinguser()
	elif text==6:
		print('注销成功，程序终止。GOOD BYE')
		return
	else:
		pass
#1：显示余额
def ShowBalance(name):
	db,cur=concur()
	cur.execute("SELECT balance from user_info WHERE name='%s';"%name)
	balance=cur.fetchone()#获取结果
	# print(type(balance))#返回时一个元组
	comclo(db,cur)
	li=list(balance)
	balance=li[0]
	# print(li[0])#返回5000.0
	# return float(balance)
	# print(balance)
	return balance
#2：转账
def Transfer(name):
	balance=ShowBalance(name)
	trans=float(input('请输入转账金额(当前余额：%f):' %balance))
	if trans>balance:
		print('余额不足！')
		Transfer(name)
	transname=input('转入的账户：')
	UserIsHere=get_db_logon(transname)
	if UserIsHere==0:
		print('你输入的账户不存在，请核对后再输！')
		Transfer(name)
	balance-=trans
	upbalance(balance,name)
	#转入用户的余额
	transbalance=ShowBalance(transname)
	transbalance+=trans
	upbalance(transbalance,transname)
#更新余额
def upbalance(balance,name):
	db,cur=concur()
	cur.execute("UPDATE user_info SET balance='%d' WHERE `name`='%s';" %(balance,name))
	comclo(db,cur)
#3：取款
def RemoveMoney(name):
	balance=ShowBalance(name)
	remove=float(input('请输入取款金额(当前余额：%f):' %balance))
	if remove>balance:
		print('余额不足，且你不能透支！')
		RemoveMoney(name)
	balance-=remove
	upbalance(balance,name)
	print('取款成功！')
#4:存款
def Addbalance(name):
	balance=ShowBalance(name)
	add=float(input('请输入存款金额:'))
	balance+=add
	upbalance(balance,name)
	print('存款成功！')
#5:切换用户
def Switchinguser():
	count=0
	logon(count)
# 获取用户业务
def main():
	text=int(input('请确认你的操作(1：登录 2：注册):'))
	if text==1:
		count=0#用户密码输入计数
		logon(count)
	elif text==2:
		signus()
#调用主函数
main()


