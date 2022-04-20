# @time 2022/1/12 9:31
# @Author howell
# @File smj_scene.PY
from test_workplace.smj.smjb import InterfaceModule
from test_workplace.smj.smjc import InterfaceModuleApi
from test_workplace.smj.smj_utils import *
import pytest, random
import allure
from faker import Faker

faker = Faker(locale='zh_CN')


class TestSmj(object):
    def setup_class(self):
        self.uid = 100053
        s = Login().login_b("host_smj_b", "admin_login")
        self.WorkerB = InterfaceModule(s)
        sc = Login().login_c(self.uid)
        self.WorkerC = InterfaceModuleApi(sc)

    @pytest.mark.parametrize("i", [i for i in range(60)])
    def test_add_coupon(self, i):
        # 优惠券名称name 优惠券描述description 发放数量num 每人限领user_num
        # 满金额：max
        # 减金额：money
        # 领取用户：member_type
        # 领取时间：start_at  end_at
        # 领取方式："grant_type": "giveout,receive",
        # 领取方式：support_receive  是否支持主动领取 1
        # 使用时间：ding_at  ding_at_end  day
        # 使用渠道：channel '使用渠道：1-线上，2-线下'
        # 使用类型：use_type 1-商品，2-服务'
        # 适用范围： range '使用范围：1-全部，2-指定商品服务，3-指定分类，4-排除指定商品服务'
        data = {"range": 1, "channel": 1, "day": 30, "use_type": 1, "name": str(i) + faker.sentence(), "num": "100",
                "money": "20",
                "user_num": "1", "max": "100.99", "member_type": "1,2", "grant_type": "giveout,receive",
                "start_at": get_now_time_cuo(), "end_at": get_now_time_cuo(60 * 60 * 24 * 10),
                "description": faker.sentence()}
        self.WorkerB.add_coupon(**data)

    # @pytest.mark.parametrize("address", ["四川省成都市龙泉驿区", " ", "舒服服点 ", "3"])
    # @pytest.mark.parametrize("province_id", ["510000", " ", "舒服服点 ", "3"])
    # @pytest.mark.parametrize("city_id", ["510100", " ", "510112 ", "3"])
    # @pytest.mark.parametrize("district_id", ["510112", " ", "510100 ", "3"])
    # @pytest.mark.parametrize("latitude", ["30.577833", " ", "510100 ", "3"])
    @pytest.mark.parametrize("area_ids", ["500000,500100,500300,510000", " ", "500000", "643"])
    def test_add_shop_offline(self, area_ids):
        # {"name": faker.company(), "contact_phone": "13980883526", "type": 1,
        #  "address": "四川省成都市龙泉驿区", "province_id": "510000", "city_id": "510100",
        #  "district_id": "510112", "note": "这个是商超", "status": 1,
        #  "latitude": "30.577833", "longitude": "104.240829", "template_id": 643,
        #  "area_ids": "500000,500100,500300,510000",}
        data = {"area_ids": area_ids}
        self.WorkerB.add_shop_offline(**data)

    @pytest.mark.parametrize("area_ids", ["500000,500100,500300,510000", " ", "500000", "643"])
    def test_shop_offline_list(self, area_ids):
        data = {"area_ids": area_ids}
        self.WorkerB.shop_offline_list(**data)

    @pytest.mark.parametrize("time", [x for x in range(2000)])
    def test_add_channel(self, time):
        data = {"name": faker.sentence()}
        self.WorkerB.add_channel(**data)

    @pytest.mark.parametrize("time", [x for x in range(50)])
    @pytest.mark.parametrize("ty,mark", [(9, "加钱"), (10, "扣钱")])
    def test_update_money(self, time, ty, mark):
        data = {"uid": 2, "type": ty, "money": time, "remark": mark}
        self.WorkerB.update_money(**data)

    @pytest.mark.parametrize("time", [x for x in range(50)])
    @pytest.mark.parametrize("ty,mark", [(3, "加钱咯"), (4, "扣钱咯")])
    def test_update_vip_card(self, time, ty, mark):
        data = {"uid": 13, "type": ty, "money": time, "remark": mark}
        self.WorkerB.update_vip_card(**data)

    def test_all_money(self):
        user_id = 100007
        data = {"uid": user_id, "type": 9, "money": 90000, "remark": "mark"}
        data1 = {"uid": user_id, "type": 3, "money": 80009.99, "remark": "mark"}
        self.WorkerB.update_money(**data)
        self.WorkerB.update_vip_card(**data1)

    @pytest.mark.parametrize("time", [x for x in range(20)])
    @pytest.mark.parametrize("ty,mark", [(11, "扣扣扣"), (11, "扣积分了")])
    def test_update_integral_record(self, time, ty, mark):
        # {"uid": 2, "type": 1, "point": 1000, "password": "123456", "remark": "备注"}
        data = {"uid": 13, "type": ty, "point": 10, "remark": mark}
        self.WorkerB.update_integral_record(**data)

    @pytest.mark.parametrize("time", [x for x in range(1)])
    @pytest.mark.parametrize("goods_id", [1000062781])
    def test_submmit_order_pay_supermarket(self, time, goods_id):
        goods_id = goods_id
        sku_id = get_sku_id(goods_id)[1][0]

        address_id = get_user_address_id(self.uid)[0][0]
        if self.uid == 100036:
            shop_id = 31478
        else:
            shop_id = get_shop_id(goods_id)[1][0]
            print(get_shop_id(goods_id))
        # shop_id = 31002
        # 1、快递，2、自提，3、同城
        deliver_type = 3
        # 优惠券ID查询 以及使用
        # 1 = > '微信',
        # 2 = > '小程序',
        # 3 = > 'IOS',
        # 4 = > '安卓',
        # 5 = > '网页'
        # random.choice(["wechat", "mp", "ios", "android", "wap"])
        sql = "select id FROM smj_coupon_record where uid=%s and cid=5315 and is_used=0;" % self.uid
        coupon_id = QueryData().get_data(sql)[0][0]
        add_goods_data = {"goods_id": goods_id, "sku_id": sku_id, "nums": 1, "address_ids": address_id,
                          "extend": {goods_id: {"buy_insurance": 0, "buyer_message": "杜鲁门啊 杜鲁门"}}, "shopId": shop_id,
                          "deliver_type": deliver_type, "expect_to_time": get_now_time(60 * 60 * 24),
                          "coupon_id": "",
                          "systemType": random.choice(["wechat", "mp", "ios", "android", "wap"])}
        response = self.WorkerC.submmit_order(**add_goods_data)
        order_sn = response['data']['order_sn']
        money = response['data']["actual_fee"]
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"}]}
        order_response = self.WorkerC.pay_order(**data)
        order_id = order_response['data']['id']
        # cancel_order = {"id": order_id}
        # # 取消订单
        # self.WorkerC.cancel_order(**cancel_order)
        # 接单数据准备
        pick_order = {"ids": order_id}
        # 接单
        self.WorkerB.order_picking_get(**pick_order)
        # 拣货完成
        pick_compelte = {"ids": order_id, "deliver_type": deliver_type}
        self.WorkerB.order_picking_compelte(**pick_compelte)
        return

        if deliver_type == 3:
            # 如果是同城配送需要将数据库中的订单状态修改为 6 配送中
            change_order_status(6, order_id)

        # 订单完成
        data_end = {"ids": order_id, "deliver_type": deliver_type}
        self.WorkerB.order_send_end(**data_end)
        return
        # 评价数据准备
        data_evalu = {"status": 0, "page": 1, "pageSize": 20}
        order_end_list = self.WorkerC.evaluate_list(**data_evalu)
        order_extent_id = order_end_list['data']['items'][0]['id']
        print(order_extent_id)
        order_id_end = order_end_list['data']['items'][0]["order_id"]
        goods_id_end = order_end_list['data']['items'][0]["goods_id"]
        # 发布评价[get_video()],
        evaluate_data = {"order_id": order_id_end, "goods_id": goods_id_end, "score": random.randint(1, 5),
                         "imgs": get_images(random.randint(1, 9)), "is_anonymity": 0,
                         "content": "图片-" + faker.text(max_nb_chars=2000), "video": "",
                         "order_extend_id": order_extent_id}
        self.WorkerC.add_evaluate(**evaluate_data)

    @pytest.mark.parametrize("i", [i for i in range(1)])
    def test_submmit_order_pay_yuncang(self, i):
        goods_id = "1000063042"
        sku_id = get_sku_id(goods_id)[0][0]
        print(get_sku_id(goods_id))
        address_id = get_user_address_id(self.uid)[0][0]
        shop_id = 31475
        # 优惠券ID查询 以及使用
        sql = "select id FROM smj_coupon_record where uid=%s and cid=5315 and is_used=0;" % self.uid
        coupon_id = QueryData().get_data(sql)[0][0]
        add_goods_data = {"goods_id": goods_id, "sku_id": sku_id, "nums": 1,
                          "address_ids": address_id,
                          "extend": {goods_id: {"buy_insurance": 1, "buyer_message": "这个备注信息应该能看到"}}, "shopId": shop_id,
                          "deliver_type": "1", "coupon_id": "", "integral_fee": 0,
                          "from": random.choice([1, 2, 3])}
        response = self.WorkerC.submmit_order(**add_goods_data)
        # 支付
        order_sn = response['data']['order_sn']
        money = response['data']["actual_fee"]
        # type balance|vip_card|wx
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"},
                                                   {"money": 0, "check": 0, "type": "vip_card"},
                                                   {"money": 0, "check": 0, "type": "wx"}]}
        order_response = self.WorkerC.pay_order(**data)
        order_id = order_response['data']['id']
        # cancel_order = {"id": order_id}
        # # 取消订单
        # self.WorkerC.cancel_order(**cancel_order)
        #
        data_order = {"items": [{"id": order_id, "code": "YTO", "sn": "YT6345970536613"}]}
        # 写入快递单号
        self.WorkerB.order_delivery(**data_order)
        # 一件发货
        self.WorkerB.order_delivery_send()
        # 确认收货
        confirm_data = {"id": order_id, "shopId": shop_id}
        self.WorkerC.confirm_receipt(**confirm_data)

        # 评价数据准备
        order_end_list = self.WorkerC.evaluate_list()
        order_extent_id = order_end_list['data']['items'][0]['id']
        order_id_end = order_end_list['data']['items'][0]["order_id"]
        goods_id_end = order_end_list['data']['items'][0]["goods_id"]
        # 发布评价[get_video()],
        evaluate_data = {"order_id": order_id_end, "goods_id": goods_id_end, "score": random.randint(1, 5),
                         "imgs": get_images(4), "is_anonymity": 0,
                         "content": "视频-" + faker.text(max_nb_chars=120), "video": [get_video()],
                         "order_extend_id": order_extent_id}
        self.WorkerC.add_evaluate(**evaluate_data)
        flag = 4
        if flag == 0:
            # 申请售后退货
            self.test_apply_sale(sku_id, order_id, shop_id)
        elif flag == 1:
            # 换货
            self.test_apply_sale1(sku_id, order_id, shop_id)
        elif flag == 2:
            # 补偿
            self.test_apply_sale2(sku_id, order_id, shop_id)
        elif flag == 3:
            # 补发
            self.test_apply_sale3(sku_id, order_id, shop_id)
        elif flag == 4:
            return

    # 积分兑换
    def test_score_change(self):
        address_id = get_user_address_id(self.uid)[0][0]
        shop_id = 31475
        data = {"shop_id": shop_id, "sku_id": 100016899, "nums": 1, "address_id": address_id, "appName": "圣美家",
                "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                "deviceModel": "microsoft"}
        response = self.WorkerC.confire_integral(**data)
        order_id = response['data']["id"]
        data_order = {"items": [{"id": order_id, "code": "YTO", "sn": "YT6345970536613"}]}
        # 写入快递单号
        self.WorkerB.order_delivery(**data_order)
        # 一件发货
        self.WorkerB.order_delivery_send()
        # 确认收货
        confirm_data = {"id": order_id, "shopId": shop_id}
        self.WorkerC.confirm_receipt(**confirm_data)

    # 申请退货
    def test_apply_sale(self, sku_id, order_id, shop_id):
        # 申请售后 5 是补偿坏损  6是补发  1 退货 2换货
        sales_data = {"sale_type": 1, "sale_type_desc": "退货", "reason": "7天无理由退货", "description": faker.sentence(),
                      "imagesArr": [],
                      "order_id": order_id, "return_sku_list": [{"sku_id": sku_id, "count": 1}],
                      "imgs": get_images(random.randint(1, 8)),
                      "video": ["https://smjcdn.jzwp.cn/_625e7d6635b3b.mp4"]}
        self.WorkerC.order_sales(**sales_data)
        return
        # 同意售后 1.查询售后信息
        sql = "SELECT id FROM `smj-dev`.`smj_order_sales` WHERE `order_id` = %s" % order_id
        sale_id = QueryData().get_data(sql)[0][0]
        sale_data = {"id": sale_id}
        sale_response = self.WorkerB.order_sale_detail(**sale_data)
        goods_fee = sale_response['data']['detail']['goods_fee']
        apply_data = {"add_fee": "0.00", "is_quality": "0", "deduct_freight_fee": "0.00", "freight_type": "0",
                      "remark": faker.sentence(), "freight_fee": 0, "is_rebate": "1", "goods_fee": goods_fee,
                      "compensate": "0.00",
                      "receiver_address": faker.name() + "," + faker.phone_number() + "," + faker.address(),
                      "sale_id": sale_id,
                      "type": "1",
                      "return_sku_list": [{"sku_id": sku_id, "count": 1}]}
        self.WorkerB.order_sale(**apply_data)

        sale_d = {"sale_id": sale_id}
        sale_c = {"id": sale_id}
        # 编辑售后单物流,B端编辑物流
        # self.WorkerB.edit_sale_order(**sale_d)
        self.WorkerC.send_back(**sale_c)
        # 确认收货
        sale_data_id = {"sale_id": sale_id, "remark": faker.sentence()}
        self.WorkerB.order_take(**sale_data_id)
        # 同意退款
        sale_data_agree = {"sale_id": sale_id, "remark": faker.sentence()}
        self.WorkerB.agree_refund_money(**sale_data_agree)

    # 换货
    def test_apply_sale1(self, sku_id, order_id, shop_id):
        # 申请售后 5 是补偿坏损  6是补发  1 退货 2换货
        sales_data = {"sale_type": 2, "sale_type_desc": "退货", "reason": "7天无理由退货", "description": faker.sentence(),
                      "imagesArr": [],
                      "order_id": order_id, "return_sku_list": [{"sku_id": sku_id, "count": 1}],
                      "imgs": get_images(random.randint(1, 8)),
                      "video": ["https://smjcdn.jzwp.cn/_625e7d6635b3b.mp4"]}
        self.WorkerC.order_sales(**sales_data)
        # 同意售后 1.查询售后信息
        sql = "SELECT id FROM `smj-dev`.`smj_order_sales` WHERE `order_id` = %s" % order_id
        sale_id = QueryData().get_data(sql)[0][0]
        sale_data = {"id": sale_id}
        sale_response = self.WorkerB.order_sale_detail(**sale_data)
        goods_fee = sale_response['data']['detail']['goods_fee']
        apply_data = {"add_fee": "0.00", "is_quality": "0", "deduct_freight_fee": "0.00", "freight_type": "0",
                      "remark": faker.sentence(), "freight_fee": 0, "is_rebate": "1", "goods_fee": goods_fee,
                      "compensate": "32.01",
                      "receiver_address": faker.name() + "," + faker.phone_number() + "," + faker.address(),
                      "sale_id": sale_id,
                      "type": "2",
                      "return_sku_list": [{"sku_id": sku_id, "count": 1}]}
        self.WorkerB.order_sale(**apply_data)
        sale_c = {"id": sale_id}
        # 编辑售后单物流,B端编辑物流
        self.WorkerC.send_back(**sale_c)
        # 确认收货
        sale_data_id = {"sale_id": sale_id, "remark": faker.sentence()}
        self.WorkerB.order_take(**sale_data_id)
        # 同意退货
        sale_data_agree = {"sale_id": sale_id}
        self.WorkerB.order_send(**sale_data_agree)

    # 坏损 补偿
    def test_apply_sale2(self, sku_id, order_id, shop_id):
        # 申请售后 5 是补偿  6是补发  1 退货
        sales_data = {"sale_type": 5, "sale_type_desc": "退货", "reason": "7天无理由退货", "description": faker.sentence(),
                      "imagesArr": [],
                      "order_id": order_id, "return_sku_list": [{"sku_id": sku_id, "count": 1}],
                      "imgs": get_images(random.randint(1, 8)),
                      "video": [get_video()]}
        self.WorkerC.order_sales(**sales_data)
        # 同意售后 1.查询售后信息
        sql = "SELECT id FROM `smj-dev`.`smj_order_sales` WHERE `order_id` = %s" % order_id
        sale_id = QueryData().get_data(sql)[0][0]
        sale_data = {"id": sale_id}
        sale_response = self.WorkerB.order_sale_detail(**sale_data)
        goods_fee = sale_response['data']['detail']['goods_fee']
        apply_data = {"add_fee": random.randint(1, 100), "is_quality": "0", "deduct_freight_fee": "0.00",
                      "freight_type": "0",
                      "remark": faker.sentence(), "freight_fee": 0, "is_rebate": "0", "goods_fee": goods_fee,
                      "compensate": "0.00",
                      "sale_id": sale_id,
                      "type": "5",
                      "return_sku_list": [{"sku_id": sku_id, "count": 1}]}
        self.WorkerB.order_sale(**apply_data)
        # 同意退款
        sale_data_agree = {"sale_id": sale_id, "remark": faker.sentence()}
        self.WorkerB.agree_refund_money(**sale_data_agree)

    #   补发
    def test_apply_sale3(self, sku_id, order_id, shop_id):
        # 申请售后 5 是补偿  6是补发  1 退货
        sales_data = {"sale_type": 6, "sale_type_desc": "退货", "reason": "7天无理由退货", "description": faker.sentence(),
                      "imagesArr": [],
                      "order_id": order_id, "return_sku_list": [{"sku_id": sku_id, "count": 1}],
                      "imgs": get_images(random.randint(1, 8)),
                      "video": ["https://smjcdn.jzwp.cn/_625e7d6635b3b.mp4"]}
        self.WorkerC.order_sales(**sales_data)
        # 同意售后 1.查询售后信息
        sql = "SELECT id FROM `smj-dev`.`smj_order_sales` WHERE `order_id` = %s" % order_id
        sale_id = QueryData().get_data(sql)[0][0]
        sale_data = {"id": sale_id}
        sale_response = self.WorkerB.order_sale_detail(**sale_data)
        goods_fee = sale_response['data']['detail']['goods_fee']
        apply_data = {"add_fee": "0.00", "is_quality": "0", "deduct_freight_fee": "0.00", "freight_type": "0",
                      "remark": faker.sentence(), "freight_fee": 0, "is_rebate": "0", "goods_fee": goods_fee,
                      "compensate": "0.00",
                      "sale_id": sale_id,
                      "type": "6",
                      "return_sku_list": [{"sku_id": sku_id, "count": 1}]}
        self.WorkerB.order_sale(**apply_data)
        # 同意退货
        sale_data_agree = {"sale_id": sale_id}
        self.WorkerB.order_send(**sale_data_agree)

    def test_sale_shenhe(self):
        sku_id = "100014937"
        order_id = "209"
        shop_id = "31365"
        self.test_apply_sale(sku_id, order_id, shop_id)

    # 服务下单
    @pytest.mark.parametrize("x", [x for x in range(1)])
    def test_submit_order_pay_fuwu(self, x):
        goods_id = "1000063075"
        sku_id = get_sku_id(goods_id)[0][0]
        address_id = get_user_address_id(self.uid)[0][0]
        shop_id = 31547
        # 优惠券ID查询 以及使用
        sql = "select id FROM smj_coupon_record where uid=%s and cid=5317 and is_used=0;" % self.uid
        coupon_id = QueryData().get_data(sql)[0][0]
        submit_data = {"goods_id": goods_id, "shopId": shop_id, "sku_id": sku_id, "latitude": "0", "longitude": "0",
                       "num": 3,
                       "address_id": address_id, "deliver_type": 2, "integral_fee": 0, "gift_fee": 0,
                       "coupon_id": "", "name": "howell",
                       "systemType": random.choice(["wechat", "mp", "ios", "android", "wap"])}
        response = self.WorkerC.order_offline_submit(**submit_data)
        order_id = response['data']['id']

        order_sn = response['data']['order_sn']

        # cancel_order = {"id": order_id}
        # # 取消订单
        # self.WorkerC.cancel_order(**cancel_order)

        pay_type_data = {"id": order_id}
        # 选择支付方式 获取支付金额
        response_pay_inform = self.WorkerC.choice_pay_type(**pay_type_data)
        money = response_pay_inform['data']['detail']["actual_fee"]
        # 准备支付数据
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"},
                                                   {"money": 0, "check": 0, "type": "vip_card"},
                                                   {"money": 0, "check": 0, "type": "wx"}]}
        # 支付
        self.WorkerC.pay_order(**data)
        # 查询服务订单列表，方便查看
        self.WorkerB.offline_list()
        for i in range(0, len(get_fuwu_code_id(order_id))):
            fuwu_code_id = get_fuwu_code_id(order_id)[i][0]
            # 订单核销
            use_data = {"goods_code_id": fuwu_code_id, "shop_id": random.choice([31547, 31548, 31549]),
                        "order_id": order_id}
            self.WorkerB.order_use(**use_data)
        # # 评价数据准备
        # order_extent_id = get_fuwu_extend_id(order_id)[0][0]
        # # 发布评价
        # evaluate_data = {"order_id": order_id, "goods_id": goods_id, "score": random.randint(1, 5),
        #                  "imgs": get_images(3), "is_anonymity": 0,
        #                  "content": faker.text(max_nb_chars=2000), "video": [get_video()],
        #                  "order_extend_id": order_extent_id}
        # self.WorkerC.add_evaluate(**evaluate_data)

    # 加入购物车
    def test_join_cart(self, goods_id):
        goods_id = goods_id
        for sku in get_sku_id(goods_id):
            sku_id = sku[0]
            data = {"shopId": "31365", "cart_id": 0, "sku_id": sku_id, "num": 1}
            self.WorkerC.join_cart(**data)

    # 获取购物车列表
    def test_cart_list(self):
        data = {"shopId": "31343"}
        self.WorkerC.cart_list(**data)

    # 购物车下单-云仓
    def test_cart_submit(self):
        goods_list = ["1000060675", "1000060673", "1000060671"]
        # goods_list = ["1000060706"]
        for good_id in goods_list:
            self.test_join_cart(good_id)
        address_id = get_user_address_id(self.uid)[0][0]
        shop_id = 31365
        # 准备购物车数据
        cart_data = {"shopId": "31365"}
        cart_response = self.WorkerC.cart_list(**cart_data)
        items_data = cart_response['data']['cloud']['common']['items']
        print(items_data)
        extend = dict()
        cart_ids = ""
        goods_id = ""
        for item in items_data:
            cart_ids = cart_ids + str(item['id']) + ","
            if str(item['goods_id']) not in goods_id:
                goods_id = str(goods_id) + str(item['goods_id']) + ","
        for good_id in goods_list:
            extend[good_id] = {"buy_insurance": 1, "buyer_message": "霸气侧漏"}
        submit_data = {"type": 2, "goods_id": goods_id[:-1], "shopId": shop_id, "sku_id": "", "latitude": "0",
                       "longitude": "0", "num": 1,
                       "address_ids": address_id, "deliver_type": 1, "integral_fee": 0, "gift_fee": 0,
                       "cart_ids": cart_ids[:-1], "extend": extend}
        response = self.WorkerC.submmit_order(**submit_data)
        order_id = response['data']['order_id']
        order_sn = response['data']['order_sn']
        pay_type_data = {"id": order_id}
        # 选择支付方式 获取支付金额
        response_pay_inform = self.WorkerC.choice_pay_type(**pay_type_data)
        money = response_pay_inform['data']['detail']["actual_fee"]
        # 准备支付数据
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"}]}
        # 支付
        self.WorkerC.pay_order(**data)

    # 购物车下单-自提订单
    def test_cart_submit_self(self):
        # goods_list = ["1000060675", "1000060673", "1000060671"]
        goods_list = ["1000060674", "1000060672"]
        for good_id in goods_list:
            self.test_join_cart(good_id)
            self.test_join_cart(good_id)
        address_id = get_user_address_id(self.uid)[0][0]
        shop_id = 31365
        # 准备购物车数据
        cart_data = {"shopId": "31365"}
        cart_response = self.WorkerC.cart_list(**cart_data)
        items_data = cart_response['data']['self']['common']['items']
        extend = dict()
        cart_ids = ""
        goods_id = ""
        deliver_type = 3
        for item in items_data:
            cart_ids = cart_ids + str(item['id']) + ","
            if str(item['goods_id']) not in goods_id:
                goods_id = goods_id + str(item['goods_id']) + ","
        for good_id in goods_list:
            extend[good_id] = {"buy_insurance": 1, "buyer_message": "霸气侧漏"}
        submit_data = {"type": 2, "goods_id": goods_id[:-1], "shopId": shop_id, "sku_id": "", "latitude": "0",
                       "longitude": "0", "num": 1,
                       "address_ids": address_id, "deliver_type": deliver_type,
                       "expect_to_time": get_now_time(1800), "integral_fee": 0, "gift_fee": 0,
                       "cart_ids": cart_ids[:-1], "extend": extend}
        response = self.WorkerC.submmit_order(**submit_data)
        order_id = response['data']['order_id']
        order_sn = response['data']['order_sn']
        pay_type_data = {"id": order_id}
        # 选择支付方式 获取支付金额
        response_pay_inform = self.WorkerC.choice_pay_type(**pay_type_data)
        money = response_pay_inform['data']['detail']["actual_fee"]
        # 准备支付数据
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"}]}
        # 支付
        order_response = self.WorkerC.pay_order(**data)
        order_id = order_response['data']['id']
        # cancel_order = {"id": order_id}
        # # 取消订单
        # self.WorkerC.cancel_order(**cancel_order)
        # # 接单数据准备
        # pick_order = {"ids": order_id}
        # # 接单
        # self.WorkerB.order_picking_get(**pick_order)
        # # 拣货完成
        # pick_compelte = {"ids": order_id, "deliver_type": deliver_type}
        # self.WorkerB.order_picking_compelte(**pick_compelte)
        # if deliver_type == 3:
        #     # 如果是同城配送需要将数据库中的订单状态修改为 6 配送中
        #     change_order_status(6, order_id)
        # # 订单完成
        # data_end = {"ids": order_id, "deliver_type": deliver_type}
        # self.WorkerB.order_send_end(**data_end)

    # 购买礼品卡
    @pytest.mark.parametrize("money", [100])
    @pytest.mark.parametrize("s", [s for s in range(50)])
    @pytest.mark.parametrize("i",
                             ["https://smjcdn.jzwp.cn/1646821811269.png",
                              "https://smjcdn.jzwp.cn/1646821883417.png",
                              "https://smjcdn.jzwp.cn/1646821886972.png"])
    def test_confirm_gift(self, money, i, s):
        data = {"money": money, "cover_img": i}
        response = self.WorkerC.confirm_gift(**data)
        order_sn = response['data']['order_sn']
        money = response['data']['price']
        # 准备支付数据
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"}]}
        # 支付
        self.WorkerC.pay_order(**data)

    # 抽奖活动
    def test_get_raffle(self):
        title = faker.sentence() + str(random.randint(10000, 100000))
        raffle_data = {"title": title}
        # 创建抽奖活动
        self.WorkerB.add_raffle(**raffle_data)
        # 获取活动ID
        sql = "SELECT max(id) FROM `smj-dev`.`smj_raffle`"
        raffle_id = QueryData().get_data(sql)[0][0]
        data_random_money = {"raffle_id": raffle_id, "name": "随机余额-" + faker.sentence(), "type": 4,
                             "thumb": get_image(random.randint(1, 15)), "min_balance": "3",
                             "max_balance": "8",
                             "chance": "10",
                             "stock": "100", "sort": "1", "status": 1}
        data_money = {"raffle_id": raffle_id, "name": "余额-" + faker.sentence(), "type": 3,
                      "thumb": get_image(random.randint(1, 15)), "values": "1",
                      "chance": "10",
                      "stock": "100", "sort": "1", "status": 1}
        data_shiwu = {"raffle_id": raffle_id, "name": "实物-" + faker.sentence(), "type": 1,
                      "thumb": get_image(random.randint(1, 15)), "values": "1",
                      "chance": "10",
                      "stock": "100", "sort": "1", "status": 1}
        data_integral = {"raffle_id": raffle_id, "name": "积分-" + faker.sentence(), "type": 2,
                         "thumb": get_image(random.randint(1, 15)), "values": "100",
                         "chance": "10",
                         "stock": "100", "sort": "1", "status": 1}
        data_coupon = {"raffle_id": raffle_id, "name": "优惠券-" + faker.sentence(), "type": 5,
                       "thumb": get_image(random.randint(1, 15)), "values": "5488",
                       "chance": "10",
                       "stock": "100", "sort": "1", "status": 1}
        data_no = {"raffle_id": raffle_id, "name": "没中奖-" + faker.sentence(), "type": 6,
                   "thumb": get_image(random.randint(1, 15)), "values": "0",
                   "chance": "30",
                   "stock": -1, "sort": "1", "status": 1}
        # 添加抽奖商品
        self.WorkerB.add_prize(**data_coupon)
        self.WorkerB.add_prize(**data_random_money)
        self.WorkerB.add_prize(**data_money)
        self.WorkerB.add_prize(**data_shiwu)
        self.WorkerB.add_prize(**data_shiwu)
        self.WorkerB.add_prize(**data_shiwu)
        self.WorkerB.add_prize(**data_integral)
        self.WorkerB.add_prize(**data_no)
        # self.WorkerB.add_prize(**data_no)
        raffle_data = {"id": raffle_id}
        # 抽奖
        # self.WorkerC.raffle_luck(**raffle_data)

    @pytest.mark.parametrize("i", [i for i in range(100)])
    def test_raffle_luck(self, i):
        raffle_data = {"id": 158}
        # 抽奖
        self.WorkerC.raffle_luck(**raffle_data)

    # 领奖
    @pytest.mark.parametrize("i", [i for i in range(1)])
    def test_get_prize(self, i):
        self.WorkerC.luck_record()
        data = {"id": "27402"}
        self.WorkerC.get_prize(**data)

    # 添加门店员工
    @pytest.mark.parametrize("i", [i for i in range(100)])
    def test_add_shop_account(self, i):
        data = {}
        self.WorkerB.add_shop_account(**data)

    def test_add_goods(self, time):
        goods_id_list = list()
        for i in range(2):
            data = {"title": "云仓-42秒杀-" + str(time) + faker.sentence()}
            data1 = {"title": "自营仓-42秒杀-" + str(time) + faker.sentence()}
            self.WorkerB.add_goods_shop(**data1)
            goods_id_list.append(str(get_max_goods_id() - 1))
            self.WorkerB.add_goods_yuncang(**data)
            goods_id_list.append(str(get_max_goods_id() - 1))
        return goods_id_list

    # 添加秒杀活动
    @pytest.mark.parametrize("i", [i for i in range(2)])
    def test_add_seckill(self, i):
        shop_offline_id = "31475"
        # shop_offline_id = "31554"
        goods_list = self.test_add_goods(i)
        # goods_list = [1000062921 + i for i in range(0, 20)]
        time.sleep(6)
        Q = QueryData()
        goods = list()
        for goods_id in goods_list:
            sku_list = []
            sql = "SELECT id FROM `smj-dev`.`smj_goods_sku` WHERE `goods_id` = %s" % goods_id
            sku_list = Q.get_data(sql)
            sku = list()
            count = 0
            for sku_id_tu in sku_list:
                count += 1
                if count % 2 == 0:
                    sku_id = sku_id_tu[0]
                    sql = "SELECT id FROM `smj-dev`.`smj_inventory` WHERE `sku_id` = %s" % sku_id
                    inventory_id = Q.get_data(sql)[0][0]
                    sql = "select shop_price from smj_goods_sku where sku_id = %s" % sku_id
                    sku_price = Q.get_data(sql)[0][0]
                    mota_sku = {"sku_id": sku_id, "inventory_id": inventory_id, "kill_price": "0", "vip_price": "0",
                                "bonus_second_vip": "0", "stock": "0", "status": "0", "shop_price": sku_price}
                    sku.append(mota_sku)
                else:
                    sku_id = sku_id_tu[0]
                    sql = "SELECT id FROM `smj-dev`.`smj_inventory` WHERE `sku_id` = %s" % sku_id
                    inventory_id = Q.get_data(sql)[0][0]
                    sql = "select shop_price from smj_goods_sku where sku_id = %s" % sku_id
                    sku_price = Q.get_data(sql)[0][0]
                    mota_sku = {"sku_id": sku_id, "inventory_id": inventory_id, "kill_price": "9.9", "vip_price": "8.8",
                                "bonus_second_vip": "1", "stock": "20", "status": "1", "shop_price": sku_price}
                    sku.append(mota_sku)
            goods_mota = {"goods_id": goods_id, "shop_offline_id": "31343", "single_max": "20", "single_min": "2",
                          "day_max": "20",
                          "limit_max": "20", "virtual_percentavirtual_scores": "0", "sort": random.randint(1, 5),
                          "sku": sku}
            goods.append(goods_mota)
        data = {"shop_offline_id": shop_offline_id, "goods": goods, "start_time": get_now_time(30 * i + 10),
                "end_time": get_now_time(i * 30 * 60 + 60 * 60), }
        self.WorkerB.add_seckill(**data)

    # 添加满减活动
    @pytest.mark.parametrize("i", [i + 1 for i in range(1)])
    def test_add_lessen(self, i):
        # 新增满减活动商品
        goods_list = self.test_add_goods(i)
        # print(goods_list)
        # goods_list = [1000062921 + i for i in range(0, 20)]
        data = {"goods": goods_list}
        # 创建满减活动
        self.WorkerB.add_lessen(**data)

    # 添加作者
    @pytest.mark.parametrize("i", [i for i in range(5000)])
    def test_add_author(self, i):
        self.WorkerB.add_author()

    @pytest.mark.parametrize("i", [i for i in range(500)])
    def test_add_author(self, i):
        self.WorkerB.add_content()

    # @pytest.mark.parametrize("i", [i for i in range(100012, 100013)])
    def test_new_user_money(self):
        user_id = "100029"
        # 加余额
        data1 = {"uid": user_id}
        self.WorkerB.update_money(**data1)
        # # 加地址  关闭fiddler
        # sc = Login().login_c(user_id)
        # WC = InterfaceModuleApi(sc)
        # WC.add_address()
        # 加积分
        data2 = {"uid": user_id, "type": 1, "point": 200000, "remark": "加扣积分"}
        self.WorkerB.update_integral_record(**data2)
        # # 优惠券发放
        # data3 = {"coupon_id": 5315, "coupon_num": "10", "member_ids": "16"}
        # self.WorkerB.coupon_send(**data3)
        # 会员卡加钱
        data3 = {"uid": user_id}
        self.WorkerB.update_vip_card(**data3)

    @pytest.mark.parametrize("i", [i for i in range(1, 100)])
    def test_new_user(self, i):
        user_id = 100026
        # 加地址  关闭fiddler
        sc = Login().login_c(user_id)
        WC = InterfaceModuleApi(sc)
        WC.add_address()

    def test_del_user(self):
        user_id = "100041"
        q = QueryData()
        sql = "DELETE FROM `smj-dev`.`smj_third` WHERE `uid` = %s" % user_id
        q.update_data(sql)
        sql_token = "DELETE FROM `smj-dev`.`smj_member_access_token` WHERE `uid` = %s" % user_id
        q.update_data(sql_token)
        sql_phone = "UPDATE `smj-dev`.`smj_member` SET `phone` = '' WHERE `id` = %s" % user_id
        q.update_data(sql_phone)
        data = {"sex": 0, "phone": faker.phone_number(), "nickname": "小米CS", "id": user_id}
        self.WorkerB.edit_user_info(**data)

    # 会员卡充值
    # @pytest.mark.parametrize("i", [i for i in range(20)])
    @pytest.mark.parametrize("money", [100])
    def test_confirm_vip(self, money):
        money = money
        data = {"money": money}
        response = self.WorkerC.confirm_vip(**data)
        order_sn = response['data']['order_sn']
        # 准备支付数据
        data = {"order_sn": order_sn, "pay_info": [{"money": money, "check": 1, "type": "balance"}]}
        # 支付
        self.WorkerC.pay_order(**data)

    # @pytest.mark.parametrize("i", [i for i in range(100012, 100013)])
    def test_set_money(self):
        user_id = "100053"
        add_or_jian = 2
        # 1为扣减 2 不兑换 3 要兑换
        if add_or_jian == 1:
            type1 = 11
            type2 = 4
            type3 = 22
        else:
            type1 = 1
            type2 = 3
            type3 = 9
        # 加积分
        data2 = {"uid": user_id, "type": type1, "point": 20000, "remark": "加扣积分"}
        self.WorkerB.update_integral_record(**data2)
        # 会员卡加钱
        data3 = {"uid": user_id, "type": type2, "money": 10000}
        self.WorkerB.update_vip_card(**data3)
        # 加余额
        data1 = {"uid": user_id, "type": type3, "money": 10000}
        self.WorkerB.update_money(**data1)
        if add_or_jian == 3:
            # 查询礼品卡
            sql = "select gift_code,password FROM smj_gift_card where status=0 and money=100;"
            Qd = QueryData().get_data(sql)
            # 绑定礼品卡
            sc = Login().login_c(user_id)
            worker = InterfaceModuleApi(sc)
            data4 = {"shop_id": 31475, "code": Qd[0][0], "password": Qd[0][1], "appName": "圣美家",
                     "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64",
                     "deviceId": "mini app",
                     "deviceModel": "microsoft", "from": 2}
            worker.bind_gift_card(**data4)

    # 测试求和
    def test_order_clearing(self):
        data = {"pageSize": 20}
        p = self.WorkerB.order_clearing(**data)
        num = p['data']['count']
        data1 = {"pageSize": num, "uid": 100041}
        p1 = self.WorkerB.order_clearing(**data1)
        money = 0
        money1 = 0
        order_sn = []
        for item in p1['data']['items']:
            if item['order_sn'] not in order_sn:
                order_sn.append(item['order_sn'])
                if item['pay_name'] == "已删除":
                    money1 -= float(item['money'])
                else:
                    money1 += float(item['money'])
                    money += float(item['actual_fee'])
        print(money)
        print(money1)

    # 关闭所有售后
    def test_close_all_sales(self):
        p = self.WorkerB.sales_list()
        for order_obj in p['data']['items']:
            id = order_obj['id']
            data = {"sale_id": id}
            self.WorkerB.order_deny(**data)


if __name__ == '__main__':
    # pytest.main(["--alluredir", "./report/report/result", "test_smj_scene.py::TestSmj::test_submmit_order_pay_yuncang"])
    TestSmj().test_submmit_order_pay_yuncang()
