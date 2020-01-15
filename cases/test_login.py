
from utils.run_method import RunMethod
from utils.operation_json import OperateJson
from utils.setUpCases import SetUpCase
import unittest


logger = SetUpCase.get_logger()

class RunCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        SetUpCase.add_project_path()

    def test_login_01(self):

        data = OperateJson.get_json("login.json")
        result = RunMethod.post_main(url=SetUpCase.get_url("host", "login.url",
                                                           "constant.url"), data=data[0])

        self.assertEqual(result["status"], data[0]["expResult"])
        logger.info("实际结果是" + str(result))

    def test_login_02(self):

        data = OperateJson.get_json("login.json")
        result = RunMethod.post_main(url=SetUpCase.get_url("host", "login.url",
                                                           "constant.url"), data=data[1])

        self.assertEqual(result["status"], data[1]["expResult"])
        logger.info("实际结果是" + str(result))

    def test_login_03(self):

        data = OperateJson.get_json("login.json")

        result = RunMethod.post_main(url=SetUpCase.get_url("host", "login.url",
                                                           "constant.url"), data=data[2])

        self.assertEqual(result["status"], data[2]["expResult"])
        logger.info("实际结果是" + str(result))


if __name__ == "__main__":

    unittest.main()








