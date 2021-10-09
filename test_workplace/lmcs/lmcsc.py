# @time 2021/9/28 17:39
# @Author howell
# @File lmcsc.PY
import os
from test_workplace.lmcs.lmcs_utils import Login
from test_workplace.lmcs.lmcs_utils import CommonRequest
from common.controlexcel import ExcelUtil


class InterfaceWorkerForC(object):
    def __init__(self):
        self.excel_filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))
        self.count = 1
        self.s = Login().login_c("10001537")
        self.worker = CommonRequest("C", "10001537")

    # 下单
    def order_submit(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {"type": 1, "goods_id": 100004298, "sku_id": 100003277, "nums": 1, "coupon_id": 0,
                         "address_ids": 4921624, "buyer_message": "这是备注信息", "remark": "备注", "from": 0, }
        p = self.worker.post("order_submit", **temp_data)
        # items = p.json()['data']['items']
        # items.append(p.json()['data']['fields'])
        # ExcelUtil(self.excel_filepath, sheetname="Sheet1").write_response_data(items)
        print(p.request.body)
        print(p.request.headers)
        print(p.json())
        return p


if __name__ == '__main__':
    InterfaceWorkerForC().order_submit()
