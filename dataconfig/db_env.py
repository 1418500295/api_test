
class DbEnvironment():

    @staticmethod
    def db_envir(env):

        if env == "test":
            db_config = {
                'host': '10.10.10.33',
                'port': 3306,
                'user': 'root',
                'passwd': '123456',
                'db': 'test',
                'charset': 'utf8'
        }
        if env == "dev":
            db_config = {
                'host': '10.10.10.32',
                'port': 3306,
                'user': 'root',
                'passwd': '123456',
                'db': 'python_ui',
                'charset': 'utf8'
            }
        return db_config


