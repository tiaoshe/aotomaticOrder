# @time 2021/10/21 13:48
# @Author howell
# @File test1.PY
class TestDemo(object):
    count = 0
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__()
        return cls.instance

    def __init__(self):
        name = "howell"
        print(name)
        TestDemo.count += 1


if __name__ == '__main__':
    T1 = TestDemo()
    TestDemo()

    print(TestDemo.count)
