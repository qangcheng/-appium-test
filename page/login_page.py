"""
进入登录页面完成登录流程
"""

from common.desired_cadps import desired_conf
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from common.common_fun import Common
import time


class login(Common):
    # 登录相关元素
    username_type = (By.ID, "com.tal.kaoyan:id/loginEmailEdittext")
    Password_type = (By.ID, "com.tal.kaoyan:id/loginPasswordEdittext")
    Check_button = (By.ID, "com.tal.kaoyan:id/loginTreatyCheckboxPassword")
    login_button = (By.ID, "com.tal.kaoyan:id/loginLoginBtn")
    colse_button = (By.ID, "com.tal.kaoyan:i    d/ivAdViewClose")
    forget_password_button = (By.XPATH, "//*[@text='忘记密码']")
    verification_code_login_button = (By.XPATH, "//*[@text='验证码登录/注册']")
    Other_login_button = (By.XPATH, "//*[@text='密码登录']")

    # 登出相关元素
    usercenter_setting_button = (By.ID, "com.tal.kaoyan:id/usercenter_setting")
    logout_button = (By.ID, "com.tal.kaoyan:id/setting_logout_text")
    tip_commit_button = (By.ID, "com.tal.kaoyan:id/tip_commit")
    Not_logged = (By.XPATH, "//*[@text='未登录']")

    # 输入账号
    def input_User(self, username):
        self.sendKeys(self.username_type, username)

    # 输入密码
    def input_psw(self, psw):
        self.sendKeys(self.Password_type, psw)

    # 忘记密码
    def Click_forget_password(self):
        self.click(self.forget_password_button)

    # 点击同意用户协议按钮
    def Click_Agreement_button(self):
        self.click(self.Check_button)

    # 点击验证码登录
    def Click_Verification_code_login(self):
        self.click(self.verification_code_login_button)

    # 点击登录按钮
    def Click_login_button(self):
        self.click(self.login_button)

    # 点击其他登录方式
    def Click_Other_login(self):
        self.click(self.Other_login_button)

    # 用户登录流程
    def psw_login(self, username, psw):
        self.check_password_loginbutton()
        self.Click_Other_login()
        logging.info('========Enter the account number========')
        logging.info('username is:%s' % username)
        self.input_User(username)
        logging.info('========enter password========')
        logging.info('password is:%s' % psw)
        self.input_psw(psw)
        logging.info("========Check_button========")
        self.Click_Agreement_button()
        self.Click_login_button()
        # self.check_loginStatus()

    # 用户退出登录相关流程
    def User_logout(self):
        self.click(self.my_button)
        self.click(self.usercenter_setting_button)
        self.click(self.logout_button)
        self.click(self.tip_commit_button)

    # 检查用户是否成功退出登录
    def Check_Logout_Operation(self):
        try:
            self.findElement(self.Not_logged)
        except NoSuchElementException:
            logging.info("用户登出失败")
            self.getScreenShot("用户登出失败")
            return False
        else:
            logging.info("用户登出成功")
            self.getScreenShot("用户登出录成功")
            return True

    # 进入首页后登录检测弹窗是否存在，先调用关闭弹窗方法
    def check_loginStatus(self):
        logging.info('=====Check_Loginstatus===')
        self.check_narket_ad()
        time.sleep(3)
        try:
            # 调用原生方法和封装方法区别体现
            self.driver.find_element(*self.my_button).click()
        except:
            logging.info("未登录成功：未找到的元素my_button：{}".format(self.my_button))
            return False
        else:
            logging.info("login success!")
            self.getScreenShot("login_success")
            time.sleep(3)
            return True


if __name__ == '__main__':
    driver = desired_conf()
    L = login(driver)
    L.psw_login(username="13632721415", psw="Chuiling@950720")
    L.User_logout()
    L.Check_Logout_Operation()
