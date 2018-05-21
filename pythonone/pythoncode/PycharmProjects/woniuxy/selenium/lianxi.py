from selenium import webdriver
import time
wd=webdriver.Firefox()
# wd.maximize_window()#最大屏
wd.get('http://192.168.9.126/Agileone')
wd.find_element_by_id('username').send_keys('admin')
wd.find_element_by_id('password').send_keys('admin')
wd.find_element_by_id('login').click()
time.sleep(3)
wd.find_element_by_link_text('※ 公告管理 ※').click()
wd.find_element_by_id('headline').send_keys('大邱叔叔')
wd.find_element_by_id('add').click()
time.sleep(3)
# wd.find_element_by_xpath("//label[@onclick='doDelete(this)']").click()#相对路径
wd.find_element_by_xpath("//label[2]").click()
time.sleep(2)
wd.switch_to.alert.accept()#弹出框点击确定
# wd.switch_to.alert.dismiss()#弹出框点击取消

