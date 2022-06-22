# @time 2022/1/11 16:52
# @Author howell
# @File smjb.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from common.rideexcel import ExcelUtil as ExcelUtilT
from faker import Faker
import random
import time
import datetime

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report1.xls'))


class InterfaceModule(object):
    def __init__(self, request_session, host="host_smj_b"):
        self.s = request_session
        self.host = host

    # 添加优惠券
    def add_coupon(self, **kwargs):
        url = get_url(self.host, "add_coupon")
        data_xs_sp = {}
        for key, value in kwargs.items():
            data_xs_sp[key] = value
        response = post(self.s, url, **data_xs_sp)
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
        # 3 加款  4  扣钱
        data = {"uid": 100029, "type": 4, "money": 19.9, "remark": "测试自动加钱", "password": "110114"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 添加公告
    def add_notice(self, **kwargs):
        url = get_url(self.host, "add_notice")
        data = {"title": faker.sentence()[:-1], "is_enable": random.choice([1, 2]), "content": faker.sentence()[:-1],
                "type_relation": random.choice([1, 2, 3]),
                "shop_offline_ids": [31343, 31242, 31241, 31240, 31002, 31001],
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
                "type_relation": random.choice([1, 2, 3]),
                "shop_offline_ids": [31343, 31242, 31241, 31240, 31002, 31001],
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
        # 加款 9 扣款 22
        data = {"uid": 100029, "type": 22, "money": 35398.42, "remark": "加钱", "password": "110114"}
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
        # data = {"type": 1, "name": "圣美家" + str(random.randint(1, 10000)), "province_id": 540000, "city_id": 540100,
        #         "district_id": 540102,
        #         "address": "娘热北路70号", "longitude": "91.12354", "latitude": "29.6808", "contact_phone": "13980883526",
        #         "note": "圣美家欧耶", "template_id": "653", "business_at": "09:00-22:00", "status": 1}
        data = {"type": 1, "name": "吾悦广场-龙泉店" + str(random.randint(1, 10000)), "province_id": 510000,
                "city_id": 510100, "district_id": 510112,
                "address": "吾悦广场", "longitude": "104.240829", "latitude": "30.577833",
                "contact_phone": faker.phone_number(),
                "note": "自提描述" + faker.sentence(), "template_id": 705, "business_at": "8:00~22:00", "status": 1}
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
        # 加积分 1 扣积分 11
        data = {"uid": 100029, "type": 11, "point": 1815, "password": "123456", "remark": "备注备注"}
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
        data = {"coupon_id": 5315, "coupon_num": "10", "member_ids": "16"}
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
        data = {"title": "奥克斯秒杀" + faker.sentence(), "description": "圣美家秒杀",
                "start_time": get_now_time(60 * 60 * 1),
                "end_time": get_now_time(1 * 60 * 60),
                "shop_offline_id": "31343",
                "goods": [{"goods_id": "1000060213", "single_max": "1", "single_min": "1", "day_max": "1",
                           "limit_max": "10", "virtual_percentavirtual_scores": "0", "sort": "1",
                           "sku": [
                               {"sku_id": "100006729", "inventory_id": "18157", "kill_price": "9.9", "vip_price": "8.8",
                                "bonus_second_vip": "1", "stock": "100", "status": "0"},
                               {"sku_id": "100006730", "inventory_id": "18158", "kill_price": "9.9", "vip_price": "8.8",
                                "bonus_second_vip": "1", "stock": "100", "status": "0"}]}], }
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
                "imgs": ["https://fncdn.jzwp.cn/1642147417352.jpg"], "type": "1"}

        data1 = {"pid": 433, "type": 1, "pname": "一级", "name": faker.name_male(), "sort": "12", "display": 1,
                 "thumb": get_images(1), "imgs": []}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data1)
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
        data = {"items": [{"id": 20244, "code": "YTO", "sn": "123456789"}]}
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
        data = {"type": "-1", "page": 1, "pageSize": 80}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        # ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
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
        data = {"page": 1, "pageSize": 900}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 仓库详情
    def warehouse_detail(self, **kwargs):
        url = get_url(self.host, "warehouse_detail")
        data = {'goods_id': 1000063179, 'warehouse_id': 31503}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 编辑库存
    def edit_stock(self, **kwargs):
        url = get_url(self.host, "edit_stock")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
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
        data = {"title": faker.sentence(), "description": faker.sentence(), "start_time": get_now_time(),
                "end_time": get_now_time(721200), "shop_offline_id": 31475,
                "rules": {"type": random.choice([2]), "full": 1, "full_reduce": 0.01},
                "goods": ["1000062028", "1000062027", "1000062026"]}
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
        data = {"id": 10, "need_integrate": 10, "free_num": 1000,
                "max_num": 2000}
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
        data = {"id": 137, "title": faker.sentence(), "type": "1", "thumb": "https://smjcdn.jzwp.cn/1646994566197.png",
                "back_color": "#A30E10", "description": faker.sentence(), "start_time": get_now_time(),
                "end_time": get_now_time(3600 * 24 * 10), "status": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_raffle(self, **kwargs):
        url = get_url(self.host, "edit_raffle")
        data = {"id": 137, "title": faker.sentence(), "type": "1", "thumb": "https://cxtcdn.jzwp.cn/1627439302135.png",
                "back_color": "#A30E10", "description": faker.sentence(), "start_time": get_now_time(),
                "end_time": get_now_time(3600 * 12 * 2), "status": "1"}
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
        data = {"page": "1", "pageSize": "30", "raffle_id": "120"}
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
        data_random_money = {"raffle_id": 105, "name": faker.sentence(), "type": 4,
                             "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "min_balance": "1",
                             "max_balance": "10",
                             "chance": "10",
                             "stock": "1000", "sort": "1", "status": 1}
        data_money = {"raffle_id": 105, "name": faker.sentence(), "type": 3,
                      "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "1",
                      "chance": "10",
                      "stock": "1000", "sort": "1", "status": 1}
        data_shiwu = {"raffle_id": 105, "name": faker.sentence(), "type": 1,
                      "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "1",
                      "chance": "100",
                      "stock": "1000", "sort": "1", "status": 1}
        data_integral = {"raffle_id": 105, "name": faker.sentence(), "type": 2,
                         "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "10",
                         "chance": "10",
                         "stock": "1000", "sort": "1", "status": 1}
        data_coupon = {"raffle_id": 105, "name": faker.sentence(), "type": 5,
                       "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "10",
                       "chance": "10",
                       "stock": "1000", "sort": "1", "status": 1}
        data_no = {"raffle_id": 105, "name": faker.sentence(), "type": 6,
                   "thumb": "https://llycdn.jzwp.cn/1617014556171.jpg", "values": "0",
                   "chance": "10",
                   "stock": "1000", "sort": "1", "status": 1}
        for key, value in kwargs.items():
            data_shiwu[key] = value
        response = post(self.s, url, **data_shiwu)
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
        data = {"page": "1", "pageSize": "9999", "raffle_id": "120"}
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
        # data = {"author_id": random.randint(2371, 2391), "content": faker.text(max_nb_chars=4000),
        #         "images": get_images(9),
        #         "video": "", "supplier_type": "0", "goods_id": "1000060494",
        #         "sort": random.randint(1, 100), "virtual_like": "1000", "virtual_share": "1000", "status": "1", }
        data = {"supplier_type": 0, "author_id": random.randint(2371, 2391), "content": faker.text(max_nb_chars=1000),
                "images": get_images(random.randint(1, 9)), "goods_id": 1000062115, "sort": 17, "video": get_video(),
                "virtual_like": 9999, "virtual_share": 9999, "status": 1, "title": faker.text(max_nb_chars=30)}
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
                "head_picture": get_image(random.randint(1, 15)),
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

    # 添加积分商品
    def add_score_goods(self, **kwargs):
        # supplier_type 2     sku加下面的属性  "ask_score": "200", "ask_amount": "100.01"
        url = get_url(self.host, "add_goods")
        data = {"action_type": 1, "stock_type": 2, "supplier_type": 2, "is_order_award_calc": 1, "is_break": 0,
                "deliver_type": [3], "store_ids": [], "first_fee": 0, "cross_border": 1, "second_fee": "0",
                "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0,
                "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_extend": [],
                "start_type": 1, "end_type": 3, "cat_id": [434], "seckill_type": 1, "use_score": 0, "min_score": 0,
                "max_score": 0, "is_open_limit": 0, "single_max": 0, "limit_max": 0, "day_max": 0,
                "title": "积分商品-卫生纸" + faker.sentence(),
                "supplier_id": 30383, "sort": "1", "content": "<p>付水电费舒服</p>", "freight_type": 1,
                "long_thumb": get_image(random.randint(1, 15)), "seckill_flag": 0, "is_coupon_convert": 0,
                "cat_id1": 434, "cat_id2": 0, "cat_id3": 0, "thumb": get_image(random.randint(1, 15)),
                "imgs": get_images(random.randint(1, 4)), "type_id": 185, "type": 185, "attr_datas": [
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "11134,11127", "stock": 0, "incr_stock": "1",
                 "stocks": [{"warehouse_id": 0, "incr_stock": "1"}], "market_price": "300", "cost_price": "100",
                 "shop_price": "200", "vip_price": "190", "partner_price": "null", "team_price": "180",
                 "bonus_second_vip": "null", "bonus_second_partner": "null", "bonus_second_team": "5",
                 "storage_cost": "null", "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null",
                 "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                 "fee12": "null", "fee13": "null", "ask_score": "200", "ask_amount": "100.01"},
            ], "sku_imgs": {}, "params": [], "goods_id": get_max_goods_id(),
                "is_index": 0, "ask_score": "200", "ask_amount": "100.01"}
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
        data = {"shop_offline_id": random.choice(["31347", "31341", "31340"]), "name": faker.name(),
                "phone": faker.phone_number(), "password": "123456",
                "role": random.choice(["1", "2"])}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # senior场景值（1 新增 2 编辑修改）
    def add_goods_fuwu(self, **kwargs):
        url = get_url(self.host, "add_offline_goods")
        #  [31347, 31364],[31347],
        # 消费有效期 expiration_time_of_consumption=2022-02-28 00:00:00~2022-02-28 23:00:00 service_expire_type=1
        params = []
        for i in range(5):
            p_dic = dict()
            p_dic["key"] = faker.sentence()
            p_dic["value"] = faker.sentence()
            params.append(p_dic)
        data = {"action_type": 1, "supplier_type": 1, "stock_type": 1, "is_break": 1, "first_fee": 0, "cross_border": 2,
                "service_expire_type": 1,
                "expiration_time_of_consumption": str(get_now_time()) + "~" + str(get_now_time(10000)),
                "second_fee": "0",
                "combination": 0,
                "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0, "team_strategy1": 0,
                "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_ids": [31347, 31364],
                "store_extend": ["username"], "start_type": 1, "end_type": 3, "cat_id": [254, 270], "seckill_type": 1,
                "use_score": 1, "min_score": 0, "max_score": 1000, "is_store_refund": 0, "goods_sn": "服务货号",
                "select_type": 2, "master_shop_id": 31347, "title": "服务三-howell-" + faker.sentence(),
                "subtitle": "服务test",
                "sort": "9999",
                "content": "<p>舒服</p>", "long_thumb": get_image(random.randint(1, 15)), "seckill_flag": 0,
                "is_coupon_convert": 0, "cat_id1": 254, "cat_id2": 270, "cat_id3": 0,
                "thumb": get_image(random.randint(1, 15)),
                "imgs": get_images(4),
                "video": get_video(), "stock_base": "1000", "type_id": 32, "type": 32,
                "attr_datas": [{"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1097,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1097,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1098,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1098,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1099,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1100,1099,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1097,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1097,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1098,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1098,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1099,1093", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"},
                               {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1101,1099,1094", "stock": 0,
                                "incr_stock": "1000", "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}],
                                "market_price": "300", "cost_price": "100", "shop_price": "200", "vip_price": "190",
                                "partner_price": "null", "team_price": "180", "bonus_second_vip": "null",
                                "bonus_second_partner": "null", "bonus_second_team": "10", "storage_cost": "null",
                                "clear_price": "null", "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null",
                                "fee4": "null", "fee5": "null", "fee6": "null", "fee7": "null", "fee11": "null",
                                "fee12": "null", "fee13": "null"}], "sku_imgs": {},
                "params": params, "goods_id": get_max_goods_id()}
        data1 = {"action_type": 1, "supplier_type": 1, "stock_type": 1, "is_break": 0, "first_fee": 0,
                 "cross_border": 2, "service_expire_type": 2, "expiration_time_of_consumption": "20", "second_fee": "0",
                 "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0,
                 "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_ids": [],
                 "store_extend": [], "start_type": 1, "end_type": 3, "cat_id": [457], "seckill_type": 1, "use_score": 0,
                 "min_score": 0, "max_score": 0, "select_type": 1, "master_shop_id": 31480,
                 "title": "【服务】-【三】" + faker.sentence(),
                 "subtitle": "服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色服务特色", "sort": "9999",
                 "content": "<p><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674662.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674664.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674666.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674667.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674669.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674670.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674672.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674673.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674674.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674676.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674677.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650960674678.jpg\" /></p>",
                 "long_thumb": get_image(random.randint(1, 15)), "seckill_flag": 0, "is_coupon_convert": 0,
                 "cat_id1": 457, "cat_id2": 0, "cat_id3": 0, "thumb": "https://smjcdn.jzwp.cn/1650960644468.jpg",
                 "imgs": get_images(random.randint(2, 5)),
                 "video": get_video(), "type_id": 188, "type": 188, "attr_datas": [
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11167", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11168", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11169", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11170", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11171", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "howell", "sku_id": 0, "goods_attr_ids": "11172", "stock": 0, "incr_stock": "1000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "1000"}], "market_price": "600",
                 "cost_price": "", "shop_price": "499.99", "vip_price": "399.99", "partner_price": "null",
                 "team_price": "299.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"}], "sku_imgs": {}, "main_attr_id": 0,
                 "params": params, "goods_id": get_max_goods_id()}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data1)
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
        params = []
        for i in range(5):
            p_dic = dict()
            p_dic["key"] = faker.sentence()
            p_dic["value"] = faker.sentence()
            params.append(p_dic)
        # delivery_type  配送方式（（1 同城配送 2到店自提 3快递发货））
        # stock_type. 仓库类型（仓库类型 1自营仓 2 云仓）
        data = {"action_type": 1, "stock_type": 2, "supplier_type": 0, "is_order_award_calc": 1, "is_break": 0,
                "deliver_type": [3], "store_ids": [], "first_fee": 0, "cross_border": 2, "second_fee": "0",
                "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0,
                "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_extend": [],
                "start_type": 1, "end_type": 3, "cat_id": [437], "seckill_type": 1, "use_score": 0, "min_score": 0,
                "max_score": 0, "is_open_limit": 0, "single_max": 0, "single_min": 0, "limit_max": 0, "day_max": 0,
                "title": "【云仓商品】-【第二轮】-" + faker.sentence(), "sort": "9990", "supplier_id": 30388,
                "content": "<p><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323968.jpeg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323970.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323971.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323973.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323974.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323976.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323977.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323978.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323979.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323981.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323982.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323983.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323985.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323986.jpg\" /><img class=\"wscnph\" src=\"https://smjcdn.jzwp.cn/1650945323987.jpg\" /></p>",
                "weight": "5", "volume_width": "5", "freight_type": 2, "freight_fee": "5", "insurance_id": 207,
                "seckill_flag": 0, "is_coupon_convert": 0, "cat_id1": 437, "cat_id2": 0, "cat_id3": 0,
                "thumb": get_image(random.randint(1, 15)),
                "imgs": get_images(4),
                "video": get_video(), "type_id": 186, "type": 186, "attr_datas": [
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11149,11146", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11149,11147", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11150,11146", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11150,11147", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11151,11146", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "S1", "sku_id": 0, "goods_attr_ids": "11153,11151,11147", "stock": 0, "incr_stock": "10000",
                 "weight": 0, "stocks": [{"warehouse_id": 0, "incr_stock": "10000"}], "market_price": "500",
                 "cost_price": "200", "shop_price": "400.99", "vip_price": "380.99", "partner_price": "null",
                 "team_price": "360.99", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "10", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"}],
                "sku_imgs": {"11149": {"thumb": ["https://smjcdn.jzwp.cn/1650945287229.jpg"]},
                             "11150": {"thumb": ["https://smjcdn.jzwp.cn/1650945289443.jpg"]},
                             "11151": {"thumb": ["https://smjcdn.jzwp.cn/1650945291292.jpg"]}}, "main_attr_id": 88,
                "params": params, "goods_id": get_max_goods_id(), "is_index": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 服务门店
    def add_shop_offline_mendian(self, **kwargs):
        url = get_url(self.host, "add_shop_offline")
        data = {"type": 2, "name": faker.company() + str(random.randint(1, 10000)), "province_id": 510000,
                "city_id": 510100, "district_id": 510186,
                "address": "环球中心w2", "longitude": "104.060835", "latitude": "30.569896", "contact_phone": "13980883526",
                "business_at": "9:00~18:00", "status": 1, "shop_type": 2,
                "shop_imgs": ["https://smjcdn.jzwp.cn/1643249620351.jpg"], "pid": "31480"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 服务门店
    def add_attr_fuwu(self, **kwargs):
        url = get_url(self.host, "add_attr")
        data = {"type": 2, "name": faker.job()}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 线下订单列表
    def offline_list(self, **kwargs):
        url = get_url(self.host, "offline_list")
        data = {"status": -1}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 订单核销
    def order_use(self, **kwargs):
        url = get_url(self.host, "order_use")
        data = {"goods_code_id": 116374, "shop_id": 30883}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 入驻审核
    def store_apply(self, **kwargs):
        url = get_url(self.host, "store_apply")
        data = {"id": 78, "status": 2, "remark": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 修改用户类型
    def change_user_type(self, **kwargs):
        url = get_url(self.host, "change_user_type")
        data = {"type": 1, "id": 19}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 修改同城运费模板
    def add_city_wide(self, **kwargs):
        url = get_url(self.host, "add_city_wide")
        data = {"name": "A奥克斯广场-永辉超市 同城配送模板", "distance": 10, "start_time_slot": "08:00:00",
                "end_time_slot": "08:00:00", "distribution": "30", "interval": "30",
                "distance_config": {"overweight": 1.5, "base_weight": 1.5, "base_freight": 1.5, "base_distance": 1.5,
                                    "over_distance": 1.5, "overweight_freight": 1.5, "over_distance_freight": 1.5},
                "status": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意售后
    def order_sale(self, **kwargs):
        url = get_url(self.host, "order_sale")
        data = {"add_fee": "0.00", "is_quality": "0", "deduct_freight_fee": "0.00", "freight_type": "0",
                "remark": "上得分是的发", "freight_fee": 0, "is_rebate": "1", "goods_fee": 9.5, "compensate": "0.00",
                "receiver_address": "上得分上得分", "sale_id": "111", "type": "1",
                "return_sku_list": [{"sku_id": "24447", "count": 1}]}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意售后
    def order_sale_detail(self, **kwargs):
        url = get_url(self.host, "order_sale_detail")
        data = {"id": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 编辑售后单的物流信息
    def edit_sale_order(self, **kwargs):
        url = get_url(self.host, "edit_sale_order")
        data = {"logistics_code": "YTO", "logistics_sn": "123456", "sale_id": "109"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 确认收货
    def order_take(self, **kwargs):
        url = get_url(self.host, "order_take")
        data = {"sale_id": "109"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意退款
    def agree_refund_money(self, **kwargs):
        url = get_url(self.host, "agree_refund_money")
        data = {"sale_id": "109"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意退款
    def edit_user_info(self, **kwargs):
        url = get_url(self.host, "edit_user_info")
        data = {"sex": 0, "phone": "18512816627", "nickname": "小米CS", "id": 100013}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意退款
    def add_rider(self, **kwargs):
        url = get_url(self.host, "add_rider")
        # 540100 510100
        data = {"username": faker.name(), "phone": faker.phone_number(), "city_id": "510100",
                "avatar": get_image(random.randint(1, 15))}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 同意售后
    def order_clearing(self, **kwargs):
        url = get_url(self.host, "order_clearing")
        data = {"pageSize": 10, "page": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 关闭售后
    def order_deny(self, **kwargs):
        url = get_url(self.host, "order_deny")
        data = {"sale_id": 211, "is_quality": "0", "remark": faker.sentence()}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 售后列表
    def sales_list(self, **kwargs):
        url = get_url(self.host, "sales_list")
        # status 1 status 10
        data = {"pageSize": 999, "page": 1, "status": 10}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 售后列表
    def refund_list(self, **kwargs):
        url = get_url(self.host, "refund_list")
        # status 1 status 10
        data = {"pageSize": 999, "page": 1, "status": 20}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 售后列表
    def set_refund_money(self, **kwargs):
        url = get_url(self.host, "set_refund_money")
        # status 1 status 10
        data = {"sale_id": 3659}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 售后发货
    def order_send(self, **kwargs):
        url = get_url(self.host, "order_send")
        data = {"sale_id": 234, "logistics_sn": "YT6345970536613", "logistics_code": "YTO",
                "remark": faker.sentence()}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 获取服务发货的门店
    def get_shop_ids(self, **kwargs):
        url = get_url(self.host, "get_shop_ids")
        # status 1 status 10
        data = {"goods_id": 1000063143}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 删除分享人
    def del_upper(self, **kwargs):
        url = get_url(self.host, "del_upper")
        data = {"id": 100073}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 修改分享人
    def update_upper(self, **kwargs):
        url = get_url(self.host, "update_upper")
        data = {"id": "10001488", "store_id": "10001487"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def add_attr_item_add_value(self, **kwargs):
        url = get_url(self.host, "add_attr_item_add_value")
        data = {"value": "123", "sort": "10", "is_main": 0, "attr_item_id": 87, "attr_id": 186, "goods_id": 1000063841}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def add_goods_shop(self, **kwargs):
        url = get_url(self.host, "add_goods")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def add_goods_shop_a(self, **kwargs):
        url = get_url(self.host, "add_goods")
        data = {"action_type": 1, "stock_type": 1, "supplier_type": 0, "is_order_award_calc": 1, "is_break": 0,
                "deliver_type": [1, 2], "store_ids": [31484], "first_fee": 0, "cross_border": 2, "second_fee": "0",
                "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0,
                "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_extend": [],
                "start_type": 1, "end_type": 3, "cat_id": [435], "seckill_type": 1, "use_score": 0, "min_score": 0,
                "max_score": 0, "is_open_limit": 0, "single_max": 0, "single_min": 0, "limit_max": 0, "day_max": 0,
                "title": "商品名称", "sort": "9990", "content": "<p>sasd as d</p>", "seckill_flag": 0,
                "is_coupon_convert": 0, "cat_id1": 435, "cat_id2": 0, "cat_id3": 0,
                "thumb": get_image(random.randint(1, 15)),
                "imgs": get_images(random.randint(0, 4)), "type_id": 186, "type": 186, "attr_datas": [
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11153,11149,11146", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11153,11149,11147", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11153,11150,11146", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11153,11150,11147", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11154,11149,11146", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11154,11149,11147", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11154,11150,11146", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"},
                {"sku_sn": "s1", "sku_id": 0, "goods_attr_ids": "11154,11150,11147", "stock": 0, "incr_stock": 0,
                 "weight": "5", "stocks": [{"warehouse_id": 31484, "incr_stock": 100}], "market_price": "300",
                 "cost_price": "100", "shop_price": "200", "vip_price": "190", "partner_price": "null",
                 "team_price": "180", "bonus_second_vip": "null", "bonus_second_partner": "null",
                 "bonus_second_team": "5", "storage_cost": "null", "clear_price": "null", "price2": "null",
                 "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null", "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"}],
                "sku_imgs": {"11149": {"thumb": get_images(1)},
                             "11150": {"thumb": get_images(1)}}, "main_attr_id": 88,
                "params": [], "goods_id": get_max_goods_id(), "is_index": 0}
        for key, value in kwargs.items():
            data[key] = value
        post(self.s, url, **data)

    # 获取服务发货的门店
    def get_goods_list(self, **kwargs):
        url = get_url(self.host, "get_goods_list")
        # status 1 status 10
        data = {"key": "up", "pageSize": 20, "page": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 获取服务发货的门店
    def goods_detail_sp(self, **kwargs):
        url = get_url(self.host, "goods_detail_sp")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 同城配送订单列表
    def city_order_list(self, **kwargs):
        url = get_url(self.host, "city_order_list")
        # status 1 status 10
        data = {"use_status": "0", "pageSize": 999, "page": 1, "shop_id": "31475", "deliver_type": 3}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 同城配送订单列表
    def pick_order_list(self, **kwargs):
        url = get_url(self.host, "pick_order_list")
        # status 1 status 10
        data = {"use_status": "0", "pageSize": 999, "page": 1, "shop_id": "31475", "deliver_type": 3}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 关闭订单
    def close_order(self, **kwargs):
        url = get_url(self.host, "close_order")
        # status 1 status 10
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 下架商品
    def down_good(self, **kwargs):
        url = get_url(self.host, "down_good")
        # status 1 status 10
        data = {"goodsIds": [483], "status": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


def set_goods_sort(self, **kwargs):
    url = get_url(self.host, "set_goods_sort")
    data = {"id": 475, "sort": "372"}
    for key, value in kwargs.items():
        data[key] = value
    response = post(self.s, url, **data)
    return response


def change_goods_sort(self):
    s = Login().login_b("host_smj_zsb", "admin_login")
    data_temp = {}
    # for i in range(1):
    #     InterfaceModule(s).add_shop_offline(**data_temp)
    # InterfaceModule(s).add_author(**data_temp)
    # InterfaceModule(s).add_goods_fuwu(**data_temp)
    # InterfaceModule(s).add_goods_shop(**data_temp)
    ab_lj = InterfaceModule(s)
    goods_temp = ab_lj.get_goods_list(**data_temp)["data"]["list"]['items']
    id_s = []
    for i in goods_temp:
        id_s.append(i['id'])
    id_sort_s = sorted(id_s, reverse=True)
    count = 1
    for id in id_sort_s:
        data = {"id": id, "sort": count}
        ab_lj.set_goods_sort(**data)
        count += 1


if __name__ == '__main__':
    s = Login().login_b("host_smj_b", "admin_login")
    worker = InterfaceModule(s)
    data = {"title": "【服务】-6月10日-测试流程" + faker.sentence()}
    worker.add_goods_fuwu(**data)
