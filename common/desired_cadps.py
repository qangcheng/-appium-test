# coding=utf-8
"""

yaml封装后读取config/capbilty.yaml文件已写入数据
 logging参数输出info 以上级别的日志,指定文件地址输出,asctime =当前时间，filename=模块名称，lineno=行号，
 levelname = 日志等级名称，message=日志信息

"""
from appium import webdriver
import yaml
import logging
import logging.config
import time
import os
from common.resd_yaml import readyml

# 读取log.conf中的配置表
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# yamlpath
a = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
capbilly_path = os.path.join(a, "config", "capbillty.yaml")
# print(capbilly_path)
# readyml(capbilly_path)


def desired_conf():
    # 读取yaml配置表中的配置,不写close,也不会出现文件未释放的问题
    # with open(r"D:\codetest\kyb_testproject\config\capbillty.yaml", 'r', encoding="UTF-8") as file:
    #     data = yaml.load(file, Loader=yaml.FullLoader)
    data = readyml(capbilly_path)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, "app", data['appPackage'])
    # desired_caps['app'] = app_path         电脑数据包安装需要读取APK路径本地安装了就不需要
    desired_caps['udid'] = data['udid']
    desired_caps['noReset'] = data['noReset']  # app 是否初始化启动
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    logging.info("....Start App.....")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    logging.info(desired_caps)

    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    desired_conf()
# 获取到当前APP模块的存放的APP路径，从电脑安装APP的路径时需要使用到的方法，手机本地已安装的不用使用到下面读取方法
# with open(r"D:\codetest\kyb_testproject\config\capbillty.yaml", 'r', encoding="UTF-8") as file:
#     data = yaml.load(file)
# base_dir = os.path.dirname(os.path.dirname(__file__))
# print(os.path.dirname(__file__))
# print(base_dir)
# app_path = os.path.join(base_dir,"app", data['appPackage'])
# print(app_path)
