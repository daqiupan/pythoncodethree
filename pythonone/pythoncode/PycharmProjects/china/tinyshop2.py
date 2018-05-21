from selenium import webdriver
from oneyun.tinyshop1 import ceoone
from selenium.webdriver.support.select import Select
import time
fddjhs

class dagone:
    def dagtwo(self):
        # cd=webdriver.Firefox()
        cd.implicitly_wait(3)
        cd.find_element_by_xpath(".//*[@id='main_nav']/li[1]/a").click()
        cd.find_element_by_xpath(".//*[@id='content']/form/div/a[3]").click()
        Select(cd.find_element_by_xpath(".//*[@id='category_id']")).select_by_visible_text('├──手机')
        Select(cd.find_element_by_xpath(".//*[@id='type_id']")).select_by_visible_text('手机产品')
        Select(cd.find_element_by_xpath("/html/body/div[3]/div[2]/form/div/div[1]/div[1]/dl[3]/dd/select")).select_by_visible_text('三星')
        cd.find_element_by_xpath(".//*[@id='obj_form']/div[1]/div[1]/dl[4]/dd/input").send_keys("盖世S10endg")
        cd.find_element_by_xpath(".//*[@id='goods_no']").send_keys('123456')
        cd.find_element_by_xpath(".//*[@id='obj_form']/div[1]/div[1]/dl[8]/dd/button").click()
        # 跳转页面
        # handle = cd.current_window_handle
        # print(handle)
        # handles=cd.window_handles
        # print(handles)
        # for i in handles:
        #     if i !=handles:
        #         cd.switch_to.window(i)
        #         time.sleep(3)

        # swith_to.frame切换到内嵌页面
        cd.switch_to.frame(cd.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe"))
        cd.find_element_by_xpath("/html/body/div[2]/ul/li[2]").click()
        cd.find_element_by_xpath("html/body/div[2]/div/div[2]/ul/li[3]/img").click()
        cd.find_element_by_xpath("/html/body/div[3]/button").click()

        cd.switch_to_default_content()
        cd.find_element_by_xpath(".//*[@id='goods_list']/table/tbody/tr[2]/td[2]/input").send_keys(100)
        cd.find_element_by_xpath(".//*[@id='goods_list']/table/tbody/tr[5]/td[2]/input").send_keys(1234)
        cd.find_element_by_xpath(".//*[@id='goods_list']/table/tbody/tr[6]/td[2]/input").send_keys(1)
        cd.find_element_by_xpath(".//*[@id='obj_form']/div[2]/input[1]").click()
        aa=cd.find_element_by_xpath("").text
        if aa=="":
            print()
        # cd.quit()


if __name__=='__main__':
    cd=ceoone().ceotwo()
    dagone().dagtwo()