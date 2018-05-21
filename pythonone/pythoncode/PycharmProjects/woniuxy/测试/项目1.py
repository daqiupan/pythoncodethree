from selenium import webdriver


11111111
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
        self.wd.quit()
kaishi().xiexin()