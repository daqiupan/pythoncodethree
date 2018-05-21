# import requests,random
# surname ="0123456789"
# namesuf = "0123456789"
# onename="0123456789"
# url = 'http://localhost/phpwind/upload/register.php?'
# for i  in range(500):
#     r = requests.session()
#     index = int(random.random()*100)
#     name = surname[index] + namesuf[index]+onename[index]
#     # print(name)
#     qq = int(random.random()*1000000000000)
#     mailbox = str(qq) + '@163.com'
#     # print(mailbox)
#     data = {'forward':'','step':'2','regname':name,'regpwd':'nwmykn','regpwdrepeat':'nwmykn','regemail':mailbox,'rgpermit':'1'}
#     hrad = {'Content-Type': 'application/x-www-form-urlencoded'}
#     res = r.post(url,data=data,headers=hrad)
#     # res.encoding = 'utf-8'
#     print(i)

import requests,random
surname ="0123456789"
namesuf = "0123456789"
onename="0123456789"
url = 'http://192.168.10.177/TinyShop_v1.7/index.php?con=simple&act=reg'
for i  in range(100):
    r = requests.session()
    index = int(random.random()*100)
    name = surname[index] + namesuf[index]+onename[index]
    # print(name)
    qq = int(random.random()*1000000000000)
    mailbox = str(qq) + '@163.com'
    # print(mailbox)
    data = 'email=mailbox&password=123456&repassword=123456&verifyCode=aaaa&tiny_token_reg=8mbllzsnytzflqkxs0zpp20isa347ycn'
    hrad = {'Content-Type: application/x-www-form-urlencoded'}
    res = r.post(url,data=data,headers=hrad)
    # res.encoding = 'utf-8'
    print(i)
