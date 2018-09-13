# coding = utf-8

import requests
import unittest
from zentao.Login_api import *
import urllib3
urllib3.disable_warnings()
import re

class Login(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.z = Login_api(self.s)
        self.z.login("admin", "123456")

    def test01(self):
        ret = self.z.login("admin", "123456")
        print(ret)


    def test02(self):

        rw = self.z.wj_shangchuan("39.jpg","D:\\imgs\\39.jpg")
        print(rw)
        return rw


    def test03(self):
        re = self.z.bd_tijiao("40.jpg","D:\\imgs\\40.jpg")
        print(re)
        return re


if __name__ == "__main__":
    unittest.main()