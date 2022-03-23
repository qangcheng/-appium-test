# coding=utf-8


import unittest
from common.desired_cadps import desired_conf
import logging


class startEnd(unittest.TestCase):
    def setUp(self):
        logging.info("====setup====")
        self.driver = desired_conf()

    def tearDown(self):
        logging.info("==== TearDowm =====")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
