# @time 2021/9/18 15:11
# @Author howell
# @File test_starb.PY
import pytest
from test_workplace.starmall.starb import StarUtil
from test_workplace.starmall.utils import GetView
from faker import Faker
import random


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

    def test_change_user_type(self):
        args = ("interface", "test_edit_user_type")
        data = {"member_id": "23", "type_id": "3"}
        temp = StarUtil()
        for num in range(1, 10000000):
            data['type_id'] = random.randint(1, 3)
            data['member_id'] = random.randint(12, 23)
            temp.post(*args, **data)


class TestContent(object):
    """
    运营内容管理
    """

    def setup_class(self):
        self.fake = Faker()

    # 运营-内容管理-作者管理-添加作者
    def test_add_author(self):
        # http://staradmin.dev.jzwp.shop/v1/forum/author/save    add_author
        args = ("interface", "add_author")
        data = {"id": "", "name": "邓齐西", "avatar": "https://shopcdn.jzwp.cn/vc-upload-1632297790084-6.jpeg",
                "status": 10}
        temp = StarUtil()
        for num in range(1, 10030):
            data['name'] = self.fake.name()
            # 调用请求方法
            temp.post(*args, **data)

    def test_add_forum(self):
        # http://staradmin.dev.jzwp.shop/v1/forum/action/create
        args = ("interface", "create_forum")
        data = {"uid": "4105", "content": "水电费", "imgs": ["https://shopcdn.jzwp.cn/vc-upload-1632392802290-6.jpeg"],
                "video": "", "goods_list": [58], "sort": 26, "virtual_like_num": 100, "virtual_share_num": 100,
                "active_status": "1", "disable_status": "1", "is_visible": 1, "username": " Gail Smith "}
        temp = StarUtil()
        for num in range(1, 2):
            data['content'] = self.fake.name()
            data['imgs'] = GetView().get_images(2)
            # 调用请求方法
            temp.post(*args, **data)


class TestCategory(object):
    """
    商品管理；分类管理
    """

    def setup_class(self):
        self.fake = Faker()

    # 运营-内容管理-作者管理-添加作者
    def test_add_category(self):
        # http://staradmin.dev.jzwp.shop/v1/goods/category/add  goods_category_create
        args = ("interface", "goods_category_create")
        data = {"name": "test", "pid": 0, "thumb": "https://shopcdn.jzwp.cn/vc-upload-1632388679924-71.jpeg",
                "sort": "50", "display": 1}
        temp = StarUtil()
        for num in range(1, 10030):
            data['name'] = "test" + str(num)
            data['sort'] = 50 + num
            # 调用请求方法
            temp.post(*args, **data)


if __name__ == '__main__':
    # pytest.main(["-s", "starb.py::TestMember::test_get_users"])
    pytest.main(["-s", "starb.py::TestMember::test_change_user_type"])
    # pytest.main(["-s", "starb.py::TestContent::test_add_author"])
