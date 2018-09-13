# coding =utf-8



import os
import unittest
from HRMS_test.common import HTMLTestRunner

# 获取项目实际路径
curpath = os.path.dirname(os.path.relpath(__file__))

# 报告路径是项目实际路径下的report文件夹
report_path = os.path.join(curpath, "report")

# 判断报告路径是否存在，如果不存在就创建
if os.path.exists(report_path):
    os.mkdir(report_path)

# 测试用例的实际路径
case_path = os.path.join(curpath,"case")

def add_case(casepath=case_path, rule="test*.py" ):
    '''加载所有测试用例'''
    # 创建discover 对象，加载所有测试用例
    discover = unittest.defaultTestLoader.discover(casepath,pattern=rule)
    return discover


def run_case(all_case, reportpath=report_path):
    '''执行所有的测试用例，并把结果写入测试报告'''

    # 创建报告的格式，并把路径传给htmlreport
    htmlreport = reportpath + r"report.html"
    print("测试报告生成地址：%s" % htmlreport)
    # 以写入的方式打开报告的路径
    fp = open(htmlreport,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title="HRMS接口测试报告",description="用例执行情况")

    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)