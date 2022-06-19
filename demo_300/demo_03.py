def change_str(str, offset):
    str_list = list(str)
    str1 = str_list[:offset]
    str2 = str_list[offset:]
    new_list = str2 + str1
    return new_list


# new_list2 = str2.extend(str1)  返回 None
# extend是在原来的字符串上面修改不会有返回值 所以返回None
# 书中答案看不懂，似乎是没有什么道理的算法
if __name__ == '__main__':
    str = "我爱中国"
    offset = 2
    print(change_str(str, offset))
