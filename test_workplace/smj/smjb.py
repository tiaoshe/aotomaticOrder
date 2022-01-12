# @time 2022/1/11 16:52
# @Author howell
# @File smjb.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil

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
        data = {"uid": 2, "type": 3, "money": 100, "remark": "加钱", "password": "110114"}
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

    # 优惠券列表
    def vip_card_list(self, **kwargs):
        url = get_url(self.host, "vip_card_list")
        data = {"uid": "", "type": "", "start_at": "", "end_at": "", "page": "", "pageSize": "", "up_down": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
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


if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    datatemp = {}
    InterfaceModule(s).member_list(**datatemp)
