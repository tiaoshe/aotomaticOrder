# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
import os


def test_os():
    print(os.name)
    print(os.getcwd())
    print(type(os.getcwd()))
    print(os.listdir(r"D:\pythonProject\aotomaticOrder\demo_300"))
