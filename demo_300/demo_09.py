# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
# file_name: test_abc.py
import pymysql
import os
from common.writelog import WriteLog
from common.controlconfig import ReadConfig
import requests, random, time
import json
from jinja2 import Template

filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'smjconfig.ini'))
filepath_data = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'smjdata.ini'))
filepath_write_log = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'smj.log'))


class QueryData(object):
    def __init__(self):
        self.conn, self.cur = self.connect_mysql()

    # 链接数据库
    def connect_mysql(self):
        conn = pymysql.connect(host='47.108.206.84', user='admin', passwd='gwUuVyOsjdb2', port=3306,
                               db='smj_server_lemeng',
                               charset='utf8mb4')
        cur = conn.cursor()  # 生成游标对象
        return conn, cur

    def get_data(self, str_sql):
        try:
            q = self.cur.execute(str_sql)  # 执行查询语句
            if q != 0:
                results = self.cur.fetchall()
                # WriteLog(filepath_write_log).write_str(content="|%s|查询数据成功" % str_sql)
            else:
                # WriteLog(filepath_write_log).write_str(content="查询%s返回数据为空" % str_sql)
                results = ""
        except BaseException as err:
            # WriteLog(filepath_write_log).write_str(content="查询发生错误:%s" % err)
            results = "查询发生了异常|%s" % err
        return results

    def update_data(self, str_sql):
        self.cur.execute(str_sql)
        self.conn.commit()

    def insert_data(self, str_sql):
        self.cur.execute(str_sql)
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()


def test_query(number="13104003890"):
    sql = "SELECT customer_id FROM smj_member WHERE phone=%s" % number
    q = QueryData().get_data(sql)
    print(q)
    return q

