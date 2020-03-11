
class DbEnvironment():

    @staticmethod
    def db_envir(env):

        if env == "test":
            db_config = {
                'host': '',
                'port': 3306,
                'user': '',
                'passwd': '',
                'db': 'test',
                'charset': 'utf8'
        }
        if env == "dev":
            db_config = {
                'host': '',
                'port': 3306,
                'user': '',
                'passwd': '',
                'db': 'python_ui',
                'charset': 'utf8'
            }
        return db_config


