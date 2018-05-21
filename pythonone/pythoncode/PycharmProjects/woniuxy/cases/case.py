from common.noticemanage import notice
from common.setup import setup
from common.oaLogin import oaLogin
class case:
    def __init__(self):
        wd = setup().set_driver()#打开Firefox浏览器，输入url，返回webdriver对象
        oaLogin().login(wd)#通过传参的方式，使用webdriver对象登录
        self.no = notice()
        self.wd = wd
    def case1_mtd(self):
        self.no.notice_add(self.wd,123)
        text = self.wd.find_element_by_xpath('/html/body/div/p[1]').text
        if text == '新增成功!':
            print('case1 pass')
            self.write_log('case1 pass')
    def case2_mtd(self):
        self.no.notice_add(self.wd,'abc')
        text = self.wd.find_element_by_xpath('/html/body/div/p[1]').text
        if text == '新增成功!':
            print('case2 pass')
            self.write_log('case2 pass')
    def case3_mtd(self):
        self.no.notice_add(self.wd,'abc123')
        text = self.wd.find_element_by_xpath('/html/body/div/p[1]').text
        if text == '新增成功!':
            print('case1 pass')
            self.write_log('case3 pass')
    def case4_mtd(self):
        self.no.notice_add(self.wd,'')
        ele = self.wd.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/h5')
        if ele.is_displayed():
            print('case4 pass')
            self.write_log('case4 pass')
    def case5_mtd(self):
        self.no.notice_add(self.wd,'哈哈')
        text = self.wd.find_element_by_xpath('/html/body/div/p[1]').text
        if text == '新增成功!':
            print('case5 pass')
            self.write_log('case5 pass')
    def write_log(self,msg):
        with open(r'C:\Users\Administrator\PycharmProjects\smeoa\log.txt','a') as f:
            f.write(msg+'\n')
    def __del__(self):
        self.wd.quit()
c = case()
c.case1_mtd()
c.case2_mtd()
c.case3_mtd()
c.case4_mtd()
c.case5_mtd()