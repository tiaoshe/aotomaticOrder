# @time 2021/10/9 13:58
# @Author howell
# @File test.PY
# 代码生成器
from jinja2 import Template


def render(tmpl, *args, **kwds):
    '''jinja2 render'''
    vars = dict(*args, **kwds)
    print(vars)
    tmp = Template(tmpl)
    return tmp.render(vars).strip()


if __name__ == '__main__':
    # tmpl_list = """
    # {% for fruit in fruits %}
    # {{ fruit }}
    # {% endfor %}
    # """
    # result = render(tmpl_list, fruits=fruits)
    # print(result)
    # fruits = ['apple', 'banana']
    # tmpl_list = """
    # {% for fruit in fruits -%}
    # {{ loop.index }}. {{ fruit }}
    # {% endfor %}
    # """
    #
    # print(render(tmpl_list, fruits=fruits))
    tml_class = """
    /n
    def {{methed}}(self):
        pass
    """

    result = render(tml_class, methed="howell")


    def save(data, filename='codes.py'):
        with open(filename, 'a') as f:
            f.write(data)


    save(data=result)
