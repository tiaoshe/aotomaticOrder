# @time 2022/1/20 15:30
# @Author howell
# @File get_data.PY
import requests
import urllib3
import os
import time
from common.controlexcel import ExcelUtil

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
excel_filepath = os.path.abspath(
    os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'run_report.xls'))

headers_temp = '''Host: yapi.jzwp.cn
Connection: keep-alive
sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
sec-ch-ua-platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://yapi.jzwp.cn/project/238/interface/api
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9'''
lines = headers_temp.split("\n")
headers = dict()
for line in lines:
    t = line.split(": ")
    headers[t[0]] = t[1]
url = "https://yapi.jzwp.cn/api/interface/list"
headers[
    'Cookie'] = "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI5NSwiaWF0IjoxNjQyNDcxNzk2LCJleHAiOjE2NDMwNzY1OTZ9.CoweSssws7chmX9IgRKVXoxeVNaoOidWfg1UXjd8zCM; _yapi_uid=295; SERVERID=55bbb075e374cc9f33486712ae8c57b7|%s|1642667511" % str(
    int(time.time()))
data = {"page": 1, "limit": "20", "project_id": "238", }
data_temp = requests.get(url=url, headers=headers, params=data, verify=False)
count = data_temp.json()['data']['count']
data['limit'] = count
data_temp = requests.get(url=url, headers=headers, params=data, verify=False)
response = data_temp.json()['data']['list']
url_detail = "https://yapi.jzwp.cn/api/interface/get"
# ids = list()
# for i in response:
#     interface_id = i['_id']
#     data_detail = {"id": interface_id}
#     detail_temp = requests.get(url=url_detail, headers=headers, params=data_detail, verify=False)
#     query_datas = detail_temp.json()['data']['req_query']
#     data_dict = dict()
#     if len(query_datas):
#         pass
#     else:
#         pass
ExcelUtil(excel_filepath, sheetname="Sheet2").write_response_data(response)
time.sleep(1)
