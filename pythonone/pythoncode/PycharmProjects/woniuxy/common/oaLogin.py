from common.setup import setup
class oaLogin:
    def login(self,wd):
        wd.find_element_by_id('emp_no').send_keys('admin')
        wd.find_element_by_id('password').send_keys('admin')
        wd.find_element_by_xpath('//form[@id="form_login"]/div[4]/div/input').click()
if __name__ == '__main__':
    wd = setup().set_driver()
    oaLogin().login(wd)