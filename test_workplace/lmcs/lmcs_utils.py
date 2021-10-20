# @time 2021/9/29 11:18
# @Author howell
# @File lmcs_utils.PY
import requests
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import os
import pymysql
import json


# 链接数据库
def conn_mysql():
    conn = pymysql.connect(host='112.124.11.179', user='admin', passwd='gwUuVyOsjdb2', port=3306, db='lmcs-dev',
                           charset='utf8mb4')
    cur = conn.cursor()  # 生成游标对象
    return conn, cur


class Login(object):
    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.log'))
        self.s = requests.Session()

    def login_b(self, host_url, login_api):
        # 传入获取配置文件的关键字
        host = ReadConfig(self.filepath).get("URL", host_url)
        interface = ReadConfig(self.filepath).get("lmcs_interface", login_api)
        url = host + interface
        data = {}
        user = "李杰1"
        data['username'] = user
        data['password'] = "123456"
        response = self.s.post(url=url, json=data)
        try:
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['accessToken']}
            WriteLog(self.filepath_write_log).write_str(content=user + "在B端登录成功")
            return self.s
        except KeyError:
            WriteLog(self.filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    # 获取用户列表中的token
    def get_token(self, uid):
        conn, cur = conn_mysql()
        sql = "SELECT token FROM `lmcs-dev`.`lmcs_member_access_token` WHERE `uid` = %s" % uid
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                token = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % uid)
        except:
            WriteLog(self.filepath_write_log).write_str(content="get_token数据库发生异常了")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return token

    def login_c(self, uid):
        token = self.get_token(uid)
        if token:
            self.s.headers['auth-key'] = 'Bearer ' + token
            self.s.headers['authorization'] = 'Bearer ' + token
            WriteLog(self.filepath_write_log).write_str(content="用户" + str(uid) + "在C端登录成功")
            return self.s
        else:
            WriteLog(self.filepath_write_log).write_str(content="登录失败")
            return None


class CommonRequest(object):
    def __init__(self, test_to, session=None):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.log'))
        if test_to == "B":
            self.host = ReadConfig(self.filepath).get("URL", "host_lmcs_b")
            self.s = Login().login_b("host_lmcs_b", "admin_login")
        elif test_to == "C":
            self.host = ReadConfig(self.filepath).get("URL", "host_lmcs_c")
            self.s = session

    def get(self, *getargs, **kwargs):
        api = ReadConfig(self.filepath).get("lmcs_interface", *getargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, params=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def post(self, *postargs, **kwargs):
        api = ReadConfig(self.filepath).get("lmcs_interface", *postargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用post方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.post(url=url, json=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def get_download(self, *downloadargs, **kwargs):
        """
        :param downloadargs: 0 传入接口对应的 参数名称
        :param kwargs:
        :return:
        """
        api = ReadConfig(self.filepath).get("lmcs_interface", *downloadargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, stream=True, params=kwargs)
        # 文件名称
        file_to_save = os.path.join(os.getcwd(), downloadargs[1])
        try:
            with open(file_to_save, "wb") as fw:
                fw.write(p.content)
        except PermissionError:
            WriteLog(self.filepath_write_log).write_str(content="文件处于打开状态请手动关闭")
            return "文件处于打开状态请手动关闭"
        return "ok"

    def get_map(self, address):
        get_url = "https://apis.map.qq.com/ws/geocoder/v1/?key=T5OBZ-KJKWI-AFMGR-5GL4Z-6AED6-75BNH&output=jsonp&callback=QQmap"
        data = {"address": address}
        p = requests.get(url=get_url, params=data, verify=True)
        string_temp = p.text[13:][:-1]
        try:
            json_data = json.loads(string_temp)
            return json_data
        except BaseException:
            WriteLog(self.filepath_write_log).write_str(content="发生异常，获取地址返回信息" + p.text)

    def get_sku_id(self, goods_id):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_goods_sku` WHERE `goods_id` = %s" % goods_id
        try:
            q = cur.execute(sql)  # 执行查询语句
            print(q)
            if q != 0:
                sku_id = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % goods_id)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return sku_id

    def get_sku_ids(self, goods_id):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_goods_sku` WHERE `goods_id` = %s" % goods_id
        sku_ids = []
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                ids = cur.fetchall()
                for temp in ids:
                    sku_ids.append(temp[0])
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % goods_id)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return sku_ids

    def get_order_id(self, order_sn):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_order` WHERE `order_sn`=%s" % order_sn
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                order_id = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % order_sn)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return order_id

    def delete_user_relations(self, uid):
        conn, cur = conn_mysql()
        sql = "DELETE FROM `lmcs-dev`.`lmcs_third` WHERE `uid` =%s" % uid
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="数据已经被删除" % uid)
            message = "ok"
        except:
            WriteLog(self.filepath_write_log).write_str(content="删除数据发生错误")
            conn.rollback()  # 如果发生错误则回滚
            message = "None"
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return message

    def get_phone_number(self, phone):
        conn, cur = conn_mysql()
        sql = "SELECT captcha FROM lmcs_common_captcha WHERE `account`=%s" % phone
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                number = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % phone)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return number


class ControlMysql(object):
    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'lmcslog.log'))

    def get_sku_id(self, goods_id):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_goods_sku` WHERE `goods_id` = %s and delflag=0" % goods_id
        sku_id = None
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                sku_id = cur.fetchall()[1][0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % goods_id)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        WriteLog(self.filepath_write_log).write_str(content="sku_id为：" + str(sku_id))
        return sku_id

    def get_sku_ids(self, goods_id):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_goods_sku` WHERE `goods_id` = %s" % goods_id
        sku_ids = []
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                ids = cur.fetchall()
                for temp in ids:
                    sku_ids.append(temp[0])
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % goods_id)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return sku_ids

    def get_order_id(self, order_sn):
        conn, cur = conn_mysql()
        sql = "SELECT id FROM `lmcs-dev`.`lmcs_order` WHERE `order_sn`=%s" % order_sn
        order_id = None
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                order_id = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % order_sn)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return order_id

    def delete_user_relations(self, uid):
        conn, cur = conn_mysql()
        sql = "DELETE FROM `lmcs-dev`.`lmcs_third` WHERE `uid` =%s" % uid
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="数据已经被删除" % uid)
            message = "ok"
        except:
            WriteLog(self.filepath_write_log).write_str(content="删除数据发生错误")
            conn.rollback()  # 如果发生错误则回滚
            message = "None"
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return message

    def get_phone_number(self, phone):
        conn, cur = conn_mysql()
        sql = "SELECT captcha FROM lmcs_common_captcha WHERE `account`=%s" % phone
        number = None
        try:
            q = cur.execute(sql)  # 执行查询语句
            if q != 0:
                number = cur.fetchone()[0]
                conn.commit()  # 提交到数据库执行
            else:
                WriteLog(self.filepath_write_log).write_str(content="查询%s返回数据为空" % phone)
        except:
            WriteLog(self.filepath_write_log).write_str(content="查询用户sku发生错误")
            conn.rollback()  # 如果发生错误则回滚
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接
        return number


if __name__ == '__main__':
    uids = "100004345"
    # address = "四川省成都市武侯区环球中心"
    # s = Login().login_c(uids)
    # p = CommonRequest("C", s).get_map(address)
    # print(p)
    print(CommonRequest("B").get_sku_ids(uids))
