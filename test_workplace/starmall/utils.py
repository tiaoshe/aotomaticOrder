# @time 2021/9/18 15:09
# @Author howell
# @File utils.PY
import requests
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import os


class Login(object):
    def __init__(self, host_url, login_api):
        filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'log.txt'))
        # 传入获取配置文件的关键字
        self.host = ReadConfig(filepath).get("URL", host_url)
        self.interface = ReadConfig(filepath).get("interface", login_api)
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
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['token']}
            WriteLog(self.filepath_write_log).write_str(content=user + "在B端登录成功")
            return self.s
        except KeyError:
            WriteLog(self.filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    def login_c(self):
        pass


if __name__ == '__main__':
    Login("host_star_b", "admin_login").login_b()
