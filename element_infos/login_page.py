import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)  # 获取当前路径
webdriber_path = os.path.join(current_path, '..\webdriver\chromedriver.exe')

class LoginPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=webdriber_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://hfw.sj56.com.cn/tes/main/index.html#')
        self.username_inputbox = self.driver.find_element(By.XPATH,'//input[@id="phoneNumber"]') #属性==》页面上的控件
        self.password_inputbox = self.driver.find_element(By.XPATH,'//input[@id="loginPassword"]')
        self.login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        self.keeplogin_chekbox = None

    def input_username(self,username): #方法==》控件的操作
        self.username_inputbox.send_keys(username)

    def input_pasword(self,password):
        self.password_inputbox.send_keys(password)

    def click_login(self):
        self.login_button.click()

if __name__ == '__main__':
    login_page = LoginPage()
    login_page.input_username('18874209921')
    login_page.input_pasword('Lc19970212..')
    login_page.click_login()