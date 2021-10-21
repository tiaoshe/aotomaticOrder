# @time 2021/10/9 17:35
# @Author howell
# @File test_c.PY
from test_workplace.lmcs.lmcs_utils import Login
from test_workplace.lmcs.lmcsc import InterfaceWorkerForC
from test_workplace.lmcs.lmcsb import InterfaceWorkerB
from test_workplace.lmcs.lmcs_utils import ControlMysql
import pytest


class TestLC(object):
    def setup_class(self):
        self.uid = "10001579"
        self.s = Login().login_c(self.uid)
        self.workerC = InterfaceWorkerForC(self.s)
        self.workerB = InterfaceWorkerB()
        self.baseWorker = ControlMysql()

    def test_submit_pay(self):
        """
        下单
        :return:
        """
        # 数据处理
        data = {"type": 1, "bargain_id": 0, "buy_insurance": 0, "join_store": 0, "goods_id": "100004348",
                "sku_id": "100003327", "nums": 1, "couponNeedNum": 1, "cart_ids": "", "address_ids": 4921651,
                "coupon_id": "", "extend": {"100004348": {"buy_insurance": 0, "buyer_message": "包装给我搞严实点"}},
                "buy_svip": 0,
                "scene": "null", "source": "null", "appName": "榴芒传说", "appVersion": "v1.0.0", "systemType": "mp",
                "systemVersion": "Windows 10 x64", "deviceId": "mini app", "deviceModel": "microsoft", "shopId": "1"}
        # 下单goods_id
        goods_id = "100004540"
        # 获取sku_id
        sku_id = self.baseWorker.get_sku_id(goods_id)
        # 获取地址
        p_address_list = self.workerC.get_address_list()
        address_id = p_address_list.json()['data']['items'][0]['id']
        data['goods_id'] = goods_id
        data['extend'] = {goods_id: {"buy_insurance": 0, "buyer_message": "包装给我搞严实点"}}
        data['sku_id'] = sku_id
        data['address_ids'] = address_id
        # 提交订单
        p = self.workerC.order_submit(**data)
        order_sn = p.json()['data']['order_sn']
        p_info = self.workerC.get_member_info()
        if float(p_info.json()['data']['balance']) <= 500:
            self.workerB.add_money(self.uid)
        # 支付获取支付结果
        p_pay = self.workerC.pay_order(order_sn)
        result = p_pay.json()['message']
        assert result == "ok"
        return order_sn

    def test_send_goods(self, order_sn=None):
        """
        订单发货
        :return:
        """
        order_sn = order_sn
        p = self.workerB.send_goods(order_sn)
        assert p.json()['message'] == "ok"

    def test_order_finish(self, order_sn=None):
        """
        完成订单
        :return:
        """
        order_sn = order_sn
        order_id = self.baseWorker.get_order_id(order_sn)
        self.workerC.confirm_receipt(order_id)

    def test_apply_sale(self):
        """
        发起售后
        :return:
        """
        order_sn = self.test_submit_pay()
        self.test_send_goods(order_sn)
        self.test_order_finish(order_sn)
        self.workerC.order_sales(order_sn)

    def test_add_money(self):
        """
        余额增加
        :return:
        """
        uid = "10001580"
        p = self.workerB.add_money(uid)
        assert p.json()['message'] == "ok"

    # 设置新用户是店铺管理员 设置品牌贡献值 用户下单测试 #TODO

    def test_delete_user_relations(self):
        # 删除用户关系
        uid = "10001562"
        p = self.baseWorker.delete_user_relations(uid)
        assert p == "ok"

    def test_get_phone_number(self):
        # 查询用户密码
        phone = "18612819029"
        p = self.baseWorker.get_phone_number(phone)
        print(p)

    def test_add_goods_to_shop(self):
        # 店铺管理将商品设置到自己的门店中
        goods_id = "100004335"
        sku_ids = self.baseWorker.get_sku_ids(goods_id)
        sku_list = []
        for sku_id in sku_ids:
            sku_data = {"sku_id": sku_id, "nums": 1000, "virtual_sale_num": 1000}
            sku_list.append(sku_data)

        data = {"goods_id": goods_id, "status": 10, "shop_id": 244, "sku": sku_list}
        self.workerC.shop_goods_edit(**data)

    @pytest.mark.parametrize("user_id",
                             ['10001559', '10001558', '10001557', '10001556', '10001555', '10001553', '10001552',
                              '10001550', '10001549', '10001548'])
    @pytest.mark.parametrize("store_id", ['10001569'])
    def test_set_super(self, user_id, store_id):
        # 批量绑定上级
        data = {"id": user_id, "store_id": store_id}
        self.workerB.change_store(**data)

    def test_set_link_superuser(self):
        """
        设置链式用户关系
        :return:
        """
        user_list = ['10001559', '10001558', '10001557', '10001556', '10001555', '10001553', '10001552',
                     '10001550', '10001549', '10001569']
        for user in user_list:
            if user != user_list[-1]:
                index = user_list.index(user)
                data = {"id": user, "store_id": user_list[index + 1]}
                self.workerB.change_store(**data)

    def test_end(self):
        order_sn = "202110191547227154766"
        self.test_send_goods(order_sn)
        self.test_order_finish(order_sn)


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
