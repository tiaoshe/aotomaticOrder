# @time 2022/1/11 16:52
# @Author howell
# @File smjb.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))


class InterfaceModule(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_b"

    # 添加优惠券
    def add_coupon(self, **kwargs):
        url = get_url(self.host, "add_coupon")
        data = {"type": 0, "cat_id": "103", "ding_at": 1638892800,
                "goods_ids": "100000367,100000400,100000405", "day": 7, "name": "打了卡是否接了", "max": "50.00",
                "money": "10.00", "is_overlay": 0, "num": 67, "user_num": 10, "start_at": 1638892800,
                "end_at": 1640188800, "created_at": 1639018359, "updated_at": 1641780313, "sort": 0, "delflag": 0,
                "description": "eeeeeee", "member_type": "1,2", "ding_at_end": 1640880000, "category": 1,
                "grant_type": "giveout,receive", "support_receive": 1, "channel": 1, "use_type": 1, "range": 2}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 优惠券编辑
    def edit_coupon(self, **kwargs):
        url = get_url(self.host, "edit_coupon")
        data = {"id": 12323, "type": 0, "cat_id": "103", "ding_at": 1638892800,
                "goods_ids": "100000367,100000400,100000405", "day": 7, "name": "打了卡是否接了", "max": "50.00",
                "money": "10.00", "is_overlay": 0, "num": 67, "user_num": 10, "start_at": 1638892800,
                "end_at": 1640188800, "created_at": 1639018359, "updated_at": 1641780313, "sort": 0, "delflag": 0,
                "description": "eeeeeee", "member_type": "1,2", "ding_at_end": 1640880000, "category": 1,
                "grant_type": "giveout,receive", "support_receive": 1, "channel": 1, "use_type": 1, "range": 2}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 会员卡加扣款
    def update_vip_card(self, **kwargs):
        url = get_url(self.host, "update_vip_card")
        data = {"uid": 2, "type": 3, "money": 99.99, "remark": "加钱", "password": "110114"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加公告
    def add_notice(self, **kwargs):
        url = get_url(self.host, "add_notice")
        data = {"title": "dolor", "is_enable": 93228930.09150541, "content": "aliquip occaecat pariatur elit dolor",
                "type_relation": 16874601.815701112, "shop_offline_ids": [-89259424.57724592],
                "effect_time_begin": "sint nulla culpa incididunt",
                "effect_time_end": "fugiat occaecat dolore officia incididunt"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 编辑公告
    def edit_notice(self, **kwargs):
        url = get_url(self.host, "edit_notice")
        data = {"id": -28723042.60814835, "title": "reprehenderit voluptate culpa cupidatat in",
                "is_enable": -75002766.33752012, "content": "pariatur id velit nostrud tempor",
                "type_relation": -27070548.76755777, "shop_offline_ids": [78357404.2210119],
                "effect_time_begin": "in ex tempor veniam cupidatat", "effect_time_end": "cupidatat enim aliquip"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加轮播
    def add_banner(self, **kwargs):
        url = get_url(self.host, "add_banner")
        data = {"sort": -92000625.26075369, "description": "ut cupidatat dolore sunt", "type": "ut",
                "param": "dolore eiusmod ipsum", "is_enable": -31741505.799358413,
                "main_color": "labore Ut dolore eu qui", "name": "velit pariatur dolor est dolor",
                "location": -2241020.391069263, "banner": "sit velit fugiat deserunt aliquip",
                "type_relation": -53601215.22166206, "area_ids": [-79824109.51455608],
                "shop_offline_ids": [91536190.30098575, 18229438.652062774]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 编辑轮播
    def edit_banner(self, **kwargs):
        url = get_url(self.host, "edit_banner")
        data = {"id": -45342545.973600015, "description": "ullamco Excepteur ut in occaecat",
                "type": "dolor nostrud eiusmod irure culpa", "param": "reprehenderit non dolore amet irure",
                "is_enable": 49283112.61302918, "main_color": "in dolor", "name": "proident",
                "location": 52734751.928685784, "banner": "do Ut consectetur", "type_relation": 49981337.896598846,
                "field_1": "exercitation ad adipisicing", "field_2": "cillum ut", "field_3": 81313900.33183175,
                "area_ids": [29707540.5431785],
                "shop_offline_ids": [-86081051.91612232, -44664002.882979006, -39552209.59002208, -46112102.18630087]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 后台余额加扣款
    def update_money(self, **kwargs):
        url = get_url(self.host, "update_money")
        data = {"uid": 2, "type": 9, "money": 100, "remark": "加钱", "password": "110114"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加活动区域
    def add_special_activity(self, **kwargs):
        url = get_url(self.host, "add_special_activity")
        data = {"id": -28723042.60814835, "title": "reprehenderit voluptate culpa cupidatat in",
                "is_enable": -75002766.33752012, "content": "pariatur id velit nostrud tempor",
                "type_relation": -27070548.76755777, "shop_offline_ids": [78357404.2210119],
                "effect_time_begin": "in ex tempor veniam cupidatat", "effect_time_end": "cupidatat enim aliquip"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 晋升审核
    def examine_store_apply(self, **kwargs):
        url = get_url(self.host, "examine_store_apply")
        data = {"id": -28723042.60814835, "title": "reprehenderit voluptate culpa cupidatat in",
                "is_enable": -75002766.33752012, "content": "pariatur id velit nostrud tempor",
                "type_relation": -27070548.76755777, "shop_offline_ids": [78357404.2210119],
                "effect_time_begin": "in ex tempor veniam cupidatat", "effect_time_end": "cupidatat enim aliquip"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加超市或服务门店
    def add_shop_offline(self, **kwargs):
        url = get_url(self.host, "add_shop_offline")
        data = {"name": faker.company() + str(random.randint(1, 10000)), "contact_phone": "13980883526", "type": 1,
                "address": "四川省成都市龙泉驿区", "province_id": "510000", "city_id": "510100",
                "district_id": "510112", "note": "这个是商超", "status": 1,
                "latitude": "30.577833", "longitude": "104.240829", "template_id": 643, "business_at": "12点到凌晨12点",
                "area_ids": "500000,500100,500300,510000,510100,510300,510400,510500,510600,510700,510800,510900,511000,511100,511300,511400,511500,511600,511700,511800,511900,512000,513200,513300,513400,520000,520100,520200,520300,520400,520500,520600,522300,522600,522700"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 积分加扣
    def update_integral_record(self, **kwargs):
        url = get_url(self.host, "update_integral_record")
        data = {"uid": 2, "type": 1, "point": 1000, "password": "123456", "remark": "备注"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 积分设置
    def integral_set_config(self, **kwargs):
        url = get_url(self.host, "integral_set_config")
        data = {"sign_integral": 100, "referer_integral": 100, "online_integral": 100, "offline_integral": 100,
                "deduction_integral": 100}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加供应商
    def add_supplier(self, **kwargs):
        url = get_url(self.host, "add_supplier")
        data = {"name": "好难得", "en_name": "haonande", "brief": "reprehenderit",
                "return_text": ["mollit anim pariatur", "dolor aute sint", "in ad ex occaecat",
                                "laboris aliquip dolore est irure", "in aliquip quis sint"],
                "phone": "13980883526", "status": 10, "link_man": "aliqua in do reprehenderit",
                "link_id_front": "dolore officia dolore eu voluptate", "link_id_backend": "in",
                "license": "aliqua laboris irure"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    #
    # # 编辑公告
    # def edit_notice(self, **kwargs):
    #     url = get_url(self.host, "edit_notice")
    #     data = {"id": -28723042.60814835, "title": "reprehenderit voluptate culpa cupidatat in",
    #             "is_enable": -75002766.33752012, "content": "pariatur id velit nostrud tempor",
    #             "type_relation": -27070548.76755777, "shop_offline_ids": [78357404.2210119],
    #             "effect_time_begin": "in ex tempor veniam cupidatat", "effect_time_end": "cupidatat enim aliquip"}
    #     for key, value in kwargs.items():
    #         data[key] = value
    #     response = post(self.s, url, **data)
    #     return response
    #
    # # 编辑公告
    # def edit_notice(self, **kwargs):
    #     url = get_url(self.host, "edit_notice")
    #     data = {"id": -28723042.60814835, "title": "reprehenderit voluptate culpa cupidatat in",
    #             "is_enable": -75002766.33752012, "content": "pariatur id velit nostrud tempor",
    #             "type_relation": -27070548.76755777, "shop_offline_ids": [78357404.2210119],
    #             "effect_time_begin": "in ex tempor veniam cupidatat", "effect_time_end": "cupidatat enim aliquip"}
    #     for key, value in kwargs.items():
    #         data[key] = value
    #     response = post(self.s, url, **data)
    #     return response
    #
    # 优惠券列表
    def coupon_list(self, **kwargs):
        url = get_url(self.host, "coupon_list")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 优惠券列表
    def notice_list(self, **kwargs):
        url = get_url(self.host, "notice_list")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 会员卡明细
    def vip_card_list(self, **kwargs):
        url = get_url(self.host, "vip_card_list")
        # data = {"uid": "2", "type": "", "start_at": "", "end_at": "", "page": "", "pageSize": "", "up_down": ""}
        data = {"uid": "2"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 用户列表
    def member_list(self, **kwargs):
        url = get_url(self.host, "member_list")
        # data = {"uid": "", "username": "", "type": "-1", "phone": "", "first_uid": "", "from": "", "channel": "",
        #         "status": "", "start_time": "", "end_time": "", "login_start": "", "login_end": "", "page": 1,
        #         "pageSize": 30, "tag": ""}
        data = {"type": "-1", "page": 1, "pageSize": 30}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 超市列表
    def shop_offline_list(self, **kwargs):
        url = get_url(self.host, "shop_offline_list")
        data = {"type": 1, "page": 1, "pageSize": 10, "name": "佳禾网络有限公司8610", "province_id": "", "city_id": "", }
        # data = {"type": 1, "page": 26}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 仓库列表
    def warehouse_list(self, **kwargs):
        url = get_url(self.host, "warehouse_list")
        # data = {"type": 1, "page": 1, "pageSize": 10, "name": "", "province_id": "", "city_id": "", }
        data = {"type": 1, "page": 1, "pageSize": 10, "keywords": "黄"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 用户详情-左侧数据
    def member_info(self, **kwargs):
        url = get_url(self.host, "member_info")
        data = {"uid": 3}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 余额明细
    def balance_record_list(self, **kwargs):
        url = get_url(self.host, "balance_record_list")
        data = {"uid": 2}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 积分明细列表
    def integral_record_list(self, **kwargs):
        url = get_url(self.host, "integral_record_list")
        data = {"uid": 2}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 用户优惠券列表
    def member_coupons_list(self, **kwargs):
        url = get_url(self.host, "member_coupons_list")
        data = {"uid": 2, "page": 1, "pageSize": 10, "used_status": 0, "receive_type": 0, "use_type": 4,
                "receive_time": "", "use_time": "", "coupon_name": "", "order_sn": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # B端查询用户地址
    def member_address_list(self, **kwargs):
        url = get_url(self.host, "member_address_list")
        data = {"uid": 2, "page": 1, "pageSize": 10, "phone": "13980883526", "name": "史莉"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # B端查询用户地址
    def login_log_list(self, **kwargs):
        url = get_url(self.host, "login_log_list")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 晋升管理列表
    def store_apply_list(self, **kwargs):
        url = get_url(self.host, "store_apply_list")
        data = {"status": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 供应商列表
    def supplier_list(self, **kwargs):
        url = get_url(self.host, "supplier_list")
        data = {"status": 10}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response


if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    datatemp = {}
    InterfaceModule(s).supplier_list(**datatemp)
