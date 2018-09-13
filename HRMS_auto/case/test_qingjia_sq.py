# coding = utf-8

import unittest
from common.re_token import get_token
from page.sjsq import qj_sq

class Test_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()


    def test_01_qj(self):
        '''请假申请成功'''
        ret = qj_sq(self.token,type="5",start="2018-09-18 09:00",end= "2018-09-18 18:00", reason="我需要请假", handover="20")
        self.assertEqual(ret, 0, msg=u"用例执行失败")

if __name__ == "__main__":
    unittest.main()