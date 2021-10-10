# @time 2021/9/29 11:18
# @Author howell
# @File lmcs_utils.PY
import requests
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import os
import pymysql


class Login(object):
    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.log'))
        self.s = requests.Session()

    def login_b(self, host_url, login_api):
        # 传入获取配置文件的关键字
        host = ReadConfig(self.filepath).get("URL", host_url)
        interface = ReadConfig(self.filepath).get("lmcs_interface", login_api)
        url = host + interface
        data = {}
        user = "李杰1"
        data['username'] = user
        data['password'] = "123456"
        response = self.s.post(url=url, json=data)
        try:
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['accessToken']}
            WriteLog(self.filepath_write_log).write_str(content=user + "在B端登录成功")
            return self.s
        except KeyError:
            WriteLog(self.filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    # 链接数据库
    def conn_mysql(self):
        conn = pymysql.connect(host='118.31.18.87', user='admin', passwd='gwUuVyOsjdb2', port=3306, db='lmcs-dev',
                               charset='utf8mb4')
        cur = conn.cursor()  # 生成游标对象
        return conn, cur

    # 获取用户列表中的token
    def get_token(self, uid):
        conn, cur = self.conn_mysql()
        sql = "SELECT token FROM `dcyg-dev`.`dcyg_member_access_token` WHERE `uid` = %s" % uid
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                token = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % uid)
        except:
            WriteLog(self.filepath_write_log).write_str(content="get_token数据库发生异常了")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return token

    def login_c(self, uid):
        token = self.get_token(uid)
        if token:
            self.s.headers['auth-key'] = 'Bearer ' + token
            self.s.headers['authorization'] = 'Bearer ' + token
            WriteLog(self.filepath_write_log).write_str(content="用户" + str(uid) + "在C端登录成功")
            return self.s
        else:
            WriteLog(self.filepath_write_log).write_str(content="登录失败")
            return None


class CommonRequest(object):
    def __init__(self, test_to, session=None):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.log'))
        if test_to == "B":
            self.host = ReadConfig(self.filepath).get("URL", "host_lmcs_b")
            self.s = Login().login_b("host_lmcs_b", "admin_login")
        elif test_to == "C":
            self.host = ReadConfig(self.filepath).get("URL", "host_lmcs_c")
            self.s = session

    def get(self, *getargs, **kwargs):
        api = ReadConfig(self.filepath).get("lmcs_interface", *getargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, params=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def post(self, *postargs, **kwargs):
        api = ReadConfig(self.filepath).get("lmcs_interface", *postargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用post方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.post(url=url, json=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def get_download(self, *downloadargs, **kwargs):
        """
        :param downloadargs: 0 传入接口对应的 参数名称
        :param kwargs:
        :return:
        """
        api = ReadConfig(self.filepath).get("lmcs_interface", *downloadargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, stream=True, params=kwargs)
        # 文件名称
        file_to_save = os.path.join(os.getcwd(), downloadargs[1])
        try:
            with open(file_to_save, "wb") as fw:
                fw.write(p.content)
        except PermissionError:
            WriteLog(self.filepath_write_log).write_str(content="文件处于打开状态请手动关闭")
            return "文件处于打开状态请手动关闭"
        return "ok"


if __name__ == '__main__':
    uids = 10001535
    c = Login().login_c(uids)
    print(c)
