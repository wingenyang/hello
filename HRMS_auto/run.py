# coding = utf-8

import unittest
import os
import yaml
from common import HTMLTestRunner
from ruamel import yaml
import requests

# 获取项目真实路径
curpath = os.path.dirname(os.path.relpath(__file__))


def login(user="15673200007",psw="123456"):
    url = "http://www.hrms.com/api/doLogin"
    d = {
        "username": user,
        "password": psw

    }
    r = requests.post(url, data=d)
    return r.json()["token"]

def write_yaml(value):
    # 创建一个对象存放token的路径，通过os.path.join()进行关联
    ypath = os.path.join(curpath, "common","token.yaml")
    # 需要写入的内容
    t = {"token": value}
    # 写入到yaml文件中
    with open(ypath, "w", encoding="utf-8") as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)

def all_case(rule="test*.py"):
    case_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), "case")
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover

def run_case(all_case,reportName="report"):
    curpath = os.path.dirname(os.path.relpath(__file__))

    report_path = os.path.join(curpath, reportName) # 用例文件夹

    # 判断存放测试报告的文件夹是否存在，不存在则创建
    if not os.path.exists(report_path): os.mkdir(report_path)
    # 创建一个接收测试报告的对象，通过os.path.join()进行关联
    report_abspath = os.path.join(report_path,"result.html")
    # 以写入的方式打开存放测试报告的文件
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title=u"自动化测试报告，测试结果如下：", description=u"用例执行情况：")
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    token = login()
    write_yaml(token)
    allcases = all_case()
    run_case(allcases)



