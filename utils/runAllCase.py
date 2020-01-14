import os,sys,time
import unittest
from HTMLTestRunner import HTMLTestRunner

class RunAllCase():

    @classmethod
    def setUpClass(cls):
        print("------测试开始执行------")

    @staticmethod
    def run_all():
        try:
            report_path = os.path.dirname(os.getcwd())
            # 格式化当前时间
            # now = time.strftime("%Y%m%d-%H%M%S", time.localtime())
            file_path = report_path + "/report/"
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            file_name = file_path + "result.html"
            # 指定要运行哪些测试用例
            test_model = "../cases/"
            discover = unittest.defaultTestLoader.discover(test_model, pattern="test*.py")

            with open(file_name, "wb") as f:
                # 将运行结果记录在测试报告中
                runner = HTMLTestRunner(stream=f, verbosity=2, title="测试报告", description="用例运行详细信息")
                runner.run(discover)
        finally:
            f.close()

    @classmethod
    def tearDownClass(cls):

        print("------测试结束------")


if __name__ == '__main__':
    RunAllCase.setUpClass()
    RunAllCase.run_all()
    RunAllCase.tearDownClass()