import json
import os
from  testdata import *

class OperateJson():

    @staticmethod
    def get_json(file_name):
        try:
            if file_name:
                project_path = os.path.dirname(os.getcwd())
                print(project_path)
                files_name = project_path + "/testdata/" + file_name
                print(files_name)

                with open(files_name, "r", encoding='utf-8') as data_file:
                    data = json.load(data_file)
                    return data
            else:
                return "测试数据不能为空"

        except FileNotFoundError:
            print("读取文件异常")



if __name__ == "__main__":
    res = OperateJson.get_json("login.json")
    print(res[1]["expResult"])
    print(type(res[0]))

