# @time 2022/1/20 14:31
# @Author howell
# @File test_sample.PY
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
