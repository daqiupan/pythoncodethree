from selenium import webdriver
import time
wd=webdriver.Firefox()
wd.maximize_window()
wd.get('http://baidu.com')
wd.find_element_by_id('kw').send_keys('蜗牛学院')
wd.find_element_by_id('su').click()
wd.find_element_by_link_text('蜗牛学院-Java培训|Java学习|Web培训|Java视频|Java自学|成都IT...').click()
wd.find_element_by_id('').click()

