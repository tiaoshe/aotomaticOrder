# @time 2021/9/18 14:42
# @Author howell
# @File controlexcel.PY

import xlrd
import xlwt
from xlutils3.copy import copy
import os
import time


class ExcelUtil(object):
    def __init__(self, excelpath, sheetname="Sheet1"):
        self.excelPath = excelpath
        self.data = xlrd.open_workbook(excelpath, formatting_info=True)
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

    def get_user_data(self):
        print(self.table.row_values(3))

    def write_data_mubiao(self, row, num=11, info="无数据"):
        self.worksheet.write(row, num, info)
        self.workbook.save(self.excelPath)

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
            try:
                self.workbook.save(self.excelPath)
            except Exception as err:
                print(err)
                new_path = self.new_work_excel()
                ExcelUtil(new_path).write_response_data(items)
        else:
            print("传入列表为空,不写入表格")
            return

    def write_start(self):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
        self.worksheet.write(self.rowNum + 1, 1, "start:" + str(time_now))
        self.workbook.save(self.excelPath)

    def new_work_excel(self):
        filepath_new_name = os.path.dirname(self.excelPath) + r"\new_report_" + str(int(time.time())) + ".xls"
        wb = xlwt.Workbook(encoding="utf-8")
        wb.add_sheet("Sheet1")
        wb.save(filepath_new_name)
        return filepath_new_name

    def write_smj_reback(self, user_list, reback_list):
        print(reback_list)
        print(user_list)
        if len(user_list) != 0 and len(reback_list) != 0:
            self.worksheet.write(self.rowNum + 1, 1, "订单号")
            run_col = 2
            run_row = 1
            user_list_id = []
            for w in user_list:
                user_list_id.append(w['user_id'])
            for i in user_list:
                self.worksheet.write(self.rowNum + 1, run_col, str(i['user_id']) + "-" + i['user_role'])
                run_col += 1
            for x in reback_list:
                self.worksheet.write(self.rowNum + 1 + run_row, 1, x['order_sn'])
                try:
                    run_col_xd = user_list_id.index(x['user_xd'])
                except:
                    run_col_xd = len(user_list)
                self.worksheet.write(self.rowNum + 1 + run_row, run_col_xd + 2, "下单")
                count_order_info = 0
                for y in x['order_info']:
                    try:
                        run_col_M = user_list_id.index(y['user'])
                    except:
                        run_col_M = len(user_list) + count_order_info
                    self.worksheet.write(self.rowNum + 1 + run_row, run_col_M + 2, y['money'])
                    count_order_info += 1
                run_row += 1
            self.workbook.save(self.excelPath)


if __name__ == '__main__':
    filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\report\\run_report1.xls"
    ExcelUtil(filepath).get_user_data()
