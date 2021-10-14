"""
编写人员：陈强
switchAvatarview工程的优化代码，更加优化到代码相关的各个元素，从面向过程到面向对象，封装各个元素的API方便测试人员编写时更换方便简单
针对个人资料页面的各个元素的入口封装，示例：更换头像流程
"""

from kyb_testproject.common.desired_cadps import desired_conf
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import random
from kyb_testproject.businessview.login_page import login


class personal_information_page(login):
    # "关于我的"模块元素
    My_entrance_button = (By.ID, "com.tal.kaoyan:id/activity_usercenter_userheader")
    Avatar_entrance_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_header_arrow")
    Back_button = (By.ID, "com.tal.kaoyan:id/myapptitle_leftbutton_image")

    # "关于考研"模块元素
    Change_nickname_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_uname")
    year_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_yeartextview")
    Apply_Majors_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_majortextview")
    Apply_college_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_schtextview")
    Subjects_applied_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_subjecttextview")

    # "基本情况"模块元素
    School_goals_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_school_target")
    Preparation_status_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_examed_times")
    current_state_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_work_status")
    Colleges_button = (By.ID, "com.tal.kaoyan:id/activity_myinfo_bschooltextview")

    # 更换头像流程权限元素
    good_button = (By.XPATH, "//*[@text='好的']")
    Always_allowed_button = (By.XPATH, "//*[@text='始终允许']")
    images = (By.ID, "com.tal.kaoyan:id/ivPicture")
    picture_tv_ok_button = (By.ID, "com.tal.kaoyan:id/picture_tv_ok")
    Crop_button = (By.XPATH, '//android.widget.TextView[@content-desc="裁剪"]')

    def Click_back(self):
        """点击返回按钮"""
        self.click(self.Back_button)

    def Click_Avatar(self):
        """点击我的页面头像入口"""
        self.click(self.My_entrance_button)

    def Click_Change_Avatar(self):
        """点击头像更换入口"""
        self.click(self.Avatar_entrance_button)

    def Click_Year(self):
        """点击考研年份入口"""
        self.click(self.year_button)

    def Click_Apply_Majors(self):
        """点击报考专业入口"""
        self.click(self.Apply_Majors_button)

    def Click_Apply_college(self):
        """点击报考院校入口"""
        self.click(self.Apply_college_button)

    def Click_Subjects_applied(self):
        """点击报考科目入口"""
        self.click(self.Subjects_applied_button)

    def Click_School_goals(self):
        """点击院校目标入口"""
        self.click(self.School_goals_button)

    def Click_Preparation_Status(self):
        """点击备考状态入口"""
        self.click(self.Preparation_status_button)

    def Click_Current_State(self):
        """点击目前状态入口"""
        self.click(self.current_state_button)

    def Click_Colleges(self):
        """点击本科院校入口"""
        self.click(self.Colleges_button)

    def Click_Change_Nickname(self):
        """更换昵称"""
        self.sendKeys(self.Change_nickname_button, text="admin")

    # 跟换头像用例流程
    def Change_Avatar_Process(self, username, psw):
        """进入跟换头像入口"""
        self.psw_login(username, psw)
        self.Click_Avatar()
        logging.info("====Click on the avatar entry successfully=====")
        self.Click_Change_Avatar()
        self.getScreenShot("Click on the avatar entry successfully")
        logging.info("====Click on the avatar to change the entrance successfully====")
        # 校验是否需要获取到权限相关
        try:
            self.findElement(self.good_button)
        except NoSuchElementException:
            self.Select_Picture_Process()
        else:
            self.click(self.good_button)
            logging.info("====Permission（好的） obtained successfully====")
            self.click(self.Always_allowed_button)
            logging.info("====Permission（总是允许） obtained successfully====")
            self.Select_Picture_Process()

    def Select_Picture_Process(self):
        """选择图片流程"""
        a = random.randint(1, 10)
        self.driver.find_elements(*self.images)[a].click()
        logging.info("Select photo successfully,Change the photo to:%s", a)
        self.getScreenShot("Select photo successfully")
        time.sleep(2)
        self.click(self.picture_tv_ok_button)
        time.sleep(2)
        self.click(self.Crop_button)
        logging.info("====Change the avatar successfully======")
        self.getScreenShot("Change the avatar successfully")
        time.sleep(3)
        self.Check_replace_avatar()

    # 校验头像更换是否跟换成功，做unittest需要校验是否成功
    def Check_replace_avatar(self):
        """校验头像更换是否跟换成功，做unittest需要校验是否成功"""
        try:
            self.findElement(self.Back_button)
            logging.info("====Photo verification succeeded:更换头像成功====")
            self.getScreenShot("Photo verification succeeded")
            logging.info("更换头像成功")
            return True
        except NoSuchElementException:
            logging.info("====Failed to change avatar====")
            return False


if __name__ == '__main__':
    driver = desired_conf()
    L = personal_information_page(driver)
    L.Change_Avatar_Process(username="13632721415", psw="Chuiling@950720")
