# coding = utf-8

import unittest
from page.sjsq import *
from common.re_token import get_token

class Test_buqian(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()

    def test_01_bq(self):
        '''上班补签申请，内容填写完整'''
        ret = bq_sq(self.token,ltype="1",date="2018-09-18 09:00", type=1,reason="我要补签")
        self.assertEqual(ret,0,msg=u"上班补签用例执行失败")
    def test_02_bq(self):
        '''下班补签申请，内容填写完整'''
        ret = bq_sq(self.token,ltype="1",date="2018-09-18 18:00", type=2,reason="我要补签下班")
        self.assertEqual(ret,0, msg="u下班补签用例执行失败")
    def test_03_bq(self):
        ret = bq_sq(self.token,ltype="2",date="2018-09-18 10:00", type=1,reason="我要补签迟到")
        self.assertEqual(ret,2,msg="用例执行失败")

if __name__ == "__main__":
    unittest.main()

