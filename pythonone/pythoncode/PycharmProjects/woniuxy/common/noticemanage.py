import random
import time
from semo import cat

from selenium.webdriver.support.select import Select

from common.oaLogin import oaLogin
from common.setup import setup
import xlrd

class notice:
    # def __init__(self):
    #     wd = setup().set_driver()
    #     oaLogin().login(wd)
    #     wd.find_element_by_link_text('公告').click()
    def notice_add(self,wd,a):
        wd.find_element_by_link_text('公告').click()
        wd.find_element_by_link_text('公告管理').click()
        wd.find_element_by_id('name').send_keys(a)
        wd.find_element_by_xpath('//button[@onclick="select_pid()"]').click()
        wd.switch_to.frame(wd.find_element_by_class_name('myFrame'))
        time.sleep(1)
        wd.find_element_by_xpath('//a[@node="0"]/span').click()
        wd.find_element_by_link_text('确定').click()
        wd.switch_to.default_content()
        wd.find_element_by_xpath('//a[@onclick="select_auth();"]').click()
        wd.switch_to.frame(wd.find_element_by_class_name('myFrame'))
        wd.find_element_by_id('rb_company').click()
        wd.find_element_by_link_text('总经办').click()
        wd.find_element_by_xpath('//div[@id=\'addr_list\']/nobr[2]/label/span').click()
        wd.find_element_by_xpath('//a[@onclick="add_address(\'rc\');"]').click()
        wd.find_element_by_xpath('//a[@onclick="add_address(\'cc\');"]').click()
        wd.find_element_by_xpath('//a[@onclick="add_address(\'bcc\');"]').click()
        wd.find_element_by_link_text('确定').click()
        wd.switch_to.default_content()
        wd.find_element_by_id('sort').send_keys(1)
        Select(wd.find_element_by_id('is_del')).select_by_index(1)
        wd.find_element_by_name('remark').send_keys('This is a test content!you can skip it!')
        wd.find_element_by_link_text('新增').click()

    def notice_change(self,wd):
        wd.find_element_by_link_text('公告管理').click()
        li = wd.find_elements_by_xpath('//div[@class="well"]/ul[@class="tree_menu"]/li/a/span')
        ele = random.choice(li)
        ele.click()
        wd.find_element_by_name('remark').send_keys('This is a changed content!you must be have look!')
        wd.find_element_by_link_text('保存').click()
    def notice_delete(self,wd):
        wd.find_element_by_link_text('公告管理').click()
        li = wd.find_elements_by_xpath('//div[@class="well"]/ul[@class="tree_menu"]/li/a/span')
        ele = random.choice(li)
        ele.click()
        wd.find_element_by_link_text('删除').click()
        wd.find_element_by_xpath('//button[@data-bb-handler="danger" and @class="btn btn-primary"]').click()
        time.sleep(1)
        #wd.find_element_by_xpath('//div[@class="modal-footer"]/button[@data-bb-handler="danger"]').click()
if __name__ == '__main__':
    notice()

