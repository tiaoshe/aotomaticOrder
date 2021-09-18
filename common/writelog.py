# @time 2021/9/18 14:32
# @Author howell
# @File writeLog.PY
import time
import os


class WriteLog(object):
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            # 获取conf文件中config.ini文件的路径
            self.filepath = os.path.abspath(
                os.path.join(os.path.dirname('__file__'), os.path.pardir, 'report', 'log.txt'))

    def write_str(self, content):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
        temp_content = time_now + str(content)
        with open(self.filepath, 'a', encoding="utf-8") as temp:
            temp.write(temp_content + '\n')


if __name__ == '__main__':
    WriteLog().write_str(content="你好呀1")
