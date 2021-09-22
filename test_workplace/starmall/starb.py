# @time 2021/9/18 15:10
# @Author howell
# @File starb.PY
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
from test_workplace.starmall.utils import Login
import os


class StarUtil(object):
    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'log.txt'))
        self.host = ReadConfig(self.filepath).get("URL", "host_star_b")
        self.s = Login("host_star_b", "admin_login").login_b()

    def get(self, *getargs, **kwargs):
        """
        :return:
        """
        api = ReadConfig(self.filepath).get(*getargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用公共get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, params=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def post(self, *postargs, **kwargs):
        """
        :param postargs: 0 传入接口对应的参数名称
        :param kwargs: 传入data
        :return:
        """
        api = ReadConfig(self.filepath).get(*postargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用公共post方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.post(url=url, json=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p

    def get_download(self, *downloadargs, **kwargs):
        """
        :param downloadargs: 0 传入接口对应的 参数名称
        :param kwargs:
        :return:
        """
        api = ReadConfig(self.filepath).get(*downloadargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用公共get方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.get(url=url, stream=True, params=kwargs)
        # 文件名称
        file_to_save = os.path.join(os.getcwd(), downloadargs[1])
        try:
            with open(file_to_save, "wb") as fw:
                fw.write(p.content)
        except PermissionError:
            WriteLog(self.filepath_write_log).write_str(content="文件处于打开状态请手动关闭")
            return "文件处于打开状态请手动关闭"
        return "ok"

    def put(self, *putargs, **kwargs):
        """
        :param putargs: 0 传入接口对应的参数名称
        :param kwargs: 传入data
        :return:
        """

        api = ReadConfig(self.filepath).get(*putargs)
        WriteLog(self.filepath_write_log).write_str(content="接口：%s|调用公共put方法|参数：%s" % (api, str(kwargs)))
        url = self.host + api
        p = self.s.put(url=url, json=kwargs)
        WriteLog(self.filepath_write_log).write_str(content="返回结果：%s " % p.json())
        return p


if __name__ == '__main__':
    args = ("interface", "get_user_list")
    print(StarUtil().get(*args))
