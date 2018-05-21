import http.client

conn=http.client.HTTPConnection("localhost")
conn.request("GET","/smeoa/index.php?m=login&a=index")
response=conn.getresponse().read().decode()
# print(response)

conn=http.client.HTTPConnection("localhost")
data="emp_no=admin&password=admin"
headers={"Content-Type": "application/x-www-form-urlencoded"}
conn.request("POST","/smeoa/index.php?m=login&a=check_login",body=data,headers=headers)
respons=conn.getresponse().read().decode()
# print(respons)
# if "" in respons:
#     print("成功")
# else:
#     print("失败")



conn=http.client.HTTPConnection("localhost")
data="&ajax=1"
headers={"Content-Type": "application/x-www-form-urlencoded"}
conn.request("POST","/smeoa/index.php?m=push&a=server2",body=data,headers=headers)
respon=conn.getresponse().read().decode()
print(respon)

