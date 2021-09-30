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

    @pytest.mark.parametrize("contribution_proportion", ["", "50", "120", "0", "10.23", "100", "-10"])
    @pytest.mark.parametrize("base_commission_proportion", ["", "50", "120", "0", "10.23", "100", "-10"])
    @pytest.mark.parametrize("overflow_commission_proportion", ["", "50", "120", "0", "10.23", "100", "-10"])
    def test_set_commission(self, contribution_proportion, base_commission_proportion, overflow_commission_proportion):
        data = {"contribution_proportion": contribution_proportion,
                "base_commission_proportion": base_commission_proportion,
                "overflow_commission_proportion": overflow_commission_proportion}
        self.worker.set_commission(**data)

    @pytest.mark.parametrize("name", ["", "50", "疯狂的小兔兔", "   ",
                                      "等黄河时空裂缝就刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭等黄河时空裂缝就刘克俭多舒服卵看书近地方刘克俭多舒服卵看书近地方刘克俭",
                                      "涛哥哥哥哥哥二哥哥", "   天才兔兔    "])
    def test_add_channel(self, name):
        data = {"name": name}
        self.worker.add_channel(**data)

    @pytest.mark.parametrize("name", ["", "sdfksdlfkjsdkfj", "收到了非跨境卵看书近地方粝食空弹剑"])
    @pytest.mark.parametrize("qd_id", ["1", "2"])
    def test_edit_channel(self, qd_id, name):
        data = {"id": qd_id, "name": name}
        self.worker.add_channel(**data)


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
