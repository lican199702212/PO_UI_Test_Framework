import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  #浏览器模块Options

from common.config_utiles import local_config

current_path = os.path.dirname(__file__)  # 获取当前路径
webdriver_path = os.path.join(current_path, '..',local_config.driver_path)

class BrowserDriver(object):
    def __init__(self,driver_path = webdriver_path,driver_name = local_config.driver_name):
        self.__driver_path = driver_path
        self.__driver_name = driver_name

    def get_driver_name(self): #判断默认浏览器
        if self.__driver_name.lower() == 'chrome': #.lower()不区分大小写的意思，强制转换
            return self.__get_chrome_driver()
        elif self.__driver_name.lower() == 'firefox':
            return self.__get_firefox_driver()

    # 谷歌浏览器驱动
    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8') #设置默认编码为UTF-8
        chrome_options.add_experimental_option('useAutomationExtension',False) #取消Chrome受自动化测试提示字段
        chrome_options.add_experimental_option('excludeSwitches',['enable-automation'] )#取消Chrome受自动化测试提示字段

        chrome_driver_path = os.path.join(self.__driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
        return driver

    #火狐浏览器驱动
    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path, 'geckodriver.exe') #文件还没放到webdriver里
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    #selenium 支持分布式 grid ==>配置（你自己的代码编写，配置，其他的人电脑配置）
    def __get_remote_drvier(self):
        pass
if __name__ == '__main__':
    pass
    #BrowserDriver().get_chrome_driver() #无法调用，只能在类的内部使用


