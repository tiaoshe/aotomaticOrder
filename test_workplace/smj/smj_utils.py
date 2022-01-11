# @time 2022/1/11 10:14
# @Author howell
# @File smj_utils.PY
import pymysql
import os
from common.writelog import WriteLog
from common.controlconfig import ReadConfig
import requests

filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'smjconfig.ini'))
filepath_write_log = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'smj.log'))


def get_url(host, api):
    host_temp = ReadConfig(filepath).get("URL", host)
    api_temp = ReadConfig(filepath).get("smj_interface", api)
    url = host_temp + api_temp
    return url


class QueryData(object):
    def __init__(self):
        self.conn, self.cur = self.connect_mysql()

    # 链接数据库
    @staticmethod
    def connect_mysql():
        conn = pymysql.connect(host='112.124.11.179', user='admin', passwd='gwUuVyOsjdb2', port=3306, db='smj-dev',
                               charset='utf8mb4')
        cur = conn.cursor()  # 生成游标对象
        return conn, cur

    def get_data(self, str_sql):
        try:
            q = self.cur.execute(str_sql)  # 执行查询语句
            if q != 0:
                results = self.cur.fetchall()
                WriteLog(filepath_write_log).write_str(content="|%s|查询数据成功" % str_sql)
            else:
                WriteLog(filepath_write_log).write_str(content="查询%s返回数据为空" % str_sql)
                results = "查询结果为空"
        except BaseException as err:
            WriteLog(filepath_write_log).write_str(content="查询发生错误:%s" % err)
            results = "查询发生了异常|%s" % err
        return results

    def __del__(self):
        self.cur.close()
        self.conn.close()


class Login(object):
    def __init__(self):
        self.s = requests.Session()

    def login_b(self, host_url, login_api):
        url = get_url(host_url, login_api)
        data = dict()
        user = "李杰2"
        data['username'] = user
        data['password'] = "123456"
        response = post(self.s, url, **data)
        try:
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['accessToken']}
            return self.s
        except KeyError:
            WriteLog(filepath_write_log).write_str(content="登录接口报错")
            print(response.json())


def get(*args, **kwargs):
    s = args[0]
    url = args[1]
    p = s.get(url=url, params=kwargs)
    WriteLog(filepath_write_log).write_str(content="请求%s返回结果：%s " % (url, p.json()))
    return p


def post(*args, **kwargs):
    s = args[0]
    url = args[1]
    p = s.post(url=url, json=kwargs)
    WriteLog(filepath_write_log).write_str(content="请求%s返回结果：%s " % (url, p.json()))
    return p


if __name__ == '__main__':
    # sql = "SELECT * FROM `smj-dev`.`smj_goods_attr_item` LIMIT 0, 2"
    # result = QueryData().get_data(sql)
    # print(result)
    Login().login_b("host_smj_b", "admin_login")
