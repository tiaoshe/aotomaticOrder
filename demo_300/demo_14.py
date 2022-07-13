# @time 2022/7/5 10:01
# @Author howell
# @File demo_12.PY
import requests
from faker import Faker
from test_workplace.smj.smj_utils import *

faker = Faker(locale='zh_CN')
import random
import queue


def login():
    url = "http://mmt.dev.jzwp.shop/v1/account/login"
    data = {"username": "李杰2", "password": "123456"}
    s = requests.Session()
    s.post(url=url, json=data)
    return s


def add_goods(session, num):
    url = "http://mmt.dev.jzwp.shop/v1/goods/save"
    goods_id = 1000077500
    for i in range(1, num):
        goods_id += 1
        sort = 450 + i
        title = "抢购" + "【" + str(i + 450) + "】" + faker.text(max_nb_chars=20)[:-1]
        data = {"is_break": 0, "is_receive_way_logistics": 1, "first_fee": 0, "cross_border": 2, "second_fee": "0",
                "combination": 0, "zu_num": 0, "stock_double": 1, "is_quick": 0, "is_top": 0, "is_welfare": 0,
                "team_strategy1": 0, "team_senior1": 0, "team_angel1": 0, "team_angel2": 0, "store_ids": [],
                "store_extend": [], "start_type": 1, "end_type": 3, "cat_id": ["152", "233"], "seckill_type": 1,
                "title": title, "supplier_id": 30303, "sort": sort, "admin_name": 271, "content": "<p>水电费水电费</p>",
                "long_thumb": "https://mmtcdn.jzwp.cn/1657676111705.jpg", "seckill_flag": 0, "is_coupon_convert": 0,
                "cat_id1": "152", "cat_id2": "233", "cat_id3": 0, "thumb": "https://mmtcdn.jzwp.cn/1657676104275.jpg",
                "imgs": ["https://mmtcdn.jzwp.cn/1657676107415.jpg"], "type_id": 5, "type": 5, "attr_datas": [
                {"sku_sn": "null", "sku_id": 0, "goods_attr_ids": "22,19", "incr_stock": "100", "market_price": "300",
                 "storage_cost": "10", "clear_price": "40", "shop_price": "250", "vip_price": "200",
                 "cost_price": "null",
                 "price2": "null", "fee1": "null", "fee2": "null", "fee3": "null", "fee4": "null", "fee5": "null",
                 "fee6": "null",
                 "fee7": "null", "fee11": "null", "fee12": "null", "fee13": "null"}],
                "sku_imgs": {"22": {"thumb": ["https://mmtcdn.jzwp.cn/1657676095386.jpg"]}}, "params": [],
                "goods_id": goods_id, "supplier_type": 0}
        p = session.post(url=url, json=data)
        print(p.json()['message'])


def add_activit(session):
    q = get_goods(session, 600)
    for i in range(60):
        goods_list = []
        for x in range(random.randint(1, 10)):
            goods_list.append(q.get())
        url = "http://mmt.dev.jzwp.shop/v3/goods-activity/add"
        data = {"start_time": get_now_time(60 * 5 * i), "end_time": get_now_time(60 * 5 * i + 600),
                "status": 1,
                "up_down": 1,
                "goods": goods_list}
        session.post(url=url, json=data)


def get_goods(session, pageSize):
    url = "http://mmt.dev.jzwp.shop/v3/goods-activity/get-goods?pageSize=%s&page=1" % pageSize
    data = {}
    p = session.get(url=url, params=data).json()
    q = queue.Queue()
    for item in p['data']['items']:
        item['goods_id'] = item['id']
        q.put(item)
    return q


def del_activit(session):
    url = "http://mmt.dev.jzwp.shop/v3/goods-activity/list"
    data = {"pageSize": 80, "page": 1}
    p = session.get(url=url, params=data).json()
    for i in p['data']['items']:
        url = "http://mmt.dev.jzwp.shop/v3/goods-activity/del"
        data = {"id": i['id']}
        session.post(url=url, json=data)


if __name__ == '__main__':
    s = login()
    # add_goods(s, 200)
    del_activit(s)
    add_activit(s)
