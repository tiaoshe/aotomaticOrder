# @time 2021/9/18 14:42
# @Author howell
# @File controlexcel.PY

import xlrd
from xlutils3.copy import copy
import os
import time


class ExcelUtil(object):
    def __init__(self, excelpath, sheetname="Sheet1"):
        self.excelPath = excelpath
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # # 获取第二行作为key值
        # self.keys = self.table.row_values(1)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        # 将xlrd文件转化成xlwt文件，让文件可写
        self.workbook = copy(self.data)
        # 获得表格对象
        self.worksheet = self.workbook.get_sheet(sheetname)

    def write_data(self, user_list):
        if len(user_list) > 0:
            count = 0
            for user_info in user_list:
                for num in range(0, self.colNum):
                    # temp = user_info[self.keys[num]]
                    self.worksheet.write(self.rowNum + count, num, user_info)
                count += 1
            self.workbook.save(self.excelPath)
            return {'message': 'ok'}
        else:
            return {'message': '用户列表为空'}

    def write_rebade_money(self, user_list, order_list, money_dic, team_relation):
        if len(user_list) > 0 and len(money_dic) > 0:
            # 得到当前行并在当前行指针接着写数据
            for num in range(1, len(user_list) + 1):
                self.worksheet.write(self.rowNum, num, user_list[num - 1])
            # 得到当前行并在当前行指针接着写数据
            for num in range(1, len(team_relation) + 1):
                self.worksheet.write(self.rowNum + 1, num, team_relation[num - 1])
            # self.workbook.save(self.excelPath)
            count = 2
            # 写单列订单号
            for order in order_list:
                self.worksheet.write(self.rowNum + count, 0, order)
                count += 1
            # 将每一行都赋值
            for row in range(0, len(money_dic)):
                order_for_money = money_dic[user_list[row]]
                for num2 in range(0, len(order_for_money)):
                    if order_for_money[user_list[num2]] == 0:
                        continue
                    self.worksheet.write(self.rowNum + row + 2, num2 + 1, order_for_money[user_list[num2]])
                self.workbook.save(self.excelPath)
        else:
            return {'message': '用户列表或返利列表为空'}

    def write_response_data(self, items):
        if len(items) != 0:
            key_list = list(items[0].keys())
            # 得到当前行并在当前行指针接着写数据
            for num in range(1, len(key_list) + 1):
                self.worksheet.write(self.rowNum, num - 1, key_list[num - 1])
            for y in range(0, len(items)):
                count = 0
                for x in key_list:
                    try:
                        data = str(items[y][x])
                    except Exception:
                        data = "None"
                    self.worksheet.write(self.rowNum + y + 1, count, data)
                    count += 1
            self.workbook.save(self.excelPath)
        else:
            print("传入列表为空,不写入表格")
            return

    def write_start(self):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
        self.worksheet.write(self.rowNum + 1, 1, "start:" + str(time_now))
        self.workbook.save(self.excelPath)


if __name__ == '__main__':
    filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/base_data/rebade.xlsx"
    ali = ExcelUtil(filepath)
    user_list = ['10001444', '10001445', '10001446', '10001447', '10001448', '10001449', '10001450']
    money_dic = {
        '10001444': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 5.0,
                     '10001450': 0},
        '10001445': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 5.0,
                     '10001450': 0},
        '10001446': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 5.0,
                     '10001450': 0},
        '10001447': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 5.0,
                     '10001450': 0},
        '10001448': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 0,
                     '10001450': 5.0},
        '10001449': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 0,
                     '10001450': 5.0},
        '10001450': {'10001444': 0, '10001445': 0, '10001446': 0, '10001447': 0, '10001448': 0, '10001449': 0,
                     '10001450': 0}}

    team_relation = ['用户', '用户', 'SVIP', '店长', '用户', '店长', '店长']

    order_list = ['10001444 | 100 | 202108091836403684626', '10001445 | 100 | 202108091836413650549',
                  '10001446 | 90 | 202108091836423919146', '10001447 | 80 | 202108091836433855629',
                  '10001448 | 100 | 202108091836443489566', '10001449 | 80 | 202108091836453541721',
                  '10001450 | 80 | 202108091836464115537']

    ali.write_rebade_money(user_list, order_list, money_dic, team_relation)
