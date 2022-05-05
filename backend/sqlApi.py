import psycopg2
from psycopg2 import pool
from private import DATABASE_CONFIG
import requests


class mysqlConnect(object):
    def __init__(self, connectConfig=DATABASE_CONFIG):
        try:
            self.connectPool = pool.SimpleConnectionPool(2, 10, **DATABASE_CONFIG, keepalives=1,
                                                         keepalives_idle=30, keepalives_interval=10,
                                                         keepalives_count=5)
        except Exception as e:
            print(e)

    def __conn(self):
        self.connect = self.connectPool.getconn()
        self.cursor = self.connect.cursor()

    def query(self, sql: str = ''):
        """
        :param sql: sql语句
        :return: 是否执行成功, sql执行结果
        """
        self.__conn()
        try:
            result = self.cursor.execute(sql)
            self.connect.commit()
            return True, result
        except psycopg2.Error as e:
            print("Error Type:{}\n Execute sql:{}".format(e.pgcode, sql))
            return False, e

    def select(self, sql: str, length=None):
        """
        :param sql: sql查询语句
        :return: 是否查询成功， sql查询结果
        """
        self.__conn()
        try:
            if length is not None:
                sql = "%s LIMIT %d;" % (sql, length)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return True, result
        except psycopg2.Error as e:
            print("Error Type:{}\n Select Error:{}".format(e.pgcode, sql))
            return False, None

    def __del__(self):
        self.connectPool.closeall()
