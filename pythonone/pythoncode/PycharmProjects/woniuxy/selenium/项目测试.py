from selenium import webdriver
import time
class kaishi:
    wd=webdriver.Firefox()
    wd.implicitly_wait(5)
    wd.get('http://localhost/smeoa/index.php')
    wd.find_element_by_id('emp_no').send_keys('admin')
    wd.find_element_by_id('password').send_keys('admin')
    wd.find_element_by_xpath('//input[@value="登录"]').click()
    wd.find_element_by_link_text('邮件').click()
    def xiexin(self):
        
        self.wd.find_element_by_link_text('写信').click()
        self.wd.find_element_by_xpath('//input[@class="letter"]').send_keys('daqiupan@gmail.com')
        self.wd.find_element_by_id('mail_title').send_keys('《全球化之经济全球化和文化全球化报告》')
        self.wd.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/form/div[5]/div/div/div/input').send_keys('C:\\Users\Administrator\Desktop')
        self.wd.find_element_by_xpath('//iframe[@tabindex=""]').send_keys('666666')
        self.wd.find_element_by_xpath('//*[@id="recever"]/a').click()
        self.wd.switch_to.frame(self.wd.find_element_by_xpath("/html/body/div[4]/iframe"))
        self.wd.find_element_by_xpath('//*[@id="rank"]/ul/li[2]/a').click()
        self.wd.find_element_by_xpath('//*[@id="addr_list"]/nobr[5]/label/span').click()
        self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[2]/label/a').click()
        self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[4]/label/a').click()
        self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[6]/label/a').click()
        self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div/div[1]/div[2]/a[1]').click()
        # self.wd.find_element_by_link_text('发送').click()

    def shoujianx(self):
        self.wd.find_element_by_link_text('收件箱').click()
        self.wd.find_element_by_id('toggle_adv_search_icon').click()
        self.wd.find_element_by_id('li_name').send_keys('梦想与现实')
        self.wd.find_element_by_id('li_content').send_keys('音乐，书，空间')
        self.wd.find_element_by_id('li_from').send_keys('大邱叔叔')
        self.wd.find_element_by_xpath('input[@name="be-create_time"]').send_keys('2')
        self.wd.find_element_by_xpath('input[@name="en-create_time"]').send_keys('6')


    def shanchu(self):
        wd=self.wd
        wd.find_element_by_link_text('已删除').click()
        wd.find_element_by_link_text('彻底删除').click()
        # wd.find_element_by_xpath('/html/body/div[4]/div/div')
        wd.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]').click()
        # wd.find_element_by_link_text('确定').click()

    def laji(self):
        self.wd.find_element_by_link_text('垃圾箱').click()
        self.wd.find_element_by_link_text('发件箱').click()
        self.wd.find_element_by_link_text('草稿箱').click()

    def wenjian(self):
        self.wd.find_element_by_link_text('我的文件').click()
        # self.wd.find_element_by_link_text('自定义文件夹1').send_keys('AAAAA')
        # self.wd.find_element_by_link_text('自定义文件夹2').send_keys('BBBBB')
        # self.wd.find_element_by_link_text('自定义文件夹3').send_keys('CCCCC')


    def yjsz(self):
         self.wd.find_element_by_link_text('邮件设置').click()

         #邮件分类
         self.wd.find_element_by_link_text('邮件分类').click()
         self.wd.find_element_by_link_text('新建').click()
         self.wd.find_element_by_xpath('//*[@id="sender_key"]').send_keys('daqiupan@gmail.com')
         self.wd.find_element_by_xpath('//*[@id="domain_key"]').send_keys('862286871@qq.com')
         self.wd.find_element_by_xpath('//*[@id="recever_key"]').send_keys('daqiupan@qq.com')
         self.wd.find_element_by_xpath('//*[@id="form_data"]/div[2]/div/label[1]/span').click()
         self.wd.find_element_by_xpath('.//*[@id="form_data"]/div[3]/div/label[1]/span').click()
         self.wd.find_element_by_xpath('.//*[@id="form_data"]/div[4]/div/label[1]/span').click()
         self.wd.find_element_by_xpath('.//*[@id="form_data"]/div[7]/input[1]').click()

         #邮件账户设置
         self.wd.find_element_by_xpath('//*[@id="left_menu"]/li[8]/ul/li[2]/a/span').click()
         self.wd.find_element_by_xpath('.//*[@id="mail_name"]').send_keys("龙系列火箭")
         self.wd.find_element_by_xpath('.//*[@id="email"]').send_keys("862286871@qq.com")
         self.wd.find_element_by_xpath('.//*[@id="pop3svr"]').send_keys("666666")
         self.wd.find_element_by_xpath('.//*[@id="smtpsvr"]').send_keys("777777")
         self.wd.find_element_by_xpath('.//*[@id="mail_id"]').send_keys("大邱叔叔")
         self.wd.find_element_by_xpath('.//*[@id="mail_pwd"]').send_keys("123456")
         self.wd.find_element_by_xpath('.//*[@id="form_data"]/div[7]/input').click()
         self.wd.find_element_by_xpath('html/body/div[4]/div/div/div[2]/button').click()

         #文件夹设置
         self.wd.find_element_by_link_text("文件夹设置").click()
         self.wd.find_element_by_xpath('.//*[@id="name"]').send_keys('spex')
         self.wd.find_element_by_xpath('.//*[@id="form_data"]/div[2]/div/div/span/button').click()
         self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div[2]/div[2]/ul/li/a/span').click()
         self.wd.find_element_by_xpath('html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/a').click()



if __name__ == '__main__':
    # kaishi().shanchu()
    kaishi().yjsz()
    # kaishi().wenjian()
    # kaishi().shoujianx()
    #kaishi().xiexin()
