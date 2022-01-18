# @time 2022/1/11 10:14
# @Author howell
# @File smj_utils.PY
import pymysql
import os
from common.writelog import WriteLog
from common.controlconfig import ReadConfig
import requests
import json
from jinja2 import Template

filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'smjconfig.ini'))
filepath_data = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'smjdata.ini'))
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
            self.s.headers = {"Authorization": "Bearer " + response['data']['accessToken']}
            return self.s
        except KeyError:
            WriteLog(filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    def login_c(self, uid):
        sql = "SELECT token FROM smj_member_access_token WHERE uid = %s" % uid
        token = QueryData().get_data(sql)[0][0]
        if token:
            self.s.headers['auth-key'] = 'Bearer ' + token
            self.s.headers['authorization'] = 'Bearer ' + token
            WriteLog(filepath_write_log).write_str(content="用户" + str(uid) + "在C端登录成功")
            return self.s
        else:
            WriteLog(filepath_write_log).write_str(content="登录失败,数据库中没有找到token")
            return None


def get(*args, **kwargs):
    s = args[0]
    url = args[1]
    p = s.get(url=url, params=kwargs)
    t = WriteLog(filepath_write_log)
    t.write_str(content="请求地址是：%s" % url)
    t.write_str(content="请求参数是：%s" % str(kwargs))
    t.write_str(content="请求返回结果：%s " % p.json())
    return p.json()


def post(*args, **kwargs):
    s = args[0]
    url = args[1]
    p = s.post(url=url, json=kwargs)
    t = WriteLog(filepath_write_log)
    t.write_str(content="请求地址是：%s" % url)
    t.write_str(content="请求参数是：%s" % str(kwargs))
    t.write_str(content="请求返回结果：%s " % p.json())
    return p.json()


# 获取详细地址的经纬度
def get_map(address):
    url = r"https://apis.map.qq.com/ws/geocoder/v1/?key=T5OBZ-KJKWI-AFMGR-5GL4Z-6AED6-75BNH&output=jsonp&callback=QQmap"
    data = {"address": address}
    p = requests.get(url=url, params=data, verify=True)
    string_temp = p.text[13:][:-1]
    try:
        json_data = json.loads(string_temp)
        return json_data
    except BaseException as err:
        WriteLog(filepath_write_log).write_str(content="发生异常，获取地址返回信息" + p.text)


def add_code(method="get", methed_name=None):
    tmp_get_class = """ 

    def {{methed}}(self, **kwargs):
        url = get_url(self.host, "{{methed}}")
        data = {{data}}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    data_temp = {}
    InterfaceModule(s).{{methed}}(**data_temp)

    """
    tmp_post_class = """ 

    def {{methed}}(self, **kwargs):
        url = get_url(self.host, "{{methed}}")
        data = {{data}}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    data_temp = {}
    InterfaceModule(s).{{methed}}(**data_temp)

    """
    result = ""
    file_name = "smjb.py"
    if method == "get" and methed_name is not None:
        data_temp = ReadConfig(filepath_data).get("request_data", methed_name)
        result = render(tmp_get_class, methed=methed_name, data=data_temp)

    elif method == "post".strip() and methed_name is not None:
        data_temp = ReadConfig(filepath_data).get("request_data", methed_name)
        result = render(tmp_post_class, methed=methed_name, data=data_temp)
    else:
        print("传参错误")
        return
    readFile = open(file_name, encoding='utf-8')
    lines = readFile.readlines()
    readFile.close()
    w = open(file_name, 'w', encoding='utf-8')
    w.writelines([item for item in lines[:-4]])
    w.close()
    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write("    ")
        f.write(result)


def render(tmpl, *args, **kwds):
    '''jinja2 render'''
    vars = dict(*args, **kwds)
    tmp = Template(tmpl)
    return tmp.render(vars).strip()


if __name__ == '__main__':
    # sql = "SELECT * FROM `smj-dev`.`smj_goods_attr_item` LIMIT 0, 2"
    # result = QueryData().get_data(sql)
    # print(result)
    # Login().login_c(2)
    # s = get_map("龙泉驿区")
    # print(s['result']['location'])
    add_code("post", "admin_login")
