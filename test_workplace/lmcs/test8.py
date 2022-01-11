# @time 2021/11/8 10:33
# @Author howell
# @File test8.PY
# coding=utf-8
import threading
import time


def saySorry():
    for i in range(10):
        print("亲爱的，我错了，我能吃饭了吗？")
        time.sleep(2)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()  # 启动线程，即让线程开始执行
