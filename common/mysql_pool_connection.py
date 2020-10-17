import pymysql
from dbutils.pooled_db import PooledDB

from config.mysql_config import MYSQL_CONFIG


class Connect(object):
    def __init__(self, pool_obj):
        self.pool = pool_obj

    def execute(self, query, args=None):
        connection = self.pool.connection()
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            res = cursor.fetchall()
        connection.close()
        return res

    def execute_commit(self, query, args=None):
        connection = self.pool.connection()
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            connection.commit()
        connection.close()


MYSQL_pool = PooledDB(pymysql, **MYSQL_CONFIG)
MYSQL_pool_connection = Connect(MYSQL_pool)
