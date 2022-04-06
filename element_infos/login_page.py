import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.logo_utiles import logo_utiles # 日志文件
from common.base_page import BasePage
from common.element_data_utiles import ElementdataUtiles # 封装的excel方法

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # 当父类和子类都有初始化实例属性，需要用到super()
        #第二版
        # self.username_inputbox = {
        #     'element_name':'用户名输入框',
        #     'locatar_type':'xpath',
        #     'locator_value':'//input[@id="phoneNumber"]',
        #     'timeout': 5
        # }
        # self.password_inputbox = {
        #     'element_name': '密码输入框',
        #     'locatar_type': 'xpath',
        #     'locator_value': '//input[@id="loginPassword"]',
        #     'timeout': 5
        # }
        # self.login_button = {
        #     'element_name': '登录按钮',
        #     'locatar_type': 'xpath',
        #     'locator_value': '//button[@type="submit"]',
        #     'timeout': 5
        # }
        #第一版
        # self.driver.get('https://hfw.sj56.com.cn/tes/main/index.html#')
        # self.username_inputbox = self.driver.find_element(By.XPATH,'//input[@id="phoneNumber"]') #属性==》页面上的控件
        # self.password_inputbox = self.driver.find_element(By.XPATH,'//input[@id="loginPassword"]')
        # self.login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        # self.keeplogin_chekbox = None

        #第三版
        # # 调用execl表格方法进行操作
        elements = ElementdataUtiles('logo_page').get_element_info()
        print(elements)
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']


    def input_username(self,username): #方法==》控件的操作
        self.input_sendkeys(self.username_inputbox,username) #最新的方法
        # self.username_inputbox.send_keys(username)
        # logo_utiles.info('用户名输入框输入：'+ str(username))

    def input_pasword(self,password):
        self.input_sendkeys(self.password_inputbox,password) #最新的方法

    def click_login(self):
        self.click_the_button(self.login_button)

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)  # 获取当前路径
    webdriber_path = os.path.join(current_path, '..\webdriver\chromedriver.exe')
    driver =webdriver.Chrome(executable_path=webdriber_path)
    login_page = LoginPage(driver) # 创建一个对象，但是你引入的是父类，父类需要一个driver。所以你要传driver进去
    login_page.open_url('https://hfw.sj56.com.cn/tes/main/index.html#')
    login_page.input_username('18874209921')
    login_page.input_pasword('Lc19970212..')
    login_page.click_login()
    login_page.set_browser_max()
    login_page.quit()