import os,time
import logging #系统自带的日志模块

# 获取当前路径
current_path = os.path.dirname(__file__)
#                               Config是一个封装好的对象.log_path一个找到配置文件中路径的方法
logo_path = os.path.join(current_path, '../logos/test.log') #找到配置文件config.ini并进入

class LogoUtiles:
    def __init__(self,logofile=logo_path): #传一个默认路径
        self.logofile = logofile
        self.logger = logging.getLogger(__name__)  # 给日志创建一个对象  __name__定义一个名称
        self.logger.setLevel(level=logging.INFO)  # 设置全局日志级别 debug  info  warning error fatal ...
        # 输出到文件里面
        file_log = logging.FileHandler(self.logofile,encoding="utf-8")
        formatter = logging.Formatter('File:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)  # 日志对象配置在文件输出

    def info(self,method):  #info日志级别
        self.logger.info(method)  # 日志对象配置在文件输出
    def error(self,method):  #info日志级别
        self.logger.error(method)  # 日志对象配置在文件输出

logo_utiles = LogoUtiles()
if __name__ == '__main__':
    logo_utiles = LogoUtiles()
    logo_utiles.info("newdream")