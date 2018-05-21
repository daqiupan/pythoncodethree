from appium import webdriver
import time
caps = {}
caps['platformName']='Android'
caps['platformVersion']='4.4.2'
caps['deviceName']='127.0.0.1:62001'
caps['appPackage']='com.tencent.mobileqq'
caps['appActivity']='.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
time.sleep(50)

driver.find_element_by_xpath("//*[@text='登 录']").click()
# driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()


# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver.find_element_by_name("1").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("delete").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()
#
# driver.find_element_by_name("=").click()
#
# driver.quit()



# a={5,1,8,4,1}
# b=list(a)
# b.sort()
# print(b)