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


class InterfaceModule(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_b"

    # 添加优惠券
    def add_coupon(self, **kwargs):
        url = get_url(self.host, "add_coupon")
        data = {"type": 0, "cat_id": "103", "ding_at": 1638892800, "goods_ids": "100000367,100000400,100000405",
                "day": 7, "name": "打了卡是否接了", "max": "50.00", "money": "10.00", "is_overlay": 0, "num": 67,
                "user_num": 10, "start_at": 1638892800,
                "end_at": 1640188800, "sort": 0, "delflag": 0,
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
        data = {"uid": 2, "type": 9, "money": 100, "remark": "加钱", "password": "110114"}
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
        data = {"coupon_id": 5274, "coupon_num": "10", "member_ids": "2"}
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
        data = {"title": "圣美家秒杀活动", "description": "圣美家秒杀",
                "start_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                "end_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 7200)),
                "shop_offline_id": "31000,31001",
                "goods": ["100005359", "100005360"]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加分类
    def add_goods_category(self, **kwargs):
        url = get_url(self.host, "add_goods_category")
        # type 1 线上商品  type 2 线下商品
        data = {"name": faker.name(), "delivery": "false", "display": 0, "sort": "100", "display_index": "1",
                "thumb": ["https://fncdn.jzwp.cn/1642147340710.jpg"], "status": "1",
                "imgs": ["https://fncdn.jzwp.cn/1642147417352.jpg"], "type": "1", "pid": "246"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加规格
    def add_attr(self, **kwargs):
        url = get_url(self.host, "add_attr")
        # type 1 线上商品  type 2 线下商品
        data = {"type": "1", "name": "今天感觉有点疲倦"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加规格
    def add_attr_item(self, **kwargs):
        url = get_url(self.host, "add_attr_item")
        # type 1 线上商品  type 2 线下商品
        data = {"name": "哈哈哈", "sort": "9",
                "values": [{"value": "1", "color": "", "id": ""}, {"value": "2", "color": "", "id": ""},
                           {"value": "3", "color": "", "id": ""}, {"value": "4", "color": "", "id": ""}],
                "attr_id": "250"}
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
        data = {"ids": "12312"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 拣货完成
    def order_picking_compelte(self, **kwargs):
        url = get_url(self.host, "order_picking_compelte")
        # deliver_type 1 自提  2 同城
        data = {"ids": "12312", "deliver_type": 1}
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
        data = {"title": "", "page": 1, "pageSize": 20, "type": "", "time_status": ""}
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


if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    data_temp = {}
    InterfaceModule(s).goods_list(**data_temp)
