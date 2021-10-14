import logging
import time
from kyb_testproject.common.desired_cadps import desired_conf
from kyb_testproject.businessview.loginview import loginview
from selenium.webdriver.common.by import By
from kyb_testproject.baseView import baseview
from selenium.common.exceptions import NoSuchElementException
from kyb_testproject.businessview.login_page import login


class Home_search(login, loginview):
    # 首页入口元素
    mainactivity_button = (By.ID, "com.tal.kaoyan:id/mainactivity_button_calendar")
    search_for_button = (By.ID, "com.tal.kaoyan:id/imageSearch")

    # 搜索页面元素
    Input_box = (By.ID, "com.tal.kaoyan:id/customsearchview_contentedittext")
    SouSuo_button = (By.XPATH, "//*[@text='搜索']")

    # 搜索结果页面滑动操作
    def Home_search_case(self):
        # self.login_actihon("13632721415", "Chuiling@950720")
        self.psw_login(username="13632721415", psw="Chuiling@950720")
        self.check_loginstatus()
        self.driver.find_element(*self.mainactivity_button).click()
        self.driver.find_element(*self.search_for_button).click()
        time.sleep(2)
        self.driver.find_element(*self.Input_box).send_keys("心理学")
        try:
            self.driver.find_element(*self.SouSuo_button)
            time.sleep(2)
        except NoSuchElementException:
            logging.info("====Search entry jump failed======")
            self.getScreenShot("Search entry jump failed")
            return False
        else:
            self.getScreenShot("The search entry jumped successfully")
            logging.info("The search entry jumped successfully")
            for i in range(2):
                self.Swipe_left()
                logging.info("=====Swipe left:" + str(i+1) + "次=====")
                time.sleep(2)
                self.getScreenShot("Swipe left"+str(i+1)+"次")
            for i in range(2):
                self.Swipe_right()
                logging.info("=====Swipe right:" + str(i+1) + "次=====")
                time.sleep(2)
                self.getScreenShot("Swipe right"+str(i+1)+"次")
            for i in range(2):
                self.Swipe_Up()
                logging.info("=====Swipe Up:" + str(i+1) + "次=====")
                time.sleep(1)
                self.getScreenShot("Swipe Up"+str(i+1)+"次")
            for i in range(2):
                self.Swipe_Down()
                logging.info("=====Swipe Down" + str(i+1) + "次=====")
                time.sleep(1)
                self.getScreenShot("Swipe Down"+str(i+1)+"次")
            return True


if __name__ == '__main__':
    drvier = desired_conf()
    o = Home_search(drvier)
    o.Home_search_case()


