import pymysql
from DBUtils.PooledDB import PooledDB
from dataconfig.db_env import DbEnvironment

db_config = DbEnvironment.db_envir("test")

class DbConfig():

    @staticmethod
    def db_connect():
        db_connection = PooledDB(pymysql, 5,
                                 host=db_config["host"],
                                 user=db_config["user"],
                                 passwd=db_config["passwd"],
                                 port=db_config["port"],
                                 db=db_config["db"],
                                 charset=db_config["charset"]).connection()
        return db_connection







