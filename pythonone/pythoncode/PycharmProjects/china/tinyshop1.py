from selenium import webdriver

class ceoone:
    def ceotwo(self,):
        cd=webdriver.Firefox()
        cd.maximize_window()
        cd.implicitly_wait(2)
        cd.get('http://192.168.10.159/TinyShop_v1.7/index.php?con=admin&act=login')
        cd.find_element_by_xpath(".//*[@id='login']/div/form/ul/li[1]/input").send_keys('admin')
        cd.find_element_by_xpath(".//*[@id='login']/div/form/ul/li[2]/input").send_keys("123456")
        cd.find_element_by_xpath(".//*[@id='login']/div/form/ul/li[3]/input").send_keys("aaaa")
        cd.find_element_by_xpath(".//*[@id='login']/div/form/ul/li[4]/input[1]").click()
        return cd

if __name__=='__main__':
    ceoone().ceotwo()