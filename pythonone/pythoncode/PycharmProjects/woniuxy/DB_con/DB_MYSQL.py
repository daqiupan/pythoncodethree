import pymysql
#获取mysql的连接对象
def get_db(host='localhost',user='root',pwd='',dbname='woniu'):
    db=pymysql.connect(host,user,pwd,dbname,charset='utf8')
    return  db
#执行sql命令
def exe_sql(sql):
    db=get_db()
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    return  db,cur
#执行增、删、改
def change_db(sql):
    db,cur=exe_sql(sql)
    db.close()
#查询一条
def select__one(sql):
    db,cur=exe_sql(sql)
    r=cur.fetchone()
    db.close()
    return r
#查询所有
def select__all(sql):
    db,cur=exe_sql(sql)
    r=cur.fetchall()
    db.close()
    return r
if __name__=='__main__':
    r=select__one('select * from liaotian')
    print(r)


