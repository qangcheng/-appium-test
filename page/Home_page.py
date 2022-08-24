from common.desired_cadps import desired_conf
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import random
from page.login_page import login


class Home_page(login):
    # 首页入口搜索相关元素
    home_button = (By.ID, "com.tal.kaoyan:id/mainactivity_button_calendar")
    search_button = (By.ID, "com.tal.kaoyan:id/imageSearch")
    Input_button = (By.ID, "com.tal.kaoyan:id/customsearchview_contentedittext")
    SouSu_button = (By.XPATH, "//*[@text='搜索']")

    def Click_Home(self):
        """点击首页入口元素"""
        self.click(self.home_button)

    def Click_Search(self):
        """点击搜索框"""
        self.click(self.search_button)

    def Input_Search(self, text):
        """输入搜索内容"""
        self.clear(self.Input_button)
        self.sendKeys(self.Input_button, text)

    def Click_Sousu(self):
        """点击输入内容后的搜素按钮"""
        self.click(self.SouSu_button)

    # 搜索滑动用例流程
    def Search_Shake_Case(self, username, psw, text):
        self.psw_login(username, psw)
        self.Click_Home()
        time.sleep(2)
        logging.info("====My youstar_page returns to the search youstar_page====")
        self.Click_Search()
        self.Input_Search(text)
        logging.info("====Enter search content:%s====" % text)
        self.getScreenShot(text)
        self.Click_Sousu()
        logging.info("====Search content succeeded===")
        self.getScreenShot("Search content succeeded")
        self.Search_swipe()
        self.Check_Search()

    # 滑动两次方法封装，后续用例根据自己需求封装
    def Search_swipe(self):
        for i in range(2):
            self.Swipe_left()
            logging.info("=====Swipe left:" + str(i + 1) + "次=====")
            time.sleep(2)
        for i in range(2):
            self.Swipe_right()
            logging.info("=====Swipe right:" + str(i + 1) + "次=====")
            time.sleep(2)
            self.getScreenShot("Swipe right" + str(i + 1) + "次")
        for i in range(2):
            self.Swipe_Up()
            logging.info("=====Swipe Up:" + str(i + 1) + "次=====")
            time.sleep(1)
            self.getScreenShot("Swipe Up" + str(i + 1) + "次")
        for i in range(2):
            self.Swipe_Down()
            logging.info("=====Swipe Down" + str(i + 1) + "次=====")
            time.sleep(1)
            self.getScreenShot("Swipe Down" + str(i + 1) + "次")

    # 校验头像更换是否跟换成功，做unittest需要校验是否成功
    def Check_Search(self):
        try:
            self.findElement(self.SouSu_button)
            logging.info("校验元素成功！:%s" % str(self.SouSu_button))
            return True

        except NoSuchElementException:
            logging.info("没有找到校验元素:%s" % str(self.SouSu_button))
            return False


if __name__ == '__main__':
    driver = desired_conf()
    L = Home_page(driver)
    L.Search_Shake_Case(username="13632721415", psw="Chuiling@950720", text="心理学")