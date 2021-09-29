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


if __name__ == '__main__':
    InterfaceWorker().add_channel()
