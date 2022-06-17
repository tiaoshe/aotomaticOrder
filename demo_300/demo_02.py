# @time 2022/6/10 16:09
# @Author howell
# @File demo_02.PY
# 问题描述：合并两个升序得整数数组A和B，形成一个新的数组，新数组也要有序。
# 问题实例：输入A=[1,2,3,4]，B=[2,4,6,8]，输出[1,2,2,3,4,4,6,8]。

def function(list_a, list_b):
    list_new = []
    i, j = 0, 0
    while len(list_new) < len(list_a) + len(list_b):
        if i < len(list_a) - 1 and j < len(list_b) - 1:
            if list_a[i] > list_b[j]:
                list_new.append(list_b[j])
                if j < len(list_b) - 1:
                    j += 1
            else:
                list_new.append(list_a[i])
                if i < len(list_a) - 1:
                    i += 1
        else:
            if i == len(list_a) - 1:
                if list_a[i] > list_b[j]:
                    list_new.append(list_b[j])
                    if j < len(list_b) - 1:
                        j += 1
                else:
                    list_new.append(list_a[i])
                    list_new.extend(list_b[j:])
                    j = len(list_b)
            else:
                if list_a[i] > list_b[j]:
                    list_new.append(list_b[j])
                    list_new.extend(list_a[i:])
                    i = len(list_a)
                else:
                    list_new.append(list_a[i])
                    if i < len(list_a) - 1:
                        i += 1
    print(list_new)


# 问题总结  在判断逻辑的时候遗漏边界值的添加
# 答案总结  运用三个循环 先比较完一个列表，再将多的列表循环加到最终列表中
# extend 方法加排序 实现相同算法

if __name__ == '__main__':
    b = [1, 2, 2, 3, 4, 6, 8, 9, 10, 11, 12]
    a = [2, 5, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    function(a, b)
