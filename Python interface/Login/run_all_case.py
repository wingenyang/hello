# coding = utf-8


import unittest
import os
from Login.common import HTMLTestRunner
def add_case():
    # 测试用例路径
    casePath = r"D:\Python interface\\Login\case"
    discover = unittest.defaultTestLoader.discover(casePath, pattern="test*.py")

    # 判断存放报告的文件夹是否存在，不存在就创建
    report = r"D:\test"
    if not os.path.exists(report):
        os.mkdir(report)

    # 报告存放的位置和名称
    report = r"D:\test\\"+"result.html"
    # 打开文件，并将报告以二进制的方式写入result.html中
    fp = open(report, "wb")

    # 创建一个对象runner，将html的描述放到runnrer中
    runner = HTMLTestRunner.HTMLTestRunner(fp, title="测试报告", description="报告描述", verbosity=2)
    runner.run(discover)
    fp.close()


