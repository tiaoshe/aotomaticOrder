# @time 2022/6/13 16:49
# @Author howell
# @File demo_05.PY
# file_name: test_abc.py
import re


def test_re():
    p = re.compile(r'(\w+) (\w+)')  # \w = [A-Za-z0-9]
    s = 'hello 123, hello 456'

    print(p.sub(r'hello world', s))  # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
    print(p.sub(r'\2 \1', s))  # 引用分组

    def func(m):
        print(m)
        return 'hi' + ' ' + m.group(2)  # group(0) 表示本身，group(1)表示hello，group(2) 表示后面的数字

    print(p.sub(func, s))  # 多次sub，每次sub的结果传递给func
    # print(p.sub(func, s, 1))
