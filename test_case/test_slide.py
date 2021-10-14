import time
from kyb_testproject.common.myunit import startEnd
from kyb_testproject.businessview.SwitchAvatarview import Switch_avatar
import logging
import unittest
from kyb_testproject.businessview.Home_search import Home_search


class TestSlide(startEnd):
    def test_slide_1(self):
        logging.info("====Slide_Test  ====")
        K = Switch_avatar(self.driver)
        time.sleep(2)
        self.assertTrue(K.Change_Avatar(), msg="slide in success")

    def test_Search_Jump_2(self):
        logging.info("====Search_Jump====")
        L = Home_search(self.driver)
        time.sleep(2)
        self.assertTrue(L.Home_search_case(), msg="Search jump success")


if __name__ == '__main__':
    unittest.main()
