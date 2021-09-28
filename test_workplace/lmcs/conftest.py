# @time 2021/9/28 18:23
# @Author howell
# @File conftest.py.PY
import pytest
import os
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import requests


# @pytest.fixture()
def login_b():
    filepath = os.path.abspath(
        os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
    filepath_write_log = os.path.abspath(
        os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.txt'))
    # 传入获取配置文件的关键字
    host = ReadConfig(filepath).get("URL", "host_lmcs_b")
    interface = ReadConfig(filepath).get("lmcs_interface", "admin_login")
    url = host + interface
    print(url)
    data = {"username": "李杰1", "password": "123456"}
    s = requests.Session()
    p = s.post(url=url, json=data)
    return s


if __name__ == '__main__':
    login_b()
