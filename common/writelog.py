# @time 2021/9/18 14:32
# @Author howell
# @File writeLog.PY
import os, shutil
import time


class WriteLog(object):
    def __init__(self, filepath):
        # 判断文件是否存在，如果存在进行下一步判断，如果不存在则创建新文件
        if os.path.isfile(filepath):
            fsize = os.path.getsize(filepath)
            fsize = fsize / float(1024 * 1024)
            # 判断文件是否大于2.4MB 如果大于 则将文件重新命名移动到history文件夹中
            if fsize < 2.5:
                self.filepath = filepath
            else:
                filepath_new_name = os.path.dirname(filepath) + "\old" + str(int(time.time())) + ".log"
                os.rename(filepath, filepath_new_name)
                oldpos = filepath_new_name
                newpos = os.path.dirname(filepath) + "\history"
                shutil.move(oldpos, newpos)
                file = open(filepath, 'w')
                file.close()
                self.filepath = filepath
        else:
            file = open(filepath, 'w')
            file.close()
            self.filepath = filepath

    def write_str(self, content):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
        temp_content = time_now + str(content)
        with open(self.filepath, 'a', encoding="utf-8") as temp:
            temp.write(temp_content + '\n')


if __name__ == '__main__':
    WriteLog().write_str(content="你好呀1")
