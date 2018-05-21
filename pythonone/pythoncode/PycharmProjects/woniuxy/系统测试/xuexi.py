import requests,unittest

s=requests.Session()
#    新增成功
url='http://localhost/smeoa/index.php?m=notice_folder&a=save'
headers={'Content-Type': 'application/x-www-form-urlencoded'}
# headers={'Content-Type': 'application/x-www-form-urlencoded','Cookie': 'Hm_lvt_2a935166b0c9b73fef3c8bae58b95fe4=1519801600,1520393797,1520490659,1520492849; sessionid=vw81ty7sh3xmjklsaew2nj7pcgjzw4rp; PHPSESSID=3322dfd6d433c9c8b2999ad2a2f645ce; left_menu=; top_menu=83; return_url=/smeoa/index.php%3Fm%3Dnotice_folder%26a%3Dindex; Hm_lpvt_2a935166b0c9b73fef3c8bae58b95fe4=1520495643; current_node=sfid90'}
data='id=&opmode=add&admin=&write=&read=&folder_list=0&name=my name is yanglei&folder_name=%E6%A0%B9%E8%8A%82%E7%82%B9&pid=0&sort=&is_del=0&remark='
r=s.post(url,headers=headers,data=data)#发送请求
r.encoding='utf-8'
print(r.text)#text文本内容
# print(r.status_code)
# print(r.content)#二进制内容
# print(r.cookies)
#print(r.json)


class TestGuest(unittest.TestCase):
    def setUp(self):
        pass
    def test_search_success(self):
        url='http://127.0.0.1:8000/api/get_event_list/?eid=22'
        r=requests.get(url)
        response=r.json()
        print(response)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()






