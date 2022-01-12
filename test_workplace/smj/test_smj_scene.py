# @time 2022/1/12 9:31
# @Author howell
# @File smj_scene.PY
from test_workplace.smj.smjb import InterfaceModule
from test_workplace.smj.smj_utils import Login
import pytest
import allure


class TestSmj(object):
    def setup_class(self):
        s = Login().login_b("host_smj_b", "admin_login")
        self.WorkerB = InterfaceModule(s)

    @pytest.mark.parametrize("name", ["这是优惠券名称1", ])
    @pytest.mark.parametrize("description", ["这是优惠券描述", ])
    def test_add_coupon(self, name, description):
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
        data = {"name": name, "description": description, "channel": 2}
        self.WorkerB.add_coupon(**data)


if __name__ == '__main__':
    pytest.main(["--alluredir", "./report/report/result", "test_smj_scene.py::TestSmj::test_add_coupon"])
