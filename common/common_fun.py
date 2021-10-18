"""
登录初始化操作，获取权限，跳过引导页等流程
"""
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from kyb_testproject.baseView.baseview import BaseView
from kyb_testproject.common.desired_cadps import desired_conf
import csv


class Common(BaseView):
    Agree_button = (By.ID, "com.tal.kaoyan:id/tip_commit")
    Ikown_button = (By.ID, "com.tal.kaoyan:id/tv_ok")
    Experiencenow_button = (By.ID, "com.tal.kaoyan:id/activity_splash_guidfinish")
    canceblanbutton = (By.ID, "com.tal.kaoyan:id/login_code_touname")
    closebutton = (By.ID, "com.tal.kaoyan:id/ivAdViewClose")
    my_button = (By.XPATH, "//*[@text='我的']")

    # 应用初始化登录进入登录界面
    def __init__(self, driver):
        super().__init__(driver)
        self.new = time.strftime("%Y-%m-%d %H_%M_%S")

    def check_password_loginbutton(self):
        """初始化登录前置条件"""
        logging.info("============check Agree_button=============")
        try:
            Agree_button = self.driver.find_element(*self.Agree_button)
        except NoSuchElementException as e:
            logging.info(e)
        else:
            Agree_button.click()
            time.sleep(5)
            logging.info("===========check_known_button===============:")
            try:
                Ikown_button = self.driver.find_element(*self.Ikown_button)
            except NoSuchElementException as s:
                logging.info(s)
            else:
                Ikown_button.click()
                time.sleep(5)
                logging.info("=============check Experiencing_button=============:")
                try:
                    Experiencenow_button = self.driver.find_element(*self.Experiencenow_button)
                except NoSuchElementException as g:
                    logging.info(g)
                else:
                    Experiencenow_button.click()
                    time.sleep(5)
                    logging.info("=============check canceblan_button=============:")
                    try:
                        canceblan_button = self.driver.find_element(*self.canceblanbutton)
                    except NoSuchElementException as U:
                        logging.info(U)
                    else:
                        canceblan_button.click()
                        time.sleep(6)

    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def Swipe_left(self):
        logging.info("SwipeLeft")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.9)
        y1 = int(L[1] * 0.5)
        x2 = int(L[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向右滑动
    def Swipe_right(self):
        logging.info("SwipeRight")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.9)
        y1 = int(L[1] * 0.5)
        x2 = int(L[0] * 0.1)
        self.driver.swipe(x2, y1, x1, y1, 1000)

    # 向上滑动
    def Swipe_Up(self):
        logging.info(" SwipeUp")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.5)
        y1 = int(L[1] * 0.5)
        y2 = int(L[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 向下滑动
    def Swipe_Down(self):
        logging.info(" SwipeDown")
        L = self.get_size()
        print(L)
        x1 = int(L[0] * 0.5)
        y1 = int(L[1] * 0.5)
        y2 = int(L[1] * 0.8)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 左下角向上滑动
    def Swipe_Left_Up(self):
        logging.info(" LeapLefTup")
        L = self.get_size()
        x1 = int(L[0] * 0.3)
        y1 = int(L[1] * 0.9)
        y2 = int(L[1] * 0.7)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 左下角向下滑动
    def Swipe_Left_Down(self):
        logging.info(" SwipeLeftDown")
        L = self.get_size()
        x1 = int(L[0] * 0.3)
        y1 = int(L[1] * 0.9)
        y2 = int(L[1] * 0.7)
        self.driver.swipe(x1, y2, x1, y1, 1000)

    # 获取当前时间
    def getTime(self):
        return self.new

    # 截取当前页面图片
    def getScreenShot(self, module):
        Time = self.getTime()
        image_ile = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, Time)
        logging.info("get %s screenshot" % module)
        self.driver.get_screenshot_as_file(image_ile)
        # 打印当前页面平台选择
        # print(self.driver.contexts)

    # 端内切换测试平台 CS/BS
    def Switch_platform(self, platform):
        self.Switch_To_Default_Content(platform)

    # 关闭首页广告弹窗
    def check_narket_ad(self):
        time.sleep(2)
        logging.info("====check_close_button====")
        try:
            close_button = self.driver.find_element(*self.closebutton)
        except NoSuchElementException:
           pass
        else:
            logging.info("====close_market_ad=====")
            # 等待元素加载方法
            WebDriverWait(self.driver, 3).until(
                lambda x: x.find_element_by_id("com.tal.kaoyan:id/ivAdViewClose"))
            close_button.click()

    # 读取csv文件
    def Get_Scv_Data(self, csv_file, line):
        logging.info("=====get_scv_data======")
        with open(csv_file, "r", encoding="utf-8-sig") as file:  # 防止出现非法字符使用sig方法
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):  # 需要获取到第几行的参数数据就改为几行
                if index == line:
                    return row


if __name__ == '__main__':
    driver = desired_conf()
    com = Common(driver)
    com.check_password_loginbutton()
    com.get_size()
    com.getScreenShot("StarApp")
    com.Switch_platform('NATIVE_APP')
