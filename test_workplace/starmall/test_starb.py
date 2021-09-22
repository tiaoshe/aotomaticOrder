# @time 2021/9/18 15:11
# @Author howell
# @File test_starb.PY
import pytest
from test_workplace.starmall.starb import StarUtil


class TestMember(object):
    """
    本测试类测试用户相关的内容
    """

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_get_users(self):
        # 匹配配置文件路径
        args = ("interface", "get_user_list")
        # 接口参数准备
        kwargs = {}
        kwargs['pageSize'] = 10
        kwargs['page'] = 1
        kwargs['member_id'] = ""
        kwargs['member_type_id'] = ""
        kwargs['referer_member'] = ""
        kwargs['created_at'] = ""
        # 调用请求方法
        p = StarUtil().get(*args, **kwargs)
        # 向表格写入items中的数据
        items = p.json()['data']['items']
        member_ids = []
        for item in items:
            member_ids.append(item['id'])
            print(item)
        print(member_ids)
        assert len(member_ids) == 10


if __name__ == '__main__':
    pytest.main(["-s", "starb.py::TestMember::test_get_users"])
