# @time 2022/2/21 11:57
# @Author howell
# @File smjmdc.PY
# 门店端
from test_workplace.smj.smj_utils import *
from common.controlexcel import ExcelUtil
from faker import Faker
import random

faker = Faker(locale='zh_CN')

excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_c_report.xls'))


class InterfaceMDApi(object):
    def __init__(self, request_session):
        self.s = request_session
        self.host = "host_smj_mdc"

    def edit_business_at(self, **kwargs):
        url = get_url(self.host, "edit_business_at")
        data = {"business_at": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_navigation(self, **kwargs):
        url = get_url(self.host, "edit_navigation")
        data = {"longitude": "", "latitude": "", "navigation_name": "", "navigation_address": "", }
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_offline_notice(self, **kwargs):
        url = get_url(self.host, "edit_offline_notice")
        data = {"notice": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_contact_phone(self, **kwargs):
        url = get_url(self.host, "edit_contact_phone")
        data = {"contact_phone": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_shop_imgs(self, **kwargs):
        url = get_url(self.host, "edit_shop_imgs")
        data = {"shop_imgs": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def my_list(self, **kwargs):
        url = get_url(self.host, "my_list")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data'])
        return response

    def order_preview(self, **kwargs):
        url = get_url(self.host, "order_preview")
        data = {"code": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_shop_name(self, **kwargs):
        url = get_url(self.host, "edit_shop_name")
        data = {"name": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def order_use_c(self, **kwargs):
        url = get_url(self.host, "order_use_c")
        data = {"code": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def order_use_list(self, **kwargs):
        url = get_url(self.host, "order_use_list")
        data = {"use_status": "", "start_use_at": "", "end_use_at": "", "use_at_quick": "", "page": "", "pageSize": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def my_goods_offline(self, **kwargs):
        url = get_url(self.host, "my_goods_offline")
        data = {"page": "", "pageSize": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def goods_detail(self, **kwargs):
        url = get_url(self.host, "goods_detail")
        data = {"goods_id": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def order_list_offline(self, **kwargs):
        url = get_url(self.host, "order_list_offline")
        data = {"status": "", "start_use_at": "", "end_use_at": "", "use_at_quick": "", "page": "", "pageSize": "",
                "start_created_at": "", "end_created_at": "", "created_at_quick": "", }
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def order_detail(self, **kwargs):
        url = get_url(self.host, "order_detail")
        data = {"id": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def index_statistics(self, **kwargs):
        url = get_url(self.host, "index_statistics")
        data = {"time_type": "", "start_time": "", "end_time": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def shop_offline_detail(self, **kwargs):
        url = get_url(self.host, "shop_offline_detail")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def shop_offline_detail_setting(self, **kwargs):
        url = get_url(self.host, "shop_offline_detail_setting")
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def shop_account_sub_list(self, **kwargs):
        url = get_url(self.host, "shop_account_sub_list")
        data = {"shop_id": "31347", "page": 2, "pageSize": 10}
        for key, value in kwargs.items():
            data[key] = value
        response = get(self.s, url, **data)
        ExcelUtil(excel_filepath).write_response_data(response['data']['items'])
        return response

    def add_sub_account(self, **kwargs):
        url = get_url(self.host, "add_sub_account")
        data = {"shop_id": "", "name": "", "phone": "", "password": "", "role": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def edit_sub_account(self, **kwargs):
        url = get_url(self.host, "edit_sub_account")
        data = {"shop_id": "", "name": "", "phone": "", "password": "", "role": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response

    def shop_capital_record(self, **kwargs):
        url = get_url(self.host, "shop_capital_record")
        data = {"start_time": "", "end_time": ""}
        for key, value in kwargs.items():
            data[key] = value
        response = post(self.s, url, **data)
        return response


if __name__ == '__main__':
    s = Login().login_md_c("host_smj_mdc", "shop_account_login")
    data_temp = {}
    InterfaceMDApi(s).shop_account_sub_list(**data_temp)
