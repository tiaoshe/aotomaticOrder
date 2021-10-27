# @time 2021/9/29 15:08
# @Author howell
# @File test_b.PY
import pytest
from test_workplace.lmcs.lmcsb import InterfaceWorkerB
from common.controlexcel import ExcelUtil
import os
from faker import Faker


class TestLB(object):

    def setup_class(self):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))
        self.worker = InterfaceWorkerB()
        self.faker = Faker(locale='zh_CN')

    @pytest.mark.parametrize("uid", ["", "10001537"])
    @pytest.mark.parametrize("keywords", ["", "昵称"])
    @pytest.mark.parametrize("phone", ["", "18512819006"])
    @pytest.mark.parametrize("first_uid", ["", "10001533"])
    @pytest.mark.parametrize("start_time, end_time", [("2000-01-01 00:00:00", "2021-09-29 15:47:40"), ("", "")])
    def test_user_list(self, uid, keywords, phone, first_uid, start_time, end_time):
        """
        B端用户列表查询
        :param uid:
        :param keywords:
        :param phone:
        :param first_uid:
        :param start_time:
        :param end_time:
        :return:
        """
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_start()
        items = []
        data = {"page": 1, "pageSize": 10, "uid": uid, "keywords": keywords, "phone": phone,
                "first_uid": first_uid, "start_time": start_time, "end_time": end_time, "type": -1, }
        items.append(data)
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        self.worker.get_user_list(**data)

    @pytest.mark.parametrize("contribution_proportion", ["", "50", "120", "0", "10.23", "1000", "-10"])
    @pytest.mark.parametrize("base_commission_proportion", ["", "50", "120", "0", "10.23", "1000", "-30"])
    @pytest.mark.parametrize("overflow_commission_proportion", ["", "50", "120", "0", "10.23", "1000", "-10"])
    def test_set_commission(self, contribution_proportion, base_commission_proportion, overflow_commission_proportion):
        data = {"contribution_proportion": contribution_proportion,
                "base_commission_proportion": base_commission_proportion,
                "overflow_commission_proportion": overflow_commission_proportion}
        self.worker.set_commission(**data)

    @pytest.mark.parametrize("name", [" ", "sdfksdfkj", "   禄口街道付了款  ", "地方"])
    def test_add_channel(self, name):
        name_end = name
        data = {"name": name_end}
        self.worker.add_channel(**data)

    @pytest.mark.parametrize("name", ["", "sdfksdlfkjsdkfj", "收到了非跨境卵看书近地方粝食空弹剑"])
    @pytest.mark.parametrize("qd_id", ["1", "2"])
    def test_edit_channel(self, qd_id, name):
        data = {"id": qd_id, "name": name}
        self.worker.add_channel(**data)

    @pytest.mark.parametrize('id_user', ["", "10001431", "100045"])
    @pytest.mark.parametrize("nickname", ["", "酥颗点肌肤老师开到九方上岛咖啡就", "sdlkfjslkdfjsldkjfk"])
    @pytest.mark.parametrize("phone", ["", "18512816620", "13980808"])
    @pytest.mark.parametrize("sex", ["", "1", "2"])
    @pytest.mark.parametrize("birthday", ["", "2000-01-01"])
    def test_edit_member(self, id_user, nickname, phone, sex, birthday):
        data = {"id": id_user, "nickname": nickname, "phone": phone, "sex": sex,
                "birthday": birthday}
        self.worker.edit_member(**data)

    @pytest.mark.parametrize("id_user", ["", 1000143, 10001535, 10001533, 10001529])
    @pytest.mark.parametrize("store_id", ["", 10001533, 10001534, 10001537, 7, 1])
    def test_change_store(self, id_user, store_id):
        """
        编辑分享人
        :return:
        """
        data = {"id": id_user, "store_id": store_id}
        self.worker.change_store(**data)

    @pytest.mark.parametrize("id_user", ["", 1000143, 10001535, 10001533, 10001529])
    @pytest.mark.parametrize("shop_id", ["", 1, 7, 10001537, 5])
    def test_change_shop(self, id_user, shop_id):
        """
        修改所属店铺
        :return:
        """
        data = {"id": id_user, "shop_id": shop_id}
        self.worker.change_store(**data)

    def test_member_info(self):
        """
        获取用户详情
        :return:
        """
        data = {"uid": "10001537"}
        self.worker.member_info(**data)

    def test_goods_list(self):
        self.worker.goods_list()

    @pytest.mark.parametrize("time", [x for x in range(10)])
    def test_add_good(self, time):
        data = {"is_break": 0, "is_receive_way_logistics": 1, "cross_border": 2, "team_angel1": 0,
                "team_angel2": 0, "brand_id": 17, "start_type": 1, "end_type": 3, "cat_id": ["303"],
                "activity_svip": 0, "activity_star": 0, "title": "title", "subtitle": "副标题",
                "goods_sn": "商品货号", "supplier_id": 30356, "sort": "9999", "weight": "2", "volume_width": "3",
                "content": "<p>图文详情</p>", "buy_notice": "抢购须知", "shop_type": 0, "shop_value": [],
                "long_thumb": "https://lmcscdn.jzwp.cn/1634030440867.jpg", "is_coupon_convert": 0,
                "cat_id1": "303", "cat_id2": 0, "cat_id3": 0,
                "thumb": "https://lmcscdn.jzwp.cn/1634030433558.jpg",
                "imgs": ["https://lmcscdn.jzwp.cn/1634030436805.jpg"], "stock_base": "1000", "type_id": 27,
                "type": 27, "attr_datas": [
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "1035", "incr_stock": "1000",
                 "market_price": "299",
                 "star_price": "null", "star_fee": "null", "thrift_fee": "19", "storage_cost": "null",
                 "clear_price": "null", "shop_price": "249", "vip_price": "null", "cost_price": "10"},
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "2062", "incr_stock": "1000",
                 "market_price": "299",
                 "star_price": "null", "star_fee": "null", "thrift_fee": "19", "storage_cost": "null",
                 "clear_price": "null", "shop_price": "249", "vip_price": "null", "cost_price": "10"},
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "2063", "incr_stock": "1000",
                 "market_price": "299",
                 "star_price": "null", "star_fee": "null", "thrift_fee": "19", "storage_cost": "null",
                 "clear_price": "null", "shop_price": "249", "vip_price": "null", "cost_price": "10"}],
                "sku_imgs": {},
                "params": [], "goods_id": 100004580, "supplier_type": 0}
        self.worker.add_goods(**data)

    @pytest.mark.parametrize("same_city_day", ["0", "-10", "100", "", "20", "10000"])
    @pytest.mark.parametrize("cross_city_day", ["0", "-10", "100", "", "20", "10000"])
    @pytest.mark.parametrize("order_cancel_refund_minutes", ["0", "-10", "100", "", "20", "10000"])
    def test_set_config(self, same_city_day, cross_city_day, order_cancel_refund_minutes):
        data = {"group": "order", "items": {"order_seckill_overtime_close": "40",  # 秒杀订单超过未付款，订单自动关闭
                                            "order_overtime_close": "41",  # 正常订单超过未付款，订单自动关闭
                                            "same_city_day": same_city_day,  # 同城订单发货 天未收货，自动确认收货
                                            "cross_city_day": cross_city_day,  # 跨城订单发货 天未收货，自动确认收货
                                            "order_aftersale_day": "44",  # 订单完成超过 天自动结束交易，不能申请售后
                                            "order_rebate_offline_day": "45",  # 订单完成超过 天自动结算返利
                                            "order_cancel_protect_minutes": "46",  # 订单在 分钟内不可取消
                                            "order_cancel_refund_minutes": order_cancel_refund_minutes}}  # 订单在支付 分钟后不可取消订单
        self.worker.set_config(**data)

    @pytest.mark.parametrize("key_value", ["[1000, 2000, 3000]", "[-1000, 2000, 3000]", "[1000, 2000, 2000, 6000]",
                                           "[1000, 2000, 2000, 6000, 5, 6, 7, 9]", "[1000, "", 2000, 6000]"])
    def test_set_amount(self, key_value):
        data = {"key_value": key_value}
        self.worker.set_amount(**data)

    @pytest.mark.parametrize("type_h", [3, 4])
    @pytest.mark.parametrize("money", [-100, 100, 0, 1, 2, 999999999999999, ""])
    def test_update_vip_card(self, type_h, money):
        data = {"uid": 10001537, "type": type_h, "money": money, "password": "234890", "remark": "测试加款啦"}
        self.worker.update_vip_card(**data)

    @pytest.mark.parametrize("shop_id", [6, 7, 1])
    @pytest.mark.parametrize("money", [-100, 100, 0, 1, 2, 999999999999999, ""])
    def test_updata_shop_money(self, shop_id, money):
        data = {"shop_id": shop_id, "money": money, "password": "234890", "remark": "备注"}
        self.worker.updata_shop_money(**data)


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
