# @time 2022/6/8 17:31
# @Author howell
# @File demo_01.PY
import math


def change_number():
    data_str = input("请输入需要颠倒的数字：")
    data = 0
    if data_str.isdigit():
        data = int(data_str)
    else:
        print("请输入纯数字")
        change_number()
        return
    number = 10
    return_list = []
    while int(data / number) != 0:
        return_list.append(data % number)
        data = int(data / number)
    return_list.append(data % number)
    return_data = 0
    for i in range(1, len(return_list) + 1):
        if len(return_list) - i != 0:
            return_data += math.pow(10, len(return_list) - i) * return_list[i - 1]
        else:
            return_data += return_list[i - 1]
    print(int(return_data))


if __name__ == '__main__':
    change_number()
