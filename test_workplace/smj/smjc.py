# @time 2022/1/11 16:53
# @Author howell
# @File smjc.PY
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_c_report.xls'))


class InterfaceModuleApi(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_c"

    # 添加用户地址
    def add_address(self, **kwargs):
        url = get_url(self.host, "add_address")
        full_address = "西藏自治区拉萨市城关区曲米路公园"
        full_address_a = "四川省成都市武侯区天府大道北段1700号"
        map_a = get_map(full_address_a)
        longitude = map_a['result']['location']['lng']
        latitude = map_a['result']['location']['lat']
        data = {"id": "", "name": faker.name(), "phone": faker.phone_number(), "address": "曲米路公园", "id_card_name": "",
                "id_card": "",
                "is_default": 1, "province": "西藏自治区", "province_id": 540000, "city": "拉萨市", "city_id": 540100,
                "district": "城关区", "district_id": 540102, "full_address": full_address, "appName": "圣美家",
                "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                "deviceModel": "microsoft", "longitude": longitude, "latitude": latitude, }
        data1 = {"id": "", "name": faker.name(), "phone": faker.phone_number(), "address": "环球中心-n5",
                 "id_card_name": "",
                 "id_card": "", "is_default": 1, "province": "四川省", "province_id": 510000, "city": "成都市",
                 "city_id": 510100, "district": "高新区", "district_id": 510107, "full_address": full_address_a,
                 "appName": "嘛嘛团", "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64",
                 "deviceId": "mini app", "deviceModel": "microsoft", "longitude": "104.061304",
                 "latitude": "30.570965", }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data1)
        return response

    # 下单
    def submmit_order(self, **kwargs):
        url = get_url(self.host, "submmit_order")
        data = {"type": 1, "bargain_id": 0, "buy_insurance": 0, "join_store": 0, "goods_id": "100005500",
                "sku_id": "100004566", "nums": 1, "couponNeedNum": 1, "cart_ids": "",
                "address_ids": "122",
                "coupon_id": "", "extend": {"100005500": {"buy_insurance": 0, "buyer_message": ""}},
                "scene": "null", "source": "null", "shopId": "31002", "deliver_type": "1"}
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

    # 提交订单-服务
    def order_offline_submit(self, **kwargs):
        url = get_url(self.host, "order_offline_submit")
        data = {"shopId": 30365, "sku_id": 100004584, "latitude": "0", "longitude": "0", "num": 1, "address_id": 0,
                "deliver_type": 2, "integral_fee": 3, "gift_fee": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 选择支付方式
    def choice_pay_type(self, **kwargs):
        url = get_url(self.host, "choice_pay_type")
        data = {"id": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 确认收货
    def confirm_receipt(self, **kwargs):
        url = get_url(self.host, "confirm_receipt")
        data = {"id": 0, "appName": "圣美家", "appVersion": "v1.0.0", "systemType": "mp",
                "systemVersion": "Windows 10 x64", "deviceId": "mini app", "deviceModel": "microsoft",
                "shopId": "0"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 发布评价
    def add_evaluate(self, **kwargs):
        url = get_url(self.host, "add_evaluate")
        data = {"order_id": 0, "avatar": 0, "nickname": 0, "goods_id": 0, "score": 5, "imgs": [""],
                "content": "这个是评价内容", "video": [0], "order_extend_id": 0}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 获取评价列表
    def evaluate_list(self, **kwargs):
        url = get_url(self.host, "evaluate_list")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 查询售后原因
    def order_reason(self, **kwargs):
        url = get_url(self.host, "order_reason")
        data = {"type": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 申请售后 # 5 是补偿  6是补发
    def order_sales(self, **kwargs):
        url = get_url(self.host, "order_sales")
        p_reason = self.order_reason()
        reason = p_reason['data'][random.randrange(0, len(p_reason['data']))]['content']
        data = {"sale_type": 6, "sale_type_desc": "补偿", "reason": reason, "description": "撒旦发",
                "imagesArr": get_images(3), "order_id": 0,
                "return_sku_list": [{"sku_id": 0, "count": 1}],
                "imgs": get_images(3), "appName": "圣美家", "appVersion": "v1.0.0",
                "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                "deviceModel": "microsoft", "shopId": "1"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 加入购物车
    def join_cart(self, **kwargs):
        url = get_url(self.host, "join_cart")
        data = {"shopId": "31343", "cart_id": 0, "sku_id": 1, "num": 1}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 购物车列表
    def cart_list(self, **kwargs):
        url = get_url(self.host, "cart_list")
        data = {"shopId": "31343"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        # items_data = response['data']['cloud']['common']['items']
        # for i in items_data:
        #     temp = []
        #     temp.append(i)
        #     ExcelUtil(excel_filepath).write_response_data(temp)
        #     ExcelUtil(excel_filepath).write_response_data(i['sku'])
        return response

    # 移除购物车
    def remove_cart(self, **kwargs):
        url = get_url(self.host, "remove_cart")
        data = {"shopId": "31343", "cart_id": 173}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 礼品卡信息
    def gift_card_information(self, **kwargs):
        url = get_url(self.host, "gift_card_information")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 礼品卡信息
    def confirm_gift(self, **kwargs):
        url = get_url(self.host, "confirm_gift")
        data = {"money": "300", "cover_img": "https://smjcdn.jzwp.cn/1644395268194.jpg"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 我的礼品卡
    def member_gift_card(self, **kwargs):
        url = get_url(self.host, "member_gift_card")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 绑定用户
    def member_gift_card_bind(self, **kwargs):
        url = get_url(self.host, "member_gift_card_bind")
        data = {"code": "7885919480453083", "password": "449566209333"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 抽奖
    def raffle_luck(self, **kwargs):
        url = get_url(self.host, "raffle_luck")
        data = {"id": "105"}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        return response

    # 抽奖记录
    def luck_record(self, **kwargs):
        url = get_url(self.host, "luck_record")
        data = {"id": "125", "page": "1", "pageSize": 99999}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    # 领奖或修改地址
    def get_prize(self, **kwargs):
        url = get_url(self.host, "get_prize")
        data = {"id": "116", "name": faker.name(), "phone": faker.phone_number(), "full_address": faker.address()}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 取消订单
    def cancel_order(self, **kwargs):
        url = get_url(self.host, "cancel_order")
        data = {"id": "116"}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    # 团长入驻申请
    def apply_team(self, **kwargs):
        url = get_url(self.host, "apply_team")
        data = {"group_thumb": get_image(random.randint(1, 15))}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


if __name__ == '__main__':
    s = Login().login_c(19)
    data_temp = {}
    # for i in ['173', '172', '171', '170', '161']:
    #     data_temp = {"shopId": "31343", "cart_id": i}
    #     InterfaceModuleApi(s).remove_cart(**data_temp)
    # for i in range(2):
    InterfaceModuleApi(s).apply_team(**data_temp)
