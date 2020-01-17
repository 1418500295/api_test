import sys
import os
from utils.operation_yaml import OperateYaml
from dataconfig.logconfig import LogConfig

class SetUpCase():

    @staticmethod
    def get_url(host, url, constant):
        yaml_data = OperateYaml.get_yaml("config.yaml")
        url = yaml_data[host] + yaml_data[url] + yaml_data[constant]
        return url

    @staticmethod
    def get_logger():

        logger = LogConfig.get_logger()
        return logger

    @staticmethod
    def add_project_path():
        project_path = os.path.dirname(os.getcwd())
        sys.path.append(project_path)


if __name__ == '__main__':
    url = SetUpCase.get_url("host", "login.url", "constant.url")
    print(url)
