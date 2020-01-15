import yaml
import os

class OperateYaml():

    @staticmethod
    def get_yaml(file_name):
        try:

            if file_name:
                project_path = os.path.dirname(os.getcwd())
                target_file_name = project_path + "/" + file_name
                yaml_file = open(target_file_name, "r", encoding="utf-8")
                yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                return yaml_data

            else:
                return "yaml文件不存在"

        except FileNotFoundError as e:
            print(e)

        finally:
            yaml_file.close()


if __name__ == "__main__":
    yaml_data = OperateYaml.get_yaml("config.yaml")
    print(yaml_data)





