# @time 2021/9/29 11:18
# @Author howell
# @File lmcs_utils.PY
import requests
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import os


class Login(object):
    def __init__(self, host_url, login_api):
        filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.txt'))
        # 传入获取配置文件的关键字
        self.host = ReadConfig(filepath).get("URL", host_url)
        self.interface = ReadConfig(filepath).get("lmcs_interface", login_api)
        self.url = self.host + self.interface
        self.s = requests.Session()
        self.login = login_api

    def login_b(self):
        data = {}
        user = "李杰1"
        data['username'] = user
        data['password'] = "123456"
        response = self.s.post(url=self.url, json=data)
        try:
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['accessToken']}
            WriteLog(self.filepath_write_log).write_str(content=user + "在B端登录成功")
            return self.s
        except KeyError:
            WriteLog(self.filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    def login_c(self):
        pass


class CommonRequest(object):
    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.txt'))
        self.host = ReadConfig(self.filepath).get("URL", "host_lmcs_b")
        self.s = Login("host_lmcs_b", "admin_login").login_b()

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


if __name__ == '__main__':
    Login("host_star_b", "admin_login").login_b()
