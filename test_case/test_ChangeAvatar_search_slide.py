import time
from kyb_testproject.common.myunit import startEnd
from kyb_testproject.businessview.personal_information_page import personal_information_page
import logging
import unittest
from kyb_testproject.businessview.Home_page import Home_page


class TestSlide(startEnd):
    def test_slide_1(self):
        logging.info("====Slide_Test  ====")
        K = personal_information_page(self.driver)
        K.Change_Avatar_Process(username="13632721415", psw="Chuiling@950720")
        self.assertTrue(K.Check_replace_avatar(), msg="Photo verification succeeded")
        time.sleep(2)

    def test_Search_Jump_2(self):
        logging.info("====Search_Jump====")
        L = Home_page(self.driver)
        L.Search_Shake_Case(username="13632721415", psw="Chuiling@950720", text="心理学")
        self.assertTrue(L.Check_Search(), msg="Search jump success")


if __name__ == '__main__':
    unittest.main()
