# @time 2021/9/29 15:08
# @Author howell
# @File test_b.PY
import pytest
from test_workplace.lmcs.lmcsb import InterfaceWorker
from common.controlexcel import ExcelUtil
import os


class TestLB(object):

    def setup_class(self):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))
        self.worker = InterfaceWorker()

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

    @pytest.mark.parametrize("name", ["", "50", "疯狂的小兔兔", "   ",
                                      "等黄河时空裂缝就刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵"
                                      "看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地"
                                      "方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭"
                                      "等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时"
                                      "空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝"
                                      "就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克"
                                      "俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒"
                                      "服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书"
                                      "近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘"
                                      "克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄"
                                      "河时空裂缝就刘克俭多舒服卵看书近地方刘克俭多舒服卵看书近地方刘克俭",
                                      "涛哥哥哥哥哥二哥哥", "   天才兔兔    "])
    def test_add_channel(self, name):
        data = {"name": name}
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

    @pytest.mark.parametrize("shop_type", [0, 1, 99, "", 2])
    @pytest.mark.parametrize("shop_value", ["", [1, 2], [1], [], [1, 2, 3, 6, 7, 14, 15, 16, 17]])
    def test_add_good(self, shop_type, shop_value):
        data = {"is_break": 1, "is_receive_way_logistics": 1, "freight_id": 543, "first_fee": 0,
                "cross_border": 2, "second_fee": "0", "combination": 0, "zu_num": 0, "stock_double": 1,
                "is_quick": 0, "is_top": 0, "is_welfare": 0, "team_strategy1": 0, "team_senior1": 0,
                "team_angel1": 0, "team_angel2": 0, "brand_id": 17, "store_ids": [], "store_extend": [],
                "start_type": 1, "end_type": 3, "cat_id": ["304"], "seckill_type": 1, "shop_type": shop_type,
                "activity_svip": 1, "activity_star": 0, "title": "商品名称测试抢购须知", "subtitle": "副标题", "goods_sn": "商品货号",
                "supplier_id": 30357, "sort": "9999", "weight": "100", "volume_width": "101",
                "content": "<p>图文详情</p>", "day_max": "127", "limit_max": "127", "single_max": "99",
                "single_min": "1", "freight_type": 3, "shop_value": shop_value,
                "long_thumb": "https://dcygcdn.jzwp.cn/1632982609973.png", "seckill_begin_time": 1632931200,
                "seckill_end_time": 1633104000, "seckill_flag": 1, "is_coupon_convert": 0, "cat_id1": "304",
                "cat_id2": 0, "cat_id3": 0, "thumb": "https://dcygcdn.jzwp.cn/1632982603434.jpg",
                "imgs": ["https://dcygcdn.jzwp.cn/1632982606675.jpg"], "stock_base": "10000", "type_id": 28,
                "type": 28, "attr_datas": [
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "", "incr_stock": "1000", "market_price": "120",
                 "star_price": "110", "star_fee": "12", "thrift_fee": "14", "storage_cost": "null",
                 "clear_price": "null", "shop_price": "119", "vip_price": "115", "cost_price": "50"}],
                "sku_imgs": {},
                "params": [{"key": "水电费", "value": "水电费"}], "goods_id": 100004273, "supplier_type": 0,
                "buy_notice": "冷风机是砥砺奋进收到了看法就熟练度开飞机SDK返利将收到了非跨境收到了看法就是邓刘克俭发送到联发科就收到了非跨境收到了反馈"}
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

    @pytest.mark.parametrize("key_value", [[1000, 2000, 3000], [-1000, 2000, 3000], [1000, 2000, 2000, 6000],
                                           [1000, 2000, 2000, 6000, 5, 6, 7, 9], [1000, "", 2000, 6000]])
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
