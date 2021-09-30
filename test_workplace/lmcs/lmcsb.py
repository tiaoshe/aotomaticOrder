# @time 2021/9/28 17:39
# @Author howell
# @File lmcsb.PY

from test_workplace.lmcs.lmcs_utils import CommonRequest
from common.controlexcel import ExcelUtil
import os


class InterfaceWorker(object):
    def __init__(self):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))

    # 获取用户列表数据
    def get_user_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"page": 1, "pageSize": 10, "type": -1}
        p = CommonRequest().get("member_list", **temp_data)
        items = p.json()['data']['items']
        items.append(p.json()['data']['fields'])
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 佣金设置
    def set_commission(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"contribution_proportion": 40, "base_commission_proportion": 60,
                         "overflow_commission_proportion": 20}
        p = CommonRequest().post("set_commission", **temp_data)
        return p

    # 获取配置
    def get_config(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "commission_config"}
        p = CommonRequest().get("get_config", **temp_data)
        return p

    # 渠道管理
    def add_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"name": "淘宝电商"}
        p = CommonRequest().post("add_channel", **temp_data)
        return p

    # 编辑渠道
    def edit_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 1, "name": "淘宝电商"}
            p = CommonRequest().post("add_channel", **temp_data)
            return p

    # 获取渠道列表
    def get_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"page": 1, "pageSize": "10"}
            p = CommonRequest().get("get_channel", **temp_data)
            items = p.json()['data']['items']
            items.append(p.json()['data']['fields'])
            ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
            return p

    # 编辑渠道
    def delete_channel(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"ids": "4,5,6"}
            p = CommonRequest().post("delete_channel", **temp_data)
            return p

    # 编辑用户
    def edit_member(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "nickname": "", "phone": "13980883526", "sex": "1",
                         "birthday": "2000-01-01"}
            p = CommonRequest().post("edit_member", **temp_data)
            return p

    # 删除分享人
    def delete_referrer(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431}
            p = CommonRequest().post("delete_referrer", **temp_data)
            return p

    # 编辑分享人
    def change_store(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "store_id": 10001431}
            p = CommonRequest().post("change_store", **temp_data)
            return p

    # 编辑所属门店
    def change_shop(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 10001431, "shop_id": 1}
            p = CommonRequest().post("change_shop", **temp_data)
            return p

    # 获取用户详情
    def member_info(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"uid": "10001537"}
        p = CommonRequest().get("member_info", **temp_data)
        return p

    # 获取品牌贡献列表
    def integral_record(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"shop_id": "-1", "uid": "10001537", "keywords": "", "phone": "",
                         "first_uid": "", "start_time": "", "end_time": "", "page": "1",
                         "pageSize": "10"}
        p = CommonRequest().get("integral_record", **temp_data)
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
        p = CommonRequest().get_download("integral_record_export", "test.xls", **temp_data)
        return p

    # 获取商品列表
    def goods_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # shop_id -1所有
            temp_data = {"shop_id": "-1", "page": "1", "pageSize": "20"}
        p = CommonRequest().get("goods_list", **temp_data)
        items = p.json()['data']['list']['items']
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 添加商品
    def add_goods(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"is_break": 1, "is_receive_way_logistics": 1, "freight_id": 543, "first_fee": 0,
                         "cross_border": 2, "second_fee": "0", "combination": 0, "zu_num": 0, "stock_double": 1,
                         "is_quick": 0, "is_top": 0, "is_welfare": 0, "team_strategy1": 0, "team_senior1": 0,
                         "team_angel1": 0, "team_angel2": 0, "brand_id": 17, "store_ids": [], "store_extend": [],
                         "start_type": 1, "end_type": 3, "cat_id": ["304"], "seckill_type": 1, "shop_type": 0,
                         "activity_svip": 1, "activity_star": 0, "title": "商品名称", "subtitle": "副标题", "goods_sn": "商品货号",
                         "supplier_id": 30357, "sort": "9999", "weight": "100", "volume_width": "101",
                         "content": "<p>图文详情</p>", "day_max": "127", "limit_max": "127", "single_max": "99",
                         "single_min": "1", "freight_type": 3, "shop_value": [],
                         "long_thumb": "https://dcygcdn.jzwp.cn/1632982609973.png", "seckill_begin_time": 1632931200,
                         "seckill_end_time": 1633104000, "seckill_flag": 1, "is_coupon_convert": 0, "cat_id1": "304",
                         "cat_id2": 0, "cat_id3": 0, "thumb": "https://dcygcdn.jzwp.cn/1632982603434.jpg",
                         "imgs": ["https://dcygcdn.jzwp.cn/1632982606675.jpg"], "stock_base": "10000", "type_id": 28,
                         "type": 28, "attr_datas": [
                    {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "", "incr_stock": "1000", "market_price": "120",
                     "star_price": "110", "star_fee": "12", "thrift_fee": "14", "storage_cost": "null",
                     "clear_price": "null", "shop_price": "119", "vip_price": "115", "cost_price": "50"}],
                         "sku_imgs": {},
                         "params": [{"key": "水电费", "value": "水电费"}], "goods_id": 100004240, "supplier_type": 0}
            p = CommonRequest().post("add_goods", **temp_data)
            return p

    # 订单时效设置
    def set_config(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "order", "items": {"order_seckill_overtime_close": "40",
                                                     "order_overtime_close": "41",
                                                     "same_city_day": "42",
                                                     "cross_city_day": "43",
                                                     "order_aftersale_day": "44",
                                                     "order_rebate_offline_day": "45",
                                                     "order_cancel_protect_minutes": "46",
                                                     "order_cancel_refund_minutes": "47"}}
        p = CommonRequest().post("set_config", **temp_data)
        return p

    # 获取订单配置
    def get_config_order(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"group": "order"}
        p = CommonRequest().get("get_config", **temp_data)
        return p

    # 会员卡加扣款
    def update_vip_card(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type=3加款  type=4扣款
            temp_data = {"uid": 10001537, "type": 3, "money": 12, "password": "234890", "remark": "测试加款啦"}
            p = CommonRequest().post("update_vip_card", **temp_data)
            return p

    # 门店加款
    def updata_shop_money(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type=3加款  type=4扣款
            temp_data = {
                "shop_id": 1,
                "money": 1000,
                "password": "234890",
                "remark": "备注"
            }
            p = CommonRequest().post("updata_shop_money", **temp_data)
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
        p = CommonRequest().get("shop_capital_record", **temp_data)
        print(p.json())
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
        p = CommonRequest().get("member_vip_card", **temp_data)
        print(p.json())
        return p


if __name__ == '__main__':
    InterfaceWorker().member_vip_card()
