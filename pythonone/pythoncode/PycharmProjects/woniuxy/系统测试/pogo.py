from selenium import webdriver
import time,random

onename="赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费廉岑雷贺倪汤滕罗毕郝邬安常乐于时傅卞康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄"
twoname="就某种意义而言今天我们是为了要求兑现诺言而汇集到国家首都来的共和国缔造者草拟宪法和独立宣言气壮山河词句时曾向每一个美国人许下了诺言他们承诺给予所有人以生存自由和追求幸福不可剥夺的权正义保障自由宝贵公民"
forname="就某种意义而言今天我们是为了要求兑现诺言而汇集到国家首都来的共和国缔造者草拟宪法和独立宣言气壮山河词句时曾向每一个美国人许下了诺言他们承诺给予所有人以生存自由和追求幸福不可剥夺的权正义保障自由宝贵公民"
for i in range(500):
    for a in range(500):
        index=int(random.random()*100)
        threename=onename[index]+twoname[index]+forname[index]
        yahu=int(random.random()*100000000)
        qq=str(yahu)+'@gmail.com'
        wd=webdriver.Firefox()
        wd.get('http://localhost/phpwind/upload/index.php')
        time.sleep(1)
        wd.find_element_by_link_text("注册").click()
        time.sleep(1)
        wd.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/ul/li/input').click()
        wd.find_element_by_id('regname').send_keys(threename,'%s'%a)
        wd.find_element_by_id('regpwd').send_keys('123456')
        wd.find_element_by_id('regpwdrepeat').send_keys('123456')
        wd.find_element_by_id('regemail').send_keys(qq)
        wd.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[4]/div/form/div/dl[7]/dd[1]/input[1]').click()
        wd.quit()
        print(i)

