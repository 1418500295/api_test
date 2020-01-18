
from dataconfig .db_config import DbConfig
coon = DbConfig.db_connect()
class DBUtils():

    @staticmethod
    def select(table_name=None, select_by=None):
        cur = coon.cursor()
        sql = "select * from %s where id = %s " % (table_name, select_by)
        cur.execute(sql)
        rs = cur.fetchone()
        cur.close()
        coon.close()
        return rs

    @staticmethod
    def update(sql):
        cur = coon.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        coon.close()
        return res





if __name__ == '__main__':
    res = DBUtils.select()
    print(res[1])
    print(type(res))





