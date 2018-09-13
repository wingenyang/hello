# coding = utf-8

import requests
import unittest
from lianxi04.login_api import login

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def test01_login(self):
        ret = login(self.s, "admin", "123456")
        self.assertIn("parent.location", ret)

    def test02_login(self):

        ret = login(self.s,"admin1", "123456")
        self.assertIn("登录失败，请检查您的用户名或密码是否填写正确",ret)


