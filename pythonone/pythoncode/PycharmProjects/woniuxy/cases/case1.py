import random
import time

from selenium.webdriver.support.select import Select

from common.oaLogin import oaLogin
from common.setup import setup


class notice:
    def __init__(self):
        wd = setup().set_driver()
        oaLogin().login(wd)
        wd.find_element_by_link_text('公告').click()
        self.notice_add(wd)
        self.wd = wd
        # self.notice_change(wd)
        # self.notice_delete(wd)
    def notice_add(self,wd):
        wd.find_element_by_link_text('公告管理').click()
        wd.find_element_by_id('name').send_keys('123')
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

        text = wd.find_element_by_xpath('/html/body/div/p[1]').text
        if text == '新增成功!':
            print('case1 pass')
    def __del__(self):
        self.wd.quit()
if __name__ == '__main__':
    notice()

