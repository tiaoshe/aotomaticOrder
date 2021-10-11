# @time 2021/9/28 17:39
# @Author howell
# @File lmcsc.PY
import os
from test_workplace.lmcs.lmcs_utils import Login
from test_workplace.lmcs.lmcs_utils import CommonRequest
from common.controlexcel import ExcelUtil


class InterfaceWorkerForC(object):
    def __init__(self, session):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_c_report.xls'))
        self.s = session
        self.worker = CommonRequest("C", session)

    # 下单
    def order_submit(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"type": 1, "bargain_id": 0, "buy_insurance": 0, "join_store": 0, "goods_id": "100004300",
                         "sku_id": "100003279", "nums": 1, "couponNeedNum": 1, "cart_ids": "", "address_ids": 4921611,
                         "coupon_id": "", "extend": {"100000194": {"buy_insurance": 0, "buyer_message": ""}},
                         "scene": "null", "source": "null", "appName": "榴芒传说", "appVersion": "v0.1.3",
                         "systemType": "mp", "systemVersion": "Android 10", "deviceId": "mini app",
                         "deviceModel": "Redmi K20 Pro", "shopId": "22"}
        p = self.worker.post("order_submit", **temp_data)
        print(p.json())
        # order_sn = p.json()['data']['order_sn']
        # self.pay_order(order_sn)
        return p

    # 支付接口
    def pay_order(self, order_sn, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"pay_type": 1, "order_sn": order_sn, "appName": "榴芒传说", "appVersion": "v0.1.3",
                         "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
                         "deviceModel": "microsoft"}
        p = self.worker.post("pay_order", **temp_data)
        return p

    # confirm_top_up 会员金额确认
    def confirm_top_up(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"money": 1000}
        p = self.worker.post("confirm_top_up", **temp_data)
        order_sn = p.json()['data']['order_sn']
        p1 = self.pay_order(order_sn)
        print(p1.json())

        return p

    # vip_card_list 会员卡明细
    def vip_card_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type：1、消费，2、退款，3、系统添加，4、系统扣款，5、充值
            temp_data = {"type": 5, "start_time": "2021-09-01", "end_time": "2021-12-01", "page": 1, "pageSize": 10}
        p = self.worker.get("vip_card_list", **temp_data)
        print(p.json())
        return p

    # vip_card_amount 会员卡充值页面信息获取
    def vip_card_amount(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {}
        p = self.worker.get("vip_card_amount", **temp_data)
        print(p.json())
        return p

    # pay_order_info 获取订单支付信息
    def pay_order_info(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": 14976}
        p = self.worker.get("pay_order_info", **temp_data)
        print(p.json())
        return p

    # order_confirm 确认订单
    def order_confirm(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type:  #1-立即购买-2-购物车
            temp_data = {"goods_id": 14976, "sku_id": 14976, "type": 14976, "nums": 14}
        p = self.worker.get("order_confirm", **temp_data)
        print(p.json())
        return p

    # 订单列表order_list_c
    def order_list_c(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 1待付款2待发货3待收货4已完成0全部订单
            temp_data = {"status": 0, "page": 1, "pageSize": 10}
        p = self.worker.get("order_list_c", **temp_data)
        print(p.json())
        items = p.json()['data']['items']
        ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        return p

    # 订单详情
    def order_detail(self, order_id, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 1待付款2待发货3待收货4已完成0全部订单 例如：14986
            temp_data = {"id": order_id}
        p = self.worker.get("order_detail", **temp_data)
        print(p.json())
        return p

    # 个人信息 member_info_lmcs
    def member_info_lmcs(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # 1待付款2待发货3待收货4已完成0全部订单 例如：14986
            temp_data = {}
        p = self.worker.get("member_info_lmcs", **temp_data)
        print(p.json())
        return p

    # 贡献值列表 integration_list
    def integration_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # type -1 展示所有
            temp_data = {"type": -1, "start_at": "2021-09-01", "end_at": "2021-11-01", "page": 1, "pageSize": 10}
        p = self.worker.get("integration_list", **temp_data)
        print(p.json())
        return p

    # 我的会员 new_member_list
    def new_member_list(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # keywords ID，手机号搜索，名称模糊搜索  time_type total、全部，yesterday、昨天，today、今天，current_week、本周，current_month、本月
            # sort 2、创建时间正序，3、创建时间倒序，4、贡献值倒序，5、贡献值正序，6、最近活跃倒序，7、最近活跃正序
            temp_data = {"keywords": "", "time_type": "total", "sort": 2, "start_at": "2021-09-01",
                         "end_at": "2021-11-01",
                         "page": 1, "pageSize": 10}
        p = self.worker.get("new_member_list", **temp_data)
        print(p.json())
        return p

    # 获取配置文件 get_config_c
    def get_config_c(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # api_home_module 首页栏目配置
            # platform_integral_rule 贡献值规则
            # platform_vip_rule	 会员协议
            # platform_remark 平台介绍
            # notice_broadcast 最新播报
            temp_data = {"key": "platform_vip_rule"}
        p = self.worker.get("get_config_c", **temp_data)
        print(p.json())
        return p

    # 店铺订单列表 store_order
    def store_order(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            # const STATUS_WAIT_PAY = 1;//待支付
            # const STATUS_WAIT_SEND = 2;//待发货
            # const STATUS_WAIT_GET = 3;//待收货
            # const STATUS_END = 5;//已完成
            # const STATUS_CLOSE = 7;//已关闭
            temp_data = {"keywords": "", "status": "1", "page": 1, "pageSize": 10}
        p = self.worker.get("store_order", **temp_data)
        print(p.json())
        return p

    # 订单详情 store_order_detail
    def store_order_detail(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": "14986"}
        p = self.worker.get("store_order_detail", **temp_data)
        print(p.json())
        return p

    # 关闭订单 close_store_order
    def close_store_order(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": "14986"}
        p = self.worker.get("close_store_order", **temp_data)
        print(p.json())
        return p

    # 订单发货 store_order_delivery
    def store_order_delivery(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"id": "14986"}
        p = self.worker.post("store_order_delivery", **temp_data)
        print(p.json())
        return p


if __name__ == '__main__':
    s = Login().login_c("10001520")
    order_sn = "202110111135237722229"
    order_id = 14986
    InterfaceWorkerForC(s).order_submit()
