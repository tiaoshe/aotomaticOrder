# @time 2022/5/16 10:55
# @Author howell
# @File app.PY

from flask import Flask
from test_workplace.smj.smjb import InterfaceModule
from test_workplace.smj.smjc import InterfaceModuleApi
from test_workplace.smj.smjqishouc import *
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
import pytest, random
import allure
import threading
from faker import Faker

app = Flask(__name__)


@app.route('/add-money')
def add_money():
    uid = 100071
    s = Login().login_b("host_smj_b", "admin_login")
    WorkerB = InterfaceModule(s)
    sc = Login().login_c(uid)
    WorkerC = InterfaceModuleApi(sc)
    user_id = "100082"
    add_or_jian = 2
    # 1为扣减 2 不兑换 3 要兑换
    if add_or_jian == 1:
        type1 = 11
        type2 = 4
        type3 = 22
    else:
        type1 = 1
        type2 = 3
        type3 = 9
    # 加积分 9900
    data2 = {"uid": user_id, "type": type1, "point": 0, "remark": "加扣积分"}
    WorkerB.update_integral_record(**data2)
    # 会员卡加钱 3000
    data3 = {"uid": user_id, "type": type2, "money": 0}
    WorkerB.update_vip_card(**data3)
    # 加余额 299.99
    data1 = {"uid": user_id, "type": type3, "money": 100}
    WorkerB.update_money(**data1)
    if add_or_jian == 3:
        # 查询礼品卡
        sql = "select gift_code,password FROM smj_gift_card where status=0 and money=100;"
        Qd = QueryData().get_data(sql)
        # 绑定礼品卡
        sc = Login().login_c(user_id)
        worker = InterfaceModuleApi(sc)
        data4 = {"shop_id": 31475, "code": Qd[0][0], "password": Qd[0][1], "appName": "圣美家",
                 "appVersion": "v1.0.0", "systemType": "mp", "systemVersion": "Windows 10 x64",
                 "deviceId": "mini app",
                 "deviceModel": "microsoft", "from": 2}
        worker.bind_gift_card(**data4)
    return "ok"


if __name__ == '__main__':
    app.run(host="192.168.0.118")
