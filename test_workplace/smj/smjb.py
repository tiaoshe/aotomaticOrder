# @time 2022/1/11 16:52
# @Author howell
# @File smjb.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random
import time
import datetime

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))


def get_now_time(secont=0):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + secont))


def get_now_time_cuo(secont_c=0):
    return int(time.time() + secont_c)


class InterfaceModule(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_b"

    # 添加优惠券
    def add_coupon(self, **kwargs):
        url = get_url(self.host, "add_coupon")
        data = {"type": 0, "cat_id": "103", "ding_at": get_now_time_cuo(), "goods_ids": "100000367,100000400,100000405",
                "day": 7, "name": faker.sentence(), "max": "50.00", "money": "10.00", "is_overlay": 0, "num": 67,
                "user_num": 10, "start_at": get_now_time_cuo(),
                "end_at": get_now_time_cuo(72000), "sort": 0, "delflag": 0,
                "description": "这个是描述", "member_type": "1,2", "ding_at_end": get_now_time_cuo(72000), "category": 1,
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
        data = {"title": "老邓头老邓头日晒不愁下雨不愁", "is_enable": 1, "content": "这个是内容",
                "type_relation": 1, "shop_offline_ids": [31000, 31001, 31002],
                "effect_time_begin": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "effect_time_end": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 7200))}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 编辑公告
    def edit_notice(self, **kwargs):
        url = get_url(self.host, "edit_notice")
        data = {"id": 27, "title": "老邓头老邓头日晒不愁下雨不愁", "is_enable": 1, "content": "这个是内容",
                "type_relation": 1, "shop_offline_ids": [31000, 31001, 31002],
                "effect_time_begin": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "effect_time_end": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 7200))}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加轮播
    def add_banner(self, **kwargs):
        url = get_url(self.host, "add_banner")
        data = {"sort": "19", "description": "12", "type": "goods_detail", "param": "100010", "is_enable": 1,
                "main_color": "#D61818", "name": "这个是跳转商品的轮播图", "location": 1, "type_relation": "1",
                "area_ids": [120114],
                "shop_offline_ids": [31000, 31001, 31002], "banner": "https://lmcscdn.jzwp.cn/1642127426717.jpg",
                "goto_url": " "}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 编辑轮播
    def edit_banner(self, **kwargs):
        url = get_url(self.host, "edit_banner")
        data = {"id": "12", "sort": "19", "description": "12", "type": "goods_detail", "param": "100010",
                "is_enable": 1,
                "main_color": "#D61818", "name": "这个是跳转商品的轮播图", "location": 1, "type_relation": "1",
                "area_ids": [120114],
                "shop_offline_ids": [31000, 31001, 31002], "banner": "https://lmcscdn.jzwp.cn/1642127426717.jpg",
                "goto_url": " "}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 后台余额加扣款
    def update_money(self, **kwargs):
        url = get_url(self.host, "update_money")
        data = {"uid": 2, "type": 9, "money": 1000000, "remark": "加钱", "password": "110114"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加活动区域
    def add_special_activity(self, **kwargs):
        url = get_url(self.host, "add_special_activity")
        data = {"plate_index": "style_2_2", "plate_type": "2", "num": 2, "contents": [
            {"type": "goods_detail", "image": "https://lmcscdn.jzwp.cn/1642127936575.jpg", "param": "100010"},
            {"type": "my_order", "image": "https://lmcscdn.jzwp.cn/1642127945312.jpg"}], "name": "活动区域添加",
                "shop_offline_id": 31000}
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
        # 添加服务门店
        data1 = {"shop_type": "2", "pid": "31018", "name": faker.company() + str(random.randint(1, 10000)),
                 "contact_phone": "13980883526", "type": 2,
                 "address": "四川省成都市龙泉驿区", "province_id": "510000", "city_id": "510100",
                 "district_id": "510112", "status": 1, "template_id": "0",
                 "latitude": "30.577833", "longitude": "104.240829", "business_at": "12点到凌晨12点"}
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
        data = {"name": faker.sentence(), "en_name": "gysjc", "brief": "供应商简介",
                "return_text": ["1", "dolor 2 sint", "in ad ex occaecat",
                                "laboris aliquip dolore est irure", "in aliquip quis sint"],
                "phone": "13980883526", "status": 10, "link_man": faker.name(),
                "link_id_front": "https://mmtcdn.jzwp.cn/1642153002088.jpg",
                "link_id_backend": "https://mmtcdn.jzwp.cn/1642153002088.jpg",
                "license": "https://mmtcdn.jzwp.cn/1642153002088.jpg"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 优惠券发放
    def coupon_send(self, **kwargs):
        url = get_url(self.host, "coupon_send")
        data = {"coupon_id": 5278, "coupon_num": "5", "member_ids": "2"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 生成兑换码
    def coupon_exchange_sn(self, **kwargs):
        url = get_url(self.host, "coupon_exchange_sn")
        data = {"num": 20, "expire_time": "2022-01-27 00:00:00", "coupon_id": "5274"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 添加秒杀活动
    def add_seckill(self, **kwargs):
        url = get_url(self.host, "add_seckill")
        data = {"title": "圣美家秒杀" + faker.sentence(), "description": "圣美家秒杀",
                "start_time": get_now_time(),
                "end_time": get_now_time(72000),
                "shop_offline_id": "31002",
                "goods": [{"goods_id": "100005501", "single_max": "1", "single_min": "1", "day_max": "1",
                           "limit_max": "10", "virtual_percentavirtual_scores": "99.9", "sort": "1",
                           "sku": [
                               {"sku_id": "100004567", "inventory_id": "87", "kill_price": "9.9", "vip_price": "8.8",
                                "bonus_second_vip": "1", "stock": "10", "status": "0"},
                               {"sku_id": "100004568", "inventory_id": "88", "kill_price": "9.9", "vip_price": "8.8",
                                "bonus_second_vip": "1", "stock": "10", "status": "0"}]}], }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加分类
    def add_goods_category(self, **kwargs):
        url = get_url(self.host, "add_goods_category")
        # type 1 线上商品  type 2 线下商品
        data = {"name": "枪械-博睿风体验馆", "delivery": "false", "display": 0, "sort": "100", "display_index": "1",
                "thumb": ["https://fncdn.jzwp.cn/1642147340710.jpg"], "status": "1",
                "imgs": ["https://fncdn.jzwp.cn/1642147417352.jpg"], "type": "2"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加规格
    def add_attr(self, **kwargs):
        url = get_url(self.host, "add_attr")
        # type 1 线上商品  type 2 线下服务
        data = {"type": "2", "name": "容弹量-线下体验馆"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加规格
    def add_attr_item(self, **kwargs):
        url = get_url(self.host, "add_attr_item")
        # type 1 线上商品  type 2 线下商品
        data = {"name": "杜鲁门突突-线下体验", "sort": "1",
                "values": [{"value": "100", "color": "", "id": ""}, {"value": "200", "color": "", "id": ""},
                           {"value": "300", "color": "", "id": ""}, {"value": "400", "color": "", "id": ""}],
                "attr_id": "32"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 发货订单 录入快递信息
    def order_delivery(self, **kwargs):
        url = get_url(self.host, "order_delivery")
        data = {"items": [{"id": 11944, "code": "YTO", "sn": "123456789"}]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 发货订单 录入快递信息
    def order_delivery_send(self, **kwargs):
        url = get_url(self.host, "order_delivery_send")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 接单
    def order_picking_get(self, **kwargs):
        url = get_url(self.host, "order_picking_get")
        data = {"ids": ["20222"]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 拣货完成
    def order_picking_compelte(self, **kwargs):
        url = get_url(self.host, "order_picking_compelte")
        # deliver_type 1 自提  2 同城
        data = {"ids": "20222", "deliver_type": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 秒杀商品添加
    def goods_activity_seckill(self, **kwargs):
        url = get_url(self.host, "goods_activity_seckill")
        # deliver_type 1 自提  2 同城
        data = {"title": faker.sentence(), "description": "cillum mollit nisi", "start_time": get_now_time(),
                "end_time": get_now_time(72000), "shop_offline_id": 31002, "goods": [
                {"goods_id": "100005355", "single_max": 1, "single_min": 1,
                 "day_max": 1, "limit_max": 0,
                 "virtual_percentavirtual_scores": 10.1, "sort": 1, "sku": [
                    {"sku_id": "100004483", "inventory_id": 10,
                     "kill_price": 10, "vip_price": 9, "bonus_second_vip": 1, "stock": 10}, ], }, ], }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 自提完成；同城完成
    def order_send_end(self, **kwargs):
        url = get_url(self.host, "order_send_end")
        # deliver_type = 1 自提 2 同城
        # ids  订单ID
        data = {"ids": 1, "deliver_type": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 优惠券列表
    def coupon_list(self, **kwargs):
        url = get_url(self.host, "coupon_list")
        data = {"page": 1, "pageSize": 30}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 公告列表
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
        data = {"uid": 2, "page": 1, "pageSize": 10, "used_status": 0, "receive_type": 0, "use_type": 0,
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

    # 优惠券记录列表
    def coupon_record_list(self, **kwargs):
        url = get_url(self.host, "coupon_record_list")
        data = {"uid": 2, "page": 1, "pageSize": 10}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 订单列表
    def order_list(self, **kwargs):
        url = get_url(self.host, "order_list")
        data = {"page": 1, "pageSize": 10}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 推广收入
    def sub_rebate_order(self, **kwargs):
        url = get_url(self.host, "sub_rebate_order")
        data = {"uid": 2, "page": 1, "pageSize": 20, "type": "", "start_time": "", "end_time": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 秒杀列表
    def seckill_list(self, **kwargs):
        url = get_url(self.host, "seckill_list")
        data = {"title": "", "page": 1, "pageSize": 20, "type": "", "time_status": "3"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 类型变更
    def member_label_change(self, **kwargs):
        url = get_url(self.host, "member_label_change")
        data = {"page": 1, "pageSize": 20}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 自提订单列表
    def order_pick_list(self, **kwargs):
        url = get_url(self.host, "order_pick_list")
        data = {"page": 1, "pageSize": 20, "use_status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 商品秒杀列表
    def goods_activity_seckill_list(self, **kwargs):
        url = get_url(self.host, "goods_activity_seckill_list")
        data = {"page": 1, "pageSize": 20, "type": "1", "title": "", "time_status": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 秒杀详情
    def goods_activity_seckill_detail(self, **kwargs):
        url = get_url(self.host, "goods_activity_seckill_detail")
        data = {"id": "15"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 获取商品列表
    def goods_list(self, **kwargs):
        url = get_url(self.host, "goods_list")
        data = {"page": "1", "pageSize": "30"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 添加满减活动
    def add_lessen(self, **kwargs):
        url = get_url(self.host, "add_lessen")
        data = {"title": faker.sentence(), "description": faker.sentence(), "start_time": get_now_time(72000),
                "end_time": get_now_time(72120), "shop_offline_id": 31002,
                "rules": {"type": 2, "full": 10, "full_reduce": 1},
                "goods": [100005404]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def detail_lessen(self, **kwargs):
        url = get_url(self.host, "detail_lessen")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def lessen_list(self, **kwargs):
        url = get_url(self.host, "lessen_list")
        data = {"page": "1", "pageSize": "30", "title": "", "time_status": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def edit_lessen(self, **kwargs):
        url = get_url(self.host, "edit_lessen")
        data = {"id": "Excepteur elit officia incididunt esse", "description": "culpa consectetur dolore",
                "start_time": "sunt dolor", "end_time": "ea officia ut deserunt", "shop_offline_id": -78954685.14153996,
                "rules": {"type": 11704170.558594525, "full": 44166651.57021934, "full_reduce": -14647143.620123029},
                "goods": [85682218.83022839, -54188088.4199506, 61706246.243041456, -81995856.21786106],
                "field_1": "officia eiusmod", "del_goods": [-42618627.9392001, 42002115.09792334]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def del_lessen(self, **kwargs):
        url = get_url(self.host, "del_lessen")
        data = {"id": "2"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def raffle_list(self, **kwargs):
        url = get_url(self.host, "raffle_list")
        data = {"page": "1", "pageSize": "30"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def edit_rules(self, **kwargs):
        url = get_url(self.host, "edit_rules")
        data = {"id": 10, "need_integrate": 10, "free_num": 100,
                "max_num": 20}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def raffle_detail(self, **kwargs):
        url = get_url(self.host, "raffle_detail")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_raffle(self, **kwargs):
        url = get_url(self.host, "add_raffle")
        data = {"title": faker.sentence(), "type": "1", "thumb": "https://cxtcdn.jzwp.cn/1627439302135.png",
                "back_color": "#ffffff", "description": faker.sentence(), "start_time": get_now_time(),
                "end_time": get_now_time(300), "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_raffle(self, **kwargs):
        url = get_url(self.host, "edit_raffle")
        data = {"id": 69197859.0914366, "title": "proident enim dolore in consectetur", "type": 71558876.7851448,
                "thumb": "dolore quis eu mollit dolor", "back_color": "tempor enim", "description": "Duis Excepteur",
                "start_time": "sit sed nisi ut incididunt", "end_time": "ut", "status": 15039441.587011024}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_raffle_status(self, **kwargs):
        url = get_url(self.host, "edit_raffle_status")
        data = {"id": 45574981.97036728, "status": -5684234.209707424}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def del_raffle(self, **kwargs):
        url = get_url(self.host, "del_raffle")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def prize_list(self, **kwargs):
        url = get_url(self.host, "prize_list")
        data = {"page": "1", "pageSize": "30", "raffle_id": "10"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def prize_detail(self, **kwargs):
        url = get_url(self.host, "prize_detail")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_prize(self, **kwargs):
        url = get_url(self.host, "add_prize")
        data_random_money = {"raffle_id": 10, "name": faker.sentence(), "type": 4,
                             "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "min_balance": "1",
                             "max_balance": "10",
                             "chance": "10",
                             "stock": "1000", "sort": "1", "status": 1}
        data_money = {"raffle_id": 10, "name": faker.sentence(), "type": 3,
                      "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "1",
                      "chance": "10",
                      "stock": "1000", "sort": "1", "status": 1}
        data_shiwu = {"raffle_id": 10, "name": faker.sentence(), "type": 1,
                      "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "1",
                      "chance": "10",
                      "stock": "1000", "sort": "1", "status": 1}
        data_integral = {"raffle_id": 10, "name": faker.sentence(), "type": 2,
                         "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "10",
                         "chance": "10",
                         "stock": "1000", "sort": "1", "status": 1}
        data_coupon = {"raffle_id": 10, "name": faker.sentence(), "type": 5,
                       "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "10",
                       "chance": "10",
                       "stock": "1000", "sort": "1", "status": 1}
        data_no = {"raffle_id": 10, "name": faker.sentence(), "type": 6,
                   "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "0",
                   "chance": "10",
                   "stock": "1000", "sort": "1", "status": 1}
        for key, value in kwargs.items():
            data_no[key] = value
        response = post(self.s, url, **data_no)
        return response

    def edit_prize(self, **kwargs):
        url = get_url(self.host, "edit_prize")
        data = {"id": -82080999.42848866, "name": "dolor dolor", "type": 34202134.73688136,
                "thumb": "sit dolore aute culpa amet", "chance": "officia Ut ullamco", "stock": "tempor ipsum",
                "sort": "adipisicing", "status": -76839408.78558473, "raffle_id": -73744563.4543993,
                "values": "cillum adipisicing", "min_balance": "Lorem dolore eu Ut tempor",
                "max_balance": "proident irure dolore"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def del_prize(self, **kwargs):
        url = get_url(self.host, "del_prize")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def record_list(self, **kwargs):
        url = get_url(self.host, "record_list")
        data = {"page": "1", "pageSize": "20", "raffle_id": "10"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def prize_express(self, **kwargs):
        url = get_url(self.host, "prize_express")
        data = {"id": "1", "express_name": "30", "express_num": "23"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_goods_shop(self, **kwargs):
        url = get_url(self.host, "add_goods")
        # delivery_type  配送方式（（1 同城配送 2到店自提 3快递发货））
        # stock_type. 仓库类型（仓库类型 1自营仓 2 云仓）
        data = {"action_type": 1, "stock_type": 1, "supplier_type": 0, "is_order_award_calc": 1, "is_break": 0,
                "delivery_type": [1, 2], "store_ids": [30997, 30996, 30995], "first_fee": 0, "cross_border": 2,
                "second_fee": "0", "combination": 0, "zu_num": 0, "video": "https://smjcdn.jzwp.cn/1643188625260.mp4",
                "stock_double": 1, "is_quick": 0, "is_top": 0,
                "is_welfare": 0, "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0,
                "store_extend": [], "start_type": 1, "end_type": 3, "cat_id": ["257", "262", "258"], "seckill_type": 1,
                "use_score": 1, "min_score": 5, "max_score": 10, "is_open_limit": 1, "single_max": 100,
                "limit_max": 100, "day_max": 100, "title": "超市-自营仓-弓" + str(get_max_goods_id())[5:], "subtitle": "商品特色",
                "goods_sn": "sn123123",
                "sort": "9999", "content": "<p>234</p>", "weight": "10", "volume_width": "410",
                "long_thumb": "https://smjcdn.jzwp.cn/1643184858440.jpg", "seckill_flag": 0, "is_coupon_convert": 0,
                "cat_id1": "257", "cat_id2": "262", "cat_id3": "258",
                "thumb": get_image(random.randint(1, 15)),
                "imgs": [get_image(random.randint(1, 15))], "stock_base": "10000", "type_id": 33, "type": 33,
                "attr_datas": [
                    {"sku_sn": "213123", "sku_id": 0, "goods_attr_ids": "1064,1056,1051", "stock": 0, "incr_stock": 0,
                     "stocks": [{"warehouse_id": "30997", "incr_stock": 100},
                                {"warehouse_id": "30996", "incr_stock": 100},
                                {"warehouse_id": "30995", "incr_stock": 100}], "market_price": "300",
                     "cost_price": "100", "shop_price": "200", "vip_price": "180", "partner_price": "null",
                     "team_price": "170", "bonus_second_vip": "null", "bonus_second_partner": "null",
                     "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                     "fee1": "null",
                     "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                     "fee7": "null",
                     "fee11": "null",
                     "fee12": "null", "fee13": "null"},
                    {"sku_sn": "213123", "sku_id": 0, "goods_attr_ids": "1064,1056,1052", "stock": 0, "incr_stock": 0,
                     "stocks": [{"warehouse_id": "30997", "incr_stock": 100},
                                {"warehouse_id": "30996", "incr_stock": 100},
                                {"warehouse_id": "30995", "incr_stock": 100}], "market_price": "300",
                     "cost_price": "100", "shop_price": "200", "vip_price": "180", "partner_price": "null",
                     "team_price": "170", "bonus_second_vip": "null", "bonus_second_partner": "null",
                     "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                     "fee1": "null",
                     "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                     "fee7": "null",
                     "fee11": "null",
                     "fee12": "null", "fee13": "null"}], "sku_imgs": {}, "params": [],
                "goods_id": get_max_goods_id(),
                "is_index": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def add_channel(self, **kwargs):
        url = get_url(self.host, "add_channel")
        data = {"name": "舒服的"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def warehouse_edit_stock(self, **kwargs):
        url = get_url(self.host, "warehouse_edit_stock")
        data = {"goods_id": "100005500", "warehouse_id": "30997",
                "sku_groups": [{"sku_id": "100004566", "incr_stock": "100"},
                               {"sku_id": "100004565", "incr_stock": "100"}], }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def content_list(self, **kwargs):
        url = get_url(self.host, "content_list")
        data = {"page": "1", "pageSize": "30"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data'])
        return response

    def content_detail(self, **kwargs):
        url = get_url(self.host, "content_detail")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_content(self, **kwargs):
        url = get_url(self.host, "add_content")
        data = {"author_id": "1", "content": "是独立房间看临时搭建开发拉跨",
                "images": ["https://mmtcdn.jzwp.cn/1623983004180.png", "https://mmtcdn.jzwp.cn/1623996530710.png"],
                "video": "", "supplier_type": "0", "goods_id": "100005501",
                "sort": "1", "virtual_like": "1000", "virtual_share": "1000", "status": "1", }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_content(self, **kwargs):
        url = get_url(self.host, "edit_content")
        data = {"id": "", "author_id": "", "content": "", "images": "", "video": "", "supplier_type": "",
                "goods_id": "100005501", "sort": "1", "virtual_like": "1000", "virtual_share": "1000", "status": "1", }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def set_content(self, **kwargs):
        url = get_url(self.host, "set_content")
        data = {"id": "1", "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def del_content(self, **kwargs):
        url = get_url(self.host, "del_content")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def author_list(self, **kwargs):
        url = get_url(self.host, "author_list")
        data = {"page": "1", "pageSize": "10"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data'])
        return response

    def add_author(self, **kwargs):
        url = get_url(self.host, "add_author")
        data = {"name": faker.name(),
                "head_picture": r"https://thirdwx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEKFMZ6K4rdxnGh3XEQAFYQKJlCV5Q2owBicWFaMaGTefO5UsjXfMruib2TgqbibPLyoXjJZ3wBlic47Ew/132",
                "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_author(self, **kwargs):
        url = get_url(self.host, "edit_author")
        data = {"id": "", "name": "1", "head_picture": "30", "status": "30"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def set_author(self, **kwargs):
        url = get_url(self.host, "set_author")
        data = {"id": "1", "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def del_author(self, **kwargs):
        url = get_url(self.host, "del_author")
        data = {"id": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def all_open_author(self, **kwargs):
        url = get_url(self.host, "all_open_author")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_score_goods(self, **kwargs):
        url = get_url(self.host, "add_score_goods")
        data = {"supplier_id": "30376", "cat_id1": 153, "title": "积分商品" + faker.sentence(),
                "action_type": "1", "goods_id": get_max_goods_id(), "attr_datas": [
                {"sku_id": 0, "stock": 0,
                 "goods_attr_ids": "256", "incr_stock": 100,
                 "market_price": "200", "cost_price": "190",
                 "sku_sn": "sku_sn000a", "ask_amount": 100,
                 "ask_score": 80}, {"sku_id": 0, "stock": 0,
                                    "goods_attr_ids": "1023",
                                    "incr_stock": 100, "market_price": "210",
                                    "cost_price": "180",
                                    "sku_sn": "sku_sn223",
                                    "ask_amount": 60,
                                    "ask_score": 60}],
                "params": [{"key": "刷个", "value": "撒旦发"},
                           {"key": "发撒旦", "value": "撒旦发"}],
                "supplier_type": 1, "cat_id2": 0, "cat_id3": 0,
                "goods_sn": "SN00000001", "subtitle": "in sed ut sunt consequat",
                "imgs": [get_image(1), get_image(2)],
                "long_thumb": get_image(3)}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def score_goods_list(self, **kwargs):
        url = get_url(self.host, "score_goods_list")
        data = {"page": "1", "pageSize": "20"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def attr_list(self, **kwargs):
        url = get_url(self.host, "attr_list")
        data = {"type": "1", "page": 1, "pageSize": 30}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_shop_account(self, **kwargs):
        url = get_url(self.host, "add_shop_account")
        data = {"shop_offline_id": random.choice(["31032", "31033", "31034"]), "name": faker.name(),
                "phone": faker.phone_number(), "password": "123456",
                "role": random.choice(["1", "2"])}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # senior场景值（1 新增 2 编辑修改）
    def add_offline_goods(self, **kwargs):
        url = get_url(self.host, "add_offline_goods")
        data = {"senior": "1", "goods_id": get_max_goods_id(), "title": "枪械体验射击馆" + str(get_max_goods_id())[5:],
                "subtitle": faker.sentence(), "cat_id1": "254", "cat_id2": "", "cat_id3": "",
                "supplier_type": "31018", "expiration_time_of_consumption": "89", "sort": 9999,
                "params": [{"key": "长度", "value": "170mm"}, {"key": "重量", "value": "500g"}],
                "is_store_refund": "", "select_type": "",
                "use_score": "", "store_extend": "", "goods_sn": "",
                "": "", "": "", "imgs": "", "store_ids": "", "attr_datas": "", "service_expire_type": "",
                }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def stock_log(self, **kwargs):
        url = get_url(self.host, "stock_log")
        data = {"page": 1, "pageSize": 30}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def set_config_gift_card(self, **kwargs):
        url = get_url(self.host, "set_config_gift_card")
        data = {"cover_imgs": ["https://smjcdn.jzwp.cn/1642642710005.jpg"],
                "face_values": [100, 200, 300, 400, 500, 1000]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def add_goods_yuncang(self, **kwargs):
        url = get_url(self.host, "add_goods")
        # delivery_type  配送方式（（1 同城配送 2到店自提 3快递发货））
        # stock_type. 仓库类型（仓库类型 1自营仓 2 云仓）
        data = {"action_type": 1, "stock_type": 2, "supplier_type": 0, "is_order_award_calc": 1, "is_break": 0,
                "delivery_type": [3], "store_ids": [], "freight_id": 545, "first_fee": 0, "cross_border": 2,
                "second_fee": "0", "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0,
                "is_welfare": 0, "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0,
                "store_extend": [], "start_type": 1, "end_type": 3, "cat_id": ["257", "263", "261"], "seckill_type": 1,
                "use_score": 1, "min_score": 0, "max_score": 0, "is_open_limit": 1, "single_max": 1, "limit_max": 1,
                "day_max": 1, "title": "云仓-箭" + str(get_max_goods_id())[5:], "subtitle": "特色test", "goods_sn": "sn342",
                "sort": "9999",
                "supplier_id": "30377", "content": "<p>地方锁粉撒旦发撒旦发撒旦发</p>", "weight": "12", "volume_width": "12",
                "freight_type": 3, "insurance_id": 180, "long_thumb": "https://smjcdn.jzwp.cn/1643190310677.jpg",
                "seckill_flag": 0, "is_coupon_convert": 0, "cat_id1": "257", "cat_id2": "263", "cat_id3": "261",
                "thumb": get_image(random.randint(1, 15)),
                "imgs": [get_image(random.randint(1, 15)), "https://smjcdn.jzwp.cn/1643190306757.jpg"],
                "stock_base": "1000", "type_id": 33, "type": 33, "attr_datas": [
                {"sku_sn": "1212", "sku_id": 0, "goods_attr_ids": "1062,1056,1051", "stock": 0, "incr_stock": "100",
                 "stocks": [{"warehouse_id": 0, "incr_stock": "100"}], "market_price": "300", "cost_price": "100",
                 "shop_price": "200", "vip_price": "180", "partner_price": "null", "team_price": "170",
                 "bonus_second_vip": "null", "bonus_second_partner": "null", "bonus_second_team": "10",
                 "storage_cost": "null", "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null",
                 "fee3": "null",
                 "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null", "fee12": "null",
                 "fee13": "null"},
                {"sku_sn": "1212", "sku_id": 0, "goods_attr_ids": "1062,1056,1052", "stock": 0, "incr_stock": "100",
                 "stocks": [{"warehouse_id": 0, "incr_stock": "100"}], "market_price": "300", "cost_price": "100",
                 "shop_price": "200", "vip_price": "180", "partner_price": "null", "team_price": "170",
                 "bonus_second_vip": "null", "bonus_second_partner": "null", "bonus_second_team": "10",
                 "storage_cost": "null", "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null",
                 "fee3": "null",
                 "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null", "fee12": "null",
                 "fee13": "null"}],
                "sku_imgs": {}, "params": [{"key": "1", "value": "2"}, {"key": "3", "value": "4"}],
                "goods_id": get_max_goods_id(), "is_index": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 服务门店
    def add_shop_offline_mendian(self, **kwargs):
        url = get_url(self.host, "add_shop_offline")
        data = {"type": 2, "name": faker.company() + str(random.randint(1, 10000)), "province_id": 510000, "city_id": 510100, "district_id": 510186,
                "address": "环球中心w2", "longitude": "104.060835", "latitude": "30.569896", "contact_phone": "13980883526",
                "business_at": "9:00~18:00", "status": 1, "shop_type": 1,
                "shop_imgs": ["https://smjcdn.jzwp.cn/1643249620351.jpg"], "pid": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    data_temp = {}
    for r in range(300):
        InterfaceModule(s).add_shop_account(**data_temp)
