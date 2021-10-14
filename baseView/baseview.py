import logging
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 1

    #  单个元素定位方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 多个元素list定位方法
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 新的定位方法,与findElement方法返回一致
    def findElementNew(self, locator):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            logging.info("正在点各位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 单个元素等待方法封装，调用这个方法可以返回定位元素，比sleep和隐示等待更加稳定
    def findElement(self, locator):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            logging.info("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 一组元素等待方法封装，调用这个方法可以返回定位元素，比sleep和隐示等待更加稳定
    def findElements(self, locator):
        if not isinstance(locator, tuple):
            logging.info('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            logging.info("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    # 封装input方法
    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        return ele.send_keys(text)

    # 封装点击方法
    def click(self, locator):
        ele = self.findElement(locator)
        return ele.click()

    # 封装清除内容方法
    def clear(self, locator):
        ele = self.findElement(locator)
        return ele.clear()

    # 获取屏幕大小方法
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动方法
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 端内切换测试平台 web&Android
    def Switch_To_Default_Content(self, platform):
        return self.driver.switch_to_default_content(platform)

    # 结束当前服务,避免端口号占用报错
    def close_service(self):
        return self.driver.quit()

    # 获取应用当前页面涉及平台
    def get_contexts(self):
        return print(self.driver.contexts)

    # Schamea跳转
    def Schamea_Jump(self, link):
        return os.popen("adb -d shell am start -a android.intent.action.VIEW -d" + link)


if __name__ == '__main__':
        pass