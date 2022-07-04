# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
# file_name: test_abc.py
import pytest


class Test_ABC:
    # 函数级开始
    def setup(self):
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        print("------->teardown_method")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")
