# @time 2021/10/9 17:35
# @Author howell
# @File test_c.PY
from test_workplace.lmcs.lmcs_utils import Login
from test_workplace.lmcs.lmcsc import InterfaceWorkerForC
import pytest


class TestLC(object):
    def setup_class(self):
        self.s = Login().login_c("10001537")
        self.worker = InterfaceWorkerForC(self.s)

    def test_order_submit(self):
        data = {"type": 1, "goods_id": 100004298, "sku_id": 100003277, "nums": 1, "coupon_id": 0,
                "address_ids": 4921624, "buyer_message": "这是备注信息", "remark": "备注", "from": 0, }
        p = self.worker.order_submit(**data)
        print(p.json())


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
