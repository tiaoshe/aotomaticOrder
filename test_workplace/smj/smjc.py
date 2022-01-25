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
    def add_address(self, **kwargs):
        url = get_url(self.host, "add_address")
        data = {"id": "", "name": faker.name(), "phone": faker.phone_number(), "address": "水电费水电费", "id_card_name": "",
                "id_card": "",
                "is_default": 0, "province": "四川省", "province_id": 510000, "city": "成都市", "city_id": 510100,
                "district": "金牛区", "district_id": 510106, "full_address": "四川省成都市金牛区水电费水电费", "appName": "超享团",
                "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                "deviceModel": "microsoft"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 下单
    def submmit_order(self, **kwargs):
        url = get_url(self.host, "submmit_order")
        data = {"type": 1, "bargain_id": 0, "buy_insurance": 0, "join_store": 0, "goods_id": "100005500",
                "sku_id": "100004566", "nums": 1, "couponNeedNum": 1, "cart_ids": "",
                "address_ids": "122",
                "coupon_id": "", "extend": {"100005500": {"buy_insurance": 0, "buyer_message": ""}},
                "scene": "null", "source": "null", "shopId": "31002"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 支付
    def pay_order(self, **kwargs):
        url = get_url(self.host, "pay_order")
        data = {"order_sn": "21112509570557172", "pay_info": [{"money": 100, "check": 1, "type": "balance"},
                                                              {"money": 0, "check": 0, "type": "vip_card"},
                                                              {"money": 0, "check": 0, "type": "wx"}]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 礼品卡绑定
    def bind_gift_card(self, **kwargs):
        url = get_url(self.host, "bind_gift_card")
        data = {"code": "ad non Duis sint mollit", "password": "ex cillum reprehenderit laborum irure"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


if __name__ == '__main__':
    s = Login().login_c(2)
    data_temp = {}
    InterfaceModuleApi(s).submmit_order(**data_temp)
