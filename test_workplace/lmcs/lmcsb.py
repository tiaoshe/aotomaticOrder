# @time 2021/9/28 17:39
# @Author howell
# @File lmcsb.PY

from test_workplace.lmcs.lmcs_utils import CommonRequest
from common.controlexcel import ExcelUtil
import os
from faker import Faker


class InterfaceWorkerB(object):
    def __init__(self):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))
        self.count = 1
        self.worker = CommonRequest("B")
        self.faker = Faker(locale='zh_CN')

    # 获取用户列表数据
    def get_user_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"page": 1, "pageSize": 5, "type": -1}
        p = self.worker.get("member_list", **temp_data)
        items = p.json()['data']['items']
        userid_list = []
        for user in items:
            userid_list.append(user['id'])
        print(userid_list)

        items.append(p.json()['data']['fields'])
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 佣金设置
    def set_commission(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"contribution_proportion": 10, "base_commission_proportion": 60,
                         "overflow_commission_proportion": 20}
        p = self.worker.post("set_commission", **temp_data)
        return p

    # 获取配置
    def get_config(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "commission_config"}
        p = self.worker.get("get_config", **temp_data)
        return p

    # 渠道管理
    def add_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"name": "淘宝电商"}
        p = self.worker.post("add_channel", **temp_data)
        return p

    # 编辑渠道
    def edit_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 1, "name": "淘宝电商1"}
            p = self.worker.post("add_channel", **temp_data)
            return p

    # 获取渠道列表
    def get_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"page": 1, "pageSize": "10"}
            p = self.worker.get("get_channel", **temp_data)
            items = p.json()['data']['items']
            items.append(p.json()['data']['fields'])
            ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
            return p

    # 删除渠道
    def delete_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"ids": "4,5,6"}
            p = self.worker.post("delete_channel", **temp_data)
            return p

    # 编辑用户
    def edit_member(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "nickname": "", "phone": "13980883526", "sex": "1",
                         "birthday": "2000-01-01"}
        p = self.worker.post("edit_member", **temp_data)
        return p

    # 删除分享人
    def delete_referrer(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431}
        p = self.worker.post("delete_referrer", **temp_data)
        return p

    # 编辑分享人
    def change_store(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "store_id": 10001431}
        p = self.worker.post("change_store", **temp_data)
        return p

    # 编辑所属门店
    def change_shop(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "shop_id": 1}
        p = self.worker.post("change_shop", **temp_data)
        return p

    # 获取用户详情
    def member_info(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"uid": "10001537"}
        p = self.worker.get("member_info", **temp_data)
        return p

    # 获取品牌贡献列表
    def integral_record(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"shop_id": "-1", "uid": "", "keywords": "", "phone": "",
                         "first_uid": "", "start_time": "", "end_time": "", "page": "1",
                         "pageSize": "10"}
        p = self.worker.get("integral_record", **temp_data)
        return p

    # 获取品牌贡献列表
    def integral_record_export(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"shop_id": "-1", "uid": "10001537", "keywords": "", "phone": "",
                         "first_uid": "", "start_time": "", "end_time": "", "page": "1",
                         "pageSize": "10"}
        p = self.worker.get_download("integral_record_export", "test.xls", **temp_data)
        return p

    # 获取商品列表
    def goods_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"key": "up", "page": "1", "pageSize": "79"}
        p = self.worker.get("goods_list", **temp_data)
        items = p.json()['data']['list']['items']
        good_ids = []
        for item in items:
            good_ids.append(item['id'])
        print(good_ids)
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 添加商品
    def add_goods(self, **kwargs):
        if kwargs:
            temp_data = kwargs
            good_id = kwargs["goods_id"] + self.count
            kwargs["goods_id"] = good_id
            kwargs["title"] = self.faker.sentence() + str(self.count) + "||" + str(good_id)
            self.count += 1
        else:
            title = self.faker.sentence()
            temp_data = {"is_break": 1, "title": title, "subtitle": "水电费", "weight": "10", "volume_width": "10",
                         "sort": "9999", "supplier_id": 30357, "is_receive_way_logistics": 1,
                         "content": "多舒多舒服舒服",
                         "cross_border": 2, "team_angel1": 0, "team_angel2": 0, "brand_id": 20, "start_type": 1,
                         "end_type": 3, "cat_id": ["325", "326"],
                         "buy_notice": "舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费舒服水电费", "shop_type": 0,
                         "activity_svip": 0, "activity_star": 0, "shop_value": [],
                         "long_thumb": "https://lmcscdn.jzwp.cn/1640325766328.jpg", "is_coupon_convert": 0,
                         "cat_id1": "325", "cat_id2": "326", "cat_id3": 0,
                         "thumb": "https://lmcscdn.jzwp.cn/1640325740725.jpg",
                         "imgs": ["https://lmcscdn.jzwp.cn/1640325743206.jpg",
                                  "https://lmcscdn.jzwp.cn/1640325746309.jpg",
                                  "https://lmcscdn.jzwp.cn/1640325754387.jpg",
                                  "https://lmcscdn.jzwp.cn/1640325757262.jpg"], "type_id": 30, "type": 30,
                         "attr_datas": [
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1056,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1056,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1056,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1056,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1057,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1057,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1057,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1057,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1058,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1058,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1058,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1059,1058,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1056,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1056,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1056,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1056,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1057,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1057,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1057,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1057,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1058,1053,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1058,1053,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1058,1055,1049",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"},
                             {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1060,1058,1055,1050",
                              "incr_stock": "100",
                              "market_price": "300", "star_price": "null", "star_fee": "null", "thrift_fee": "20",
                              "storage_cost": "null", "clear_price": "null", "shop_price": "200", "vip_price": "null",
                              "cost_price": "100"}],
                         "sku_imgs": {"1053": {"thumb": ["https://lmcscdn.jzwp.cn/1640325734880.jpg"]},
                                      "1055": {"thumb": ["https://lmcscdn.jzwp.cn/1640325737078.jpg"]}}, "params": [],
                         "goods_id": 100005314, "supplier_type": 0}
        p = self.worker.post("add_goods", **temp_data)
        return p

    # 商品门店列表
    def get_goods_shop_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"id": "100004242"}
        p = self.worker.get("goods_shop_list", **temp_data)
        return p

    def get_order_list(self, **kwargs):
        """
        获取用户订单列表
        :param shop_id:所属店铺id
        :param deliver_shop_id:发货门店id
        :param shop_type:订单类型，1：平台订单，2：门店订单，不传是所有
        :param goods_source:订单来源, `全部`不转值, 从响应字段goods_source_map中获取下标值
        :return:
        """
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"page": 1, "pageSize": 10, "shop_id": 1}
        p = self.worker.get("order_list", **temp_data)
        items = p.json()['data']['items']
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 订单时效设置
    def set_config(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "order", "items": {"order_seckill_overtime_close": "40",  # 秒杀订单超过未付款，订单自动关闭
                                                     "order_overtime_close": "41",  # 正常订单超过未付款，订单自动关闭
                                                     "same_city_day": "42",  # 同城订单发货 天未收货，自动确认收货
                                                     "cross_city_day": "43",  # 跨城订单发货 天未收货，自动确认收货
                                                     "order_aftersale_day": "44",  # 订单完成超过 天自动结束交易，不能申请售后
                                                     "order_rebate_offline_day": "45",  # 订单完成超过 天自动结算返利
                                                     "order_cancel_protect_minutes": "46",  # 订单在 分钟内不可取消
                                                     "order_cancel_refund_minutes": "47"}}  # 订单在支付 分钟后不可取消订单
        p = self.worker.post("set_config", **temp_data)
        return p

    # 获取订单配置
    def get_config_order(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "order"}
        p = self.worker.get("get_config", **temp_data)
        return p

    # 设置会员卡充值金额
    def set_amount(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type=3加款  type=4扣款
            temp_data = {"key_value": [1000, 2000, 3000]}
        p = self.worker.post("set_amount", **temp_data)
        return p

    # 获取会员卡充值金额
    def get_amount(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type=3加款  type=4扣款
            temp_data = {}
        p = self.worker.get("get_amount", **temp_data)
        return p

    # 会员卡加扣款
    def update_vip_card(self, uid=None, **kwargs):
        if kwargs:
            temp_data = kwargs
            temp_data['uid'] = uid
        else:
            # type=3加款  type=4扣款
            temp_data = {"uid": uid, "type": 3, "money": 10000, "password": "234890",
                         "remark": "测试四道口是否撒旦发附近上来看积分卢卡斯的积分顺利打开附件加款啦"}
        p = self.worker.post("update_vip_card", **temp_data)
        return p

    # 门店加款
    def updata_shop_money(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {
                "shop_id": 136,
                "money": 1000000.01,
                "password": "234890",
                "remark": "备注"
            }
        p = self.worker.post("updata_shop_money", **temp_data)
        return p

    # 门店扣款
    def updata_shop_money_dec(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {
                "shop_id": 136,
                "money": 1000,
                "password": "234890",
                "remark": "备注"
            }
            p = self.worker.post("updata_shop_money_dec", **temp_data)
            return p

    # 门店余额明细
    def shop_capital_record(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 6系统加款 7系统扣款 8售后扣款
            temp_data = {"shop_id": "1", "type": "", "order_sn": "", "admin": "",
                         "start_time": "", "end_time": "", "export": "", "page": "1",
                         "pageSize": "10", }
        p = self.worker.get("shop_capital_record", **temp_data)
        items = p.json()['data']['items']
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 会员卡明细
    def member_vip_card(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 1、消费 2、退款 3、加款 4、扣款
            temp_data = {"uid": "", "type": "", "order_sn": "", "admin_id": "",
                         "start_time": "", "end_time": "", "page": "1",
                         "pageSize": "10", }
        p = self.worker.get("member_vip_card", **temp_data)
        items = p.json()['data']['items']
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 添加banner
    def add_banner(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 1、消费 2、退款 3、加款 4、扣款
            temp_data = {
                "area": [510000, 510100, 510107],
                "banner": "https://mmtcdn.jzwp.cn/1623925056763.jpg",
                "main_color": "#ffffff",
                "location": 1,
                "type": "article_list",
                "param": "/v4/school/list",
                "sort": 40,
                "is_enable": 1,
                "description": "描述描述",
                "start_at": "2021-08-02 16:19:26",
                "end_at": "2021-08-03 16:19:26",
                "shop_status": 2,
                "shop_list": [
                    {"id": 6, "name": "武侯环球中心店444"},
                    {"id": 7, "name": "武侯环球中心店555"}
                ]
            }
        p = self.worker.post("add_banner", **temp_data)
        print(p.json())
        return p

    # add_shop 添加门店
    def add_shop(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            name = self.faker.company()
            temp_data = {"name": name, "province_id": 510000, "city_id": 510100, "district_id": 510112,
                         "address": "吾悦广场", "longitude": "104.240829", "latitude": "30.577833", "phone": "13980883526",
                         "status": 10, "account_info": [{"account_id": 920, "role_name": "管理员"}],
                         "logo_img": "https://lmcscdn.jzwp.cn/1634092641180.jpg", "business_at": "9:00~4:00"}
        p = self.worker.post("add_shop", **temp_data)
        return p

    # 发货 send_goods
    def send_goods(self, order_sn=None, **kwargs):
        order_id = self.worker.get_order_id(order_sn)
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"items": [{"id": order_id, "code": "YTO", "sn": "123456789"}]}
        temp_data_send = {"type": 0}
        self.worker.post("save_goods", **temp_data)
        p = self.worker.post('send_goods', **temp_data_send)
        return p

    # 余额加扣款
    def add_money(self, uid=None, **kwargs):
        if kwargs:
            temp_data = kwargs
            temp_data['uid'] = uid
        else:
            temp_data = {"uid": uid, "type": 9, "money": "1000000", "remark": "测试充值", "password": "234890"}
        p = self.worker.post("add_money", **temp_data)
        return p

    # 测试发货  只针对线上商品
    def send_xianshang_goods(self):
        temp_data_send = {"type": 0}
        p = self.worker.post('send_goods', **temp_data_send)


if __name__ == '__main__':
    # for i in range(100):
    # uid = "10001550"
    # for i in range(100):
    # InterfaceWorkerB()
    InterfaceWorkerB().get_user_list()
