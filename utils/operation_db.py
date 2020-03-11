
from dataconfig .db_config import DbConfig
coon = DbConfig.db_connect()
class DBUtils():

    @staticmethod
    def select(table_name=None, id=None):
        cur = coon.cursor()
        sql = "select * from %s where id = %s " % (table_name, id)
        cur.execute(sql)
        rs = cur.fetchone()
        coon.commit()
        cur.close()
        coon.close()
        return rs

    @staticmethod
    def update(sql):
        cur = coon.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        coon.close()
        return res





if __name__ == '__main__':
    rs = DBUtils.select("user", "1")
    print(rs)






