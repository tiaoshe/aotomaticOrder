# @time 2021/10/9 17:35
# @Author howell
# @File test_c.PY
from test_workplace.lmcs.lmcs_utils import Login
from test_workplace.lmcs.lmcsc import InterfaceWorkerForC
from test_workplace.lmcs.lmcsb import InterfaceWorkerB
from test_workplace.lmcs.lmcs_utils import ControlMysql
import pytest
import allure


class TestLC(object):
    def setup_class(self):
        self.uid = "10001597"
        self.s = Login().login_c(self.uid)
        self.workerC = InterfaceWorkerForC(self.s)
        self.workerB = InterfaceWorkerB()
        self.baseWorker = ControlMysql()

    # @pytest.mark.parametrize("time", [x + 1 for x in range(18)])
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
        goods_id = "100004590"
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
        # 是否付款
        flag = True
        if flag:
            order_sn = p.json()['data']['order_sn']
            p_info = self.workerC.get_member_info()
            if float(p_info.json()['data']['balance']) <= 50000:
                self.workerB.add_money(self.uid)
                self.workerB.update_vip_card(self.uid)
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

    def test_cancel_order(self, order_sn=None):
        """
        完成订单
        :return:
        """
        order_sn = order_sn
        order_id = self.baseWorker.get_order_id(order_sn)
        self.workerC.cancel_order(order_id)

    def test_orders_send(self):
        # 批量将代发货列表的 商品发货
        orders_list = self.workerC.get_user_order_list()
        for order_sn in orders_list:
            self.test_send_goods(order_sn)

    @allure.feature('下单确认收货售后')
    @pytest.mark.parametrize("times", [times + 1 for times in range(5)])
    def test_apply_sale_allure(self, times):
        """
        发起售后
        :return:
        """
        with allure.step("下单"):
            order_sn = self.test_submit_pay()
        with allure.step("发货"):
            self.test_send_goods(order_sn)
        with allure.step("确认收货"):
            self.test_order_finish(order_sn)
        # with allure.step("申请售后"):
        #     self.workerC.order_sales(order_sn)

    def test_add_money(self):
        """
        余额增加
        :return:
        """
        uid = "10001594"
        p = self.workerB.add_money(uid)
        assert p.json()['message'] == "ok"

    # 设置新用户是店铺管理员 设置品牌贡献值 用户下单测试 #TODO

    @pytest.mark.parametrize("goods_id",
                             [100004588, 100004589, 100004590, 100004586, 100004587, 100004583, 100004584, 100004585,
                              100004581, 100004582, 100004545, 100004542, 100004541, 100004540, 100004520, 100004512,
                              100004502, 100004500, 100004402, 100004401, 100004400, 100004399, 100004398, 100004397,
                              100004394, 100004393, 100004392, 100004391, 100004388, 100004386, 100004385, 100004384,
                              100004383, 100004378, 100004376, 100004372, 100004369, 100004348, 100004347, 100004345,
                              100004343, 100004339, 100004337, 100004334, 100004333, 100004300, 100004299, 100004298,
                              100004286, 100004235, 100004234, 100004231, 100004184, 100004030, 100004059, 100004039,
                              100004037, 100004025, 100003914, 100003913, 100003742, 100003698, 100003699, 100003696,
                              100003697, 100003695, 100001315, 100004539, 100004364, 100001284, 100004220, 100004214,
                              100004213, 100004212, 100004209, 100004208, 100004205, 100004199, 100004183]
                             )
    def test_add_goods_to_shop(self, goods_id):
        # 店铺管理将商品设置到自己的门店中
        goods_id = goods_id
        sku_ids = self.baseWorker.get_sku_ids(goods_id)
        sku_list = []
        for sku_id in sku_ids:
            sku_data = {"sku_id": sku_id, "nums": 100, "virtual_sale_num": 100}
            sku_list.append(sku_data)

        data = {"goods_id": goods_id, "status": 10, "shopId": 256, "sku": sku_list}
        self.workerC.shop_goods_edit(**data)

    @pytest.mark.parametrize("user_id", ['10001595', '10001594', '10001593', '10001592', '10001591', '10001590',
                                         '10001589', '10001588', '10001587', '10001586', '10001585', '10001584',
                                         '10001583', '10001582', '10001581', '10001580', '10001579', '10001578',
                                         '10001577', '10001576', '10001575', '10001574', '10001573', '10001572',
                                         '10001571', '10001570', '10001569', '10001568', '10001567', '10001565',
                                         '10001564', '10001563', '10001562', '10001561', '10001560', '10001559',
                                         '10001558', '10001557', '10001556', '10001555', '10001553', '10001552',
                                         '10001550', '10001549', '10001548', '10001547', '10001546', '10001545',
                                         '10001544', '10001543', '10001542', '10001541', '10001537', '10001536',
                                         '10001535', '10001534', '10001533', '10001532', '10001530', '10001529',
                                         '10001528', '10001527', '10001526', '10001524', '10001523', '10001522',
                                         '10001521', '10001520', '10001519', '10001518', '10001517', '10001516',
                                         '10001515', '10001514', '10001513', '10001511', '10001509', '10001508',
                                         '10001506', '10001505', '10001504', '10001503', '10001502', '10001501',
                                         '10001500', '10001499', '10001498', '10001497', '10001496', '10001495',
                                         '10001494', '10001493', '10001492', '10001489', '10001487', '10001486',
                                         '10001485', '10001484', '10001483', '10001482', '10001481', '10001480',
                                         '10001479', '10001478', '10001477', '10001476', '10001475', '10001474',
                                         '10001473', '10001472', '10001471', '10001470', '10001469', '10001468',
                                         '10001467', '10001466', '10001465', '10001464', '10001463', '10001462',
                                         '10001461', '10001460', '10001459', '10001458', '10001457', '10001455',
                                         '10001454', '10001453', '10001452', '10001451', '10001450', '10001449',
                                         '10001448', '10001447', '10001446', '10001445', '10001444', '10001443',
                                         '10001442', '10001440', '10001439', '10001438', '10001436', '10001435',
                                         '10001434', '10001433', '10001432', '10001431', '10001430', '10001429']
                             )
    @pytest.mark.parametrize("store_id", ['10001595'])
    def test_set_super(self, user_id, store_id):
        # 批量绑定上级
        data = {"id": user_id, "store_id": store_id}
        self.workerB.change_store(**data)

    def test_set_link_superuser(self):
        """
        设置链式用户关系
        :return:
        """
        user_list = ['10001597', '10001596', '10001598']
        for user in user_list:
            if user != user_list[-1]:
                index = user_list.index(user)
                data = {"id": user, "store_id": user_list[index + 1]}
                self.workerB.change_store(**data)

    @pytest.mark.parametrize("times", [x for x in range(10)])
    def test_end(self, times):
        # 生成取消订单
        order_sn = self.test_submit_pay()
        self.test_cancel_order(order_sn)

    @pytest.mark.parametrize("times", [x for x in range(200)])
    def test_add_vip_money(self, times):
        self.workerC.confirm_top_up()

    def test_send_good(self):
        order_sn = " 21110510182938041  "
        order_sn.strip()
        self.test_send_goods(order_sn)
        # self.test_order_finish(order_sn)

    @pytest.mark.parametrize("member_id",
                             ['10001553', '10001552', '10001550', '10001549', '10001548', '10001547', '10001546',
                              '10001545', '10001544', '10001543', '10001542', '10001541', '10001537', '10001536',
                              '10001535', '10001534', '10001533', '10001532', '10001530', '10001529'])
    def test_add_shop_user(self, member_id):
        self.workerC.add_shop_user(member_id)

    def test_delete_user_relations(self):
        # 删除用户关系
        uid = "10001605"
        p = self.baseWorker.delete_user_relations(uid)
        assert p == "ok"

    def test_get_phone_number(self):
        # 查询用户密码
        phone = "18612819067"
        p = self.baseWorker.get_phone_number(phone)
        print(p)

    def test_add_vip_balance_money(self):
        uid = "10001606"
        balance_data = {"uid": uid, "type": 9, "money": "150", "remark": "测试充值", "password": "234890"}
        vip_data = {"uid": uid, "type": 3, "money": "30", "password": "234890",
                    "remark": "测试四道口是否撒旦发附近上来看积分卢卡斯的积分顺利打开附件加款啦"}
        # 添加会员卡和余额
        self.workerB.add_money(**balance_data)
        self.workerB.update_vip_card(**vip_data)


if __name__ == '__main__':
    pytest.main(['-v', '-s', "--alluredir=report", "test_scene.py::TestLC::test_apply_sale"])
