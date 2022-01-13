# @time 2022/1/11 16:53
# @Author howell
# @File smjc.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))


class InterfaceModuleApi(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_c"

    # 添加用户地址
    def add_address(self):
        url = get_url(self.host, "add_address")
        data = {"id": "", "name": faker.name(), "phone": "13980883526", "address": "水电费水电费", "id_card_name": "",
                "id_card": "",
                "is_default": 0, "province": "四川省", "province_id": 510000, "city": "成都市", "city_id": 510100,
                "district": "金牛区", "district_id": 510106, "full_address": "四川省成都市金牛区水电费水电费", "appName": "超享团",
                "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                "deviceModel": "microsoft"}
        response = post(self.s, url, **data)
        print(response)
        return response


if __name__ == '__main__':
    s = Login().login_c(2)
    data_temp = {}
    InterfaceModuleApi(s).add_address(**data_temp)
