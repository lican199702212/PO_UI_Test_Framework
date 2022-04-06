import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPage
from common.logo_utiles import logo_utiles

current_path = os.path.dirname(__file__)  # 获取当前路径
webdriber_path = os.path.join(current_path, '..\webdriver\chromedriver.exe')

class MainPage(object):
    def __init__(self):
        login_page = LoginPage()
        login_page.input_username('18874209921')
        login_page.input_pasword('Lc19970212..')
        login_page.click_login()
        self.driver = login_page.driver # 把login_page.driver 转移到 MainPage里

        self.text_name = self.driver.find_element(By.XPATH, '//div[@class="sjmain-row"]')
        self.click_neibu = self.driver.find_element(By.XPATH,'//span[text()="内部版"]')
        self.click_qiye = self.driver.find_element(By.XPATH, '//span[text()="企业版"]')
        self.click_zhifu = self.driver.find_element(By.XPATH, '//span[text()="支付版"]')
        self.click_fengchao = self.driver.find_element(By.XPATH, '//span[text()="蜂巢中台"]')
        self.click_name = self.driver.find_element(By.XPATH, '//span[@class="name"]')

    def get_text_name(self): #方法==》控件的操作
        value = self.text_name.get_attribute('title') #获取当前文字
        return value

    def get_click_neibu(self):
        self.click_neibu.click()
        logo_utiles.info("点击内部版控件")

    def get_click_qiye(self):
        self.click_qiye.click()

    def get_click_zhifu(self):
        self.click_zhifu.click()

    def get_click_engchao(self):
        self.click_fengchao.click()

    def get_click_name(self):
        self.click_name.click()
if __name__ == '__main__':
    main_page = MainPage()
    value = main_page.get_text_name()
    print(value)
    main_page.get_click_neibu()
    time.sleep(2)
    main_page.get_click_qiye()

