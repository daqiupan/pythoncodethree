import hashlib,time,requests

def signstr():
    print(time.time())
    now_time=str(time.time()).split('.')[0]#当前时间以点号为分割（1213131412.212121），分割为0
    sign_str=now_time+'&Guest-Bugmaster'

    #创建md5对象
    md5=hashlib.md5()
    sign_bytes_utf8=sign_str.encode()
    #生成加密串
    md5.update(sign_bytes_utf8)
    #获取加密串
    sign_md5=md5.hexdigest()
    return now_time,sign_md5
now_time,sign_md5=signstr()
# print(signstr())
url='http://127.0.0.1:8000/api/sec_add_event/'
data={'eid':'66','name':'小米MIX2s新品发布会','limit':'8000','address':'国家会议中心','start_time':'2018-03-27 14:00:00','time':now_time,'sign':sign_md5}
r=requests.post(url,data=data)
# print(r.json())