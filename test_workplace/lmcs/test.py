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
    #
    # def pay_order(self, order_sn, **kwargs):
    #     if kwargs:
    #         temp_data = kwargs
    #     else:
    #         temp_data = {"pay_type": 1, "order_sn": order_sn, "appName": "榴芒传说", "appVersion": "v0.1.3",
    #                      "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
    #                      "deviceModel": "microsoft"}
    #     p = self.worker.post("pay_order", **temp_data)
    #     return p

    tml_class = """
    def {{methed}}(self, **kwargs):
    if kwargs:
        temp_data = kwargs
    else:
        temp_data = {{data}}
    p = self.worker.post("{{methed}}", **temp_data)
    return p

    """
    data = {"pay_type": 1, "appName": "榴芒传说", "appVersion": "v0.1.3",
            "systemType": "mp", "systemVersion": "Windows 10 x64", "deviceId": "mini app",
            "deviceModel": "microsoft"}

    result = render(tml_class, methed="howell", data=data)


    def save(data, filename='codes.py'):
        with open(filename, 'a+') as f:
            f.write(data)
            f.write("\n\n")
    save(data=result)
