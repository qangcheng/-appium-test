from kyb_testproject.common.desired_cadps import desired_conf
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import random
from kyb_testproject.businessview.login_page import login
from kyb_testproject.businessview.loginview import loginview

a = random.randint(0, 10)

csv_file = '../data/account.csv'


class Switch_avatar(login, loginview):
    # 头像入口相关元素
    Avatar_button = (By.ID, "com.tal.kaoyan:id/activity_usercenter_userheader")
    Avatar_entrance = (By.ID, "com.tal.kaoyan:id/activity_myinfo_header_arrow")
    picture_tv_ok_button = (By.ID, "com.tal.kaoyan:id/picture_tv_ok")
    Back_button = (By.ID, "com.tal.kaoyan:id/myapptitle_leftbutton_image")

    # 获取权限相关元素
    good_button = (By.XPATH, "//*[@text='好的']")
    Always_allowed_button = (By.XPATH, "//*[@text='始终允许']")
    images = (By.ID, "com.tal.kaoyan:id/ivPicture")
    Crop_button = (By.XPATH, '//android.widget.TextView[@content-desc="裁剪"]')

    # 点击头像
    def Change_Avatar(self):
        self.psw_login(username="13632721415", psw="Chuiling@950720")
        self.check_loginstatus()
        # self.driver.find_element(*self.Avatar_button).click()
        self.click(self.Avatar_button)
        try:

            self.driver.find_element(*self.Avatar_entrance)
        except NoSuchElementException:
            logging.error("====Click on the avatar no response====")
            self.getScreenShot("Click on the avatar no response")
            return False
        else:
            self.click(self.Avatar_entrance)
            logging.info("====entered the change avatar page Successfully=====")
            self.Get_Permission()
            return True

    # 个人详情页面上传头像全流程
    def Get_Permission(self):
        try:
            # self.driver.find_element(*self.good_button).click()
            self.click(self.good_button)
        except NoSuchElementException:
            #  不用获取权限流程
            self.Upload_process()
            time.sleep(2)
            self.close_service()
        else:
            # 需要获取权限流程
            for i in range(1):
                self.driver.find_element(*self.Always_allowed_button).click()
                time.sleep(2)
            self.Upload_process()

    # 头像上传流程
    def Upload_process(self):
        try:
           images_button = self.driver.find_elements(*self.images)
        except NoSuchElementException:
            logging.info("====No available material found====")
            return False
        else:
            images_button[a].click()
            time.sleep(2)
            logging.info("Switched the %s  photos" % a)
            self.getScreenShot('Switched the %s photos' % a)
            self.driver.find_element(*self.picture_tv_ok_button).click()
            self.driver.find_element(*self.Crop_button).click()
            time.sleep(2)
            self.driver.find_element(*self.Back_button).click()
            try:
                self.driver.find_element(*self.Avatar_button)
            except NoSuchElementException:
                logging.info("Failed to return to my page")
                return False
            else:
                logging.info("=====Change the avatar successfully======")
                self.getScreenShot("Change the avatar successfully")
                self.Logout_Action()
                return True
                # 头像上传完成后再调用登出方法


if __name__ == '__main__':
    driver = desired_conf()
    k = Switch_avatar(driver)
    k.Change_Avatar()
