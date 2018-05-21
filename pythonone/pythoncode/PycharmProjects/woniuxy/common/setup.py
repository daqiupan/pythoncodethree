from selenium import webdriver
class setup:
    def set_driver(self):
        wd = webdriver.Firefox()
        wd.get('http://localhost/smeoa/index.php')
        wd.implicitly_wait(10)
        return wd