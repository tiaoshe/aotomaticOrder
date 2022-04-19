# @time 2022/2/21 11:57
# @Author howell
# @File smjpsc.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random
import requests
import string

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_c_report.xls'))
host = "host_smj_qs"
s = requests.Session()


# 骑手登录
def rider_login(phone):
    url = get_url(host, "rider_login")
    # data_1 = {"phone": phone, "type": "7"}
    # code_1 = get_rider_code(**data_1)['code']
    code_1 = "123456"
    deviceId = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    data_2 = {"phone": phone, "code": code_1, "status": 1, "deviceId": deviceId}
    response = post(s, url, **data_2)
    return response


def get_phone_number():
    sql = "select phone from smj_rider where `status`=1 and delflag=0;"
    return QueryData().get_data(sql)


# 骑手端获取验证码
def get_rider_code(**kwargs):
    url = get_url(host, "get_rider_code")
    # 类型：1.注册 2.找回密码 3.老手机号验证 4.重置登录密码 5.重置支付密码 6.新手机号绑定 7.验证码登录
    data = {"phone": "18512816620", "type": "7"}
    for key, value in kwargs.items():
        data[key] = value
    response = post(s, url, **data)
    sql = "select captcha from smj_common_captcha WHERE account=%s and status=0;" % data['phone']
    code = QueryData().get_data(sql)[0][0]
    response['code'] = code
    response['phone'] = data['phone']
    return response


def get_rider_login_on(phone):
    s = requests.Session()
    sql = "select token from smj_rider where `status`=1 and delflag=0 and phone=%s" % phone
    token = QueryData().get_data(sql)[0][0]
    if token == "":
        token = rider_login(phone)['data']['token']
    s.headers = {"Authorization": "Bearer " + token}
    return s


class InterfaceQSApi(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_qs"

    # 骑手登录
    def get_rider_agreement(self, **kwargs):
        url = get_url(self.host, "get_rider_agreement")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 骑手上线
    def rider_on(self, **kwargs):
        url = get_url(self.host, "rider_on")
        data = {"status": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 骑手上报位置
    def set_position(self, **kwargs):
        url = get_url(self.host, "set_position")
        data = {"city_id": "510100", "lng": str(random.randint(103848967, 104320981) / 1000000),
                "lat": str(random.randint(30417993, 30800710) / 1000000)}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


# 让所有骑手上线
def on_all_rider():
    sql = "select phone from smj_rider where city_id=510100 and status=1 and delflag=0 and phone!=''"
    q = QueryData().get_data(sql)
    for i in range(0, len(q)):
        phone_1 = q[i][0]
        s = get_rider_login_on(phone_1)
        worker_1 = InterfaceQSApi(s)
        worker_1.rider_on()
        worker_1.set_position()


# 让所有骑手下线
def off_all_rider():
    sql = "select phone from smj_rider where city_id=510100 and status=1 and delflag=0 and phone!=''"
    q = QueryData().get_data(sql)
    for i in range(0, len(q)):
        phone_1 = q[i][0]
        s = get_rider_login_on(phone_1)
        worker_1 = InterfaceQSApi(s)
        data = {"status": 2}
        worker_1.rider_on(**data)
        if i == 100:
            return


# 更新骑手位置
def updata_rider():
    sql = "select phone from smj_rider where city_id=510100 and status=1 and delflag=0 and phone!=''"
    q = QueryData().get_data(sql)
    for i in range(0, len(q)):
        phone_1 = q[i][0]
        s = get_rider_login_on(phone_1)
        worker_1 = InterfaceQSApi(s)
        data = {"status": 2}
        worker_1.rider_on(**data)


if __name__ == '__main__':
    off_all_rider()