# @time 2021/9/22 10:42
# @Author howell
# @File conftest.PY
import pytest
from test_workplace.starmall.utils import Login


@pytest.fixture()
def login_b():
    Login("host_star_b", "admin_login").login_b()
