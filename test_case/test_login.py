from kyb_testproject.common.myunit import startEnd
from kyb_testproject.businessview.loginview import loginview
import logging
import random
import unittest


class TestLogin(startEnd):
    csv_file = "../data/account.csv"

    def test_login_1(self):
        logging.info("==== test_login ：13632721415 ====")
        L = loginview(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 1)  # 调用csv读取方法，获取账号密码
        L.login_actihon(data[0], data[1])
        self.assertTrue(L.check_loginstatus(), msg="log in success")

    # @unittest.skip("skip case  test_login_2")  # 跳过某条用例
    def test_login_2(self):
        logging.info("==== test_login :5555 ====")
        L = loginview(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 2)
        L.login_actihon(data[0], data[1])
        self.assertTrue(L.check_loginstatus(), msg="log in fail")

    # @unittest.skip("skip  case  test_login_3")  # 跳过某条用例
    def test_login_3(self):
        logging.info("==== test_login : 3333 ====")
        L = loginview(self.driver)
        data = L.Get_Scv_Data(self.csv_file, 3)
        L.login_actihon(data[0], data[1])
        self.assertTrue(L.check_loginstatus(), msg="log in fail")


if __name__ == '__main__':
    unittest.main()
