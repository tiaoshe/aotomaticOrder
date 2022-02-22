# @time 2022/2/21 11:57
# @Author howell
# @File smjpsc.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_c_report.xls'))


class InterfaceQSApi(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_c"

    # 骑手登录
    def rider_login(self, **kwargs):
        url = get_url(self.host, "rider_login")
        data = {"phone": "18512816620", "code": "", "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 骑手端获取验证码
    def get_rider_code(self, **kwargs):
        url = get_url(self.host, "get_rider_code")
        # 类型：1.注册 2.找回密码 3.老手机号验证 4.重置登录密码 5.重置支付密码 6.新手机号绑定 7.验证码登录
        data = {"phone": "18512816620", "type": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 骑手登录
    def get_rider_agreement(self, **kwargs):
        url = get_url(self.host, "get_rider_agreement")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response
