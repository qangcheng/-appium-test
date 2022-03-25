from common.myunit import startEnd
from businessview.login_page import login
import logging
import random
import unittest


class TestLogin(startEnd):
    csv_file = "../data/account.csv"

    def test_login_1(self):
        logging.info("==== test_login ：13632721415 ====")
        L = login(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 1)  # 调用csv读取方法，获取账号密码
        L.psw_login(data[0], data[1])
        self.assertTrue(L.check_loginStatus(), msg="log in success")

    # @unittest.skip("skip case  test_login_2")  # 跳过某条用例
    def test_login_2(self):
        logging.info("==== test_login :5555 ====")
        L = login(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 2)
        L.psw_login(data[0], data[1])
        self.assertFalse(L.check_loginStatus(), msg="log in fail")

    # @unittest.skip("skip  case  test_login_3")  # 跳过某条用例
    def test_login_3(self):
        logging.info("==== test_login : 3333 ====")
        L = login(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 3)
        L.psw_login(data[0], data[1])
        self.assertFalse(L.check_loginStatus(), msg="log in fail")

    def test_logout_4(self):
        logging.info("==== test_logout ====")
        logging.info("==== test_login ：13632721415 ====")
        L = login(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 1)  # 调用csv读取方法，获取账号密码
        L.psw_login(data[0], data[1])
        L.User_logout()
        self.assertTrue(L.Check_Logout_Operation())


if __name__ == '__main__':
    unittest.main()
