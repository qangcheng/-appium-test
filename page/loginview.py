"""
进入登录页面完成登录流程
"""


from common.desired_cadps import desired_conf
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from common.common_fun import Common
import time


class loginview(Common):
    # 登录相关元素
    username_type = (By.ID, "com.tal.kaoyan:id/login_email_edittext")
    Password_type = (By.ID, "com.tal.kaoyan:id/login_password_edittext")
    Check_button = (By.CLASS_NAME, "android.widget.CheckBox")
    login_button = (By.ID, "com.tal.kaoyan:id/login_login_btn")
    colse_button = (By.ID, "com.tal.kaoyan:id/ivAdViewClose")

    # 登出相关元素
    usercenter_setting_button = (By.ID, "com.tal.kaoyan:id/usercenter_setting")
    logout_button = (By.ID, "com.tal.kaoyan:id/setting_logout_text")
    tip_commit_button = (By.ID, "com.tal.kaoyan:id/tip_commit")
    name_button = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")

    def login_actihon(self, username, password):
        # 用户登录流程
        self.check_password_loginbutton()
        logging.info('========Enter the account number========')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('========enter password========')
        logging.info('password is:%s' % password)
        self.driver.find_element(*self.Password_type).send_keys(password)
        logging.info("========Check_button========")
        try:
            Checkbutton = self.driver.find_element(*self.Check_button)
        except NoSuchElementException as errocode_one:
            logging.info(errocode_one)
        else:
            Checkbutton.click()
            time.sleep(3)
        logging.info("========login_action========")
        try:
            loginbutton = self.driver.find_element(*self.login_button)
        except NoSuchElementException as errocode_two:
            logging.info(errocode_two)
        else:
            loginbutton.click()

    # 进入首页后登录检测弹窗是否存在，先调用关闭弹窗方法
    def check_loginstatus(self):
        logging.info('=====Check_Loginstatus===')
        self.check_narket_ad()
        time.sleep(3)

        try:
            self.driver.find_element(*self.my_button).click()
        except NoSuchElementException:
            logging.error("login_fail!!!!")
            self.getScreenShot('login_fail')
            return False
        else:
            logging.info("login success!")
            self.getScreenShot("login_success")
            time.sleep(3)
            return True

    # 应用内登出操作
    def Logout_Action(self):
        logging.info("=====Logout_action=====")
        self.driver.find_element(*self.usercenter_setting_button).click()
        self.driver.find_element(*self.logout_button).click()
        self.driver.find_element(*self.tip_commit_button).click()
        try:
            Not_logged = self.driver.find_element(*self.name_button)
        except NoSuchElementException:
            logging.info('=====Logout_Fail===')
            self.getScreenShot("Logout_Fail")
            return False
        else:
            logging.info("logout_success!")
            self.getScreenShot("Logout_success") 
            return True


if __name__ == '__main__':
    driver = desired_conf()
    L = loginview(driver)
    L.login_actihon("13632721415", "Chuiling@950720")
    L.check_loginstatus()
    L.Logout_Action()
    time.sleep(2)


