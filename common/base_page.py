import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.logo_utiles import logo_utiles # 日志文件
from common.config_utiles import local_config #配置文件

class BasePage(object):
    def __init__(self,driver): #初始化一个driver
        self.driver = webdriver.Chrome() #driver

    #浏览器的操作封装 ==>二次封装
    def open_url(self,url):
        self.driver.get(url)
        logo_utiles.info("打开url地址%s "% url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logo_utiles.info("设置浏览器最大化 ")

    def refresh(self):
        self.driver.refresh()
        logo_utiles.info("浏览器最刷新")

    def quit(self):
        self.driver.quit()
        logo_utiles.info("退出浏览器")

    def implicitly_wait(self,seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)
        logo_utiles.info('隐式等待')

    def get_title(self):
        value = self.driver.title
        logo_utiles.info('获取网页标题%s'%value)
        return value
    # ...

    #元素封装操作  element_info= {
        #     'element_name':'用户名输入框',
        #     'locatar_type':'xpath',
        #     'locator_value':'//input[@id="phoneNumber"]',
        #     'timeout': 5
        # }
    def find_element(self,element_info): # element_info 值
        locator_type_name =element_info['locatar_type'] # 初始化 查找元素的方法：xpath。class.id 等等
        locator_value_info = element_info['locator_value']  # 初始化 //input[@id="phoneNumber"] 一个方法
        locator_timeout = element_info['timeout'] # 初始化 'timeout': 5
        if locator_type_name == 'id':
            locatar_type = By.ID
        elif locator_type_name == 'class':
            locatar_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locatar_type = By.XPATH
        elif locator_type_name == 'name':
            locatar_type = By.NAME

        #....还有多种查找元素的方法

        #方法一 教科书上的
        element = WebDriverWait(self.driver,locator_timeout)\
                .until(lambda x:x.find_element(By.XPATH, locator_value_info))
        logo_utiles.info('[%s]元素识别成功'%element_info['element_name'])
        # 方法二
        # element = WebDriverWait(self.driver, locator_timeout) \
        #     .until(EC.presence_of_element_located(locatar_type,locator_value_info))
        return element
        # self.driver.find_element(locatar_type,'//input[@id="phoneNumber"]')
        # ==》演变成下面的
         #  self.driver.find_element(By.XPATH, locator_value_info)

    def click_the_button(self,element_info):
        element = self.find_element(element_info) #
        element.click()
        logo_utiles.info('[%s]元素进行点击操作' % element_info['element_name'])

    def input_sendkeys(self,element_info,content):
        element = self.find_element(element_info)  #
        element.send_keys(content)
        logo_utiles.info('[%s]元素进行输入内容：%s' % (element_info['element_name'],content))

    #frame ==>id/name frname元素对象
    #思路一  推荐 简单明了
    def switch_to_frname(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        # 释放frame，重新回到主页面上
        #driver.switch_to.default_content()

    #思路二
    def switch_to_frname_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frname_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    #思路三
    def switch_to_frame_01(self,**element_dict):
        self.wait(3)
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)

    # selenuim 执行js
    def excute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.excute_script(js_str)
        else:
            self.driver.excute_script(js_str,None)

    def delete_element(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.excute_script('arguments[0].removerAttribute("%s");'%attribute_name,element)

    # 等待封装

    def wait(self,seconds=local_config.time_out): #固定等待
        time.sleep(seconds)










