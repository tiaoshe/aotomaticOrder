# @time 2021/9/18 15:09
# @Author howell
# @File utils.PY
import requests
from common.controlconfig import ReadConfig
from common.writelog import WriteLog
import os
import random


class Login(object):
    def __init__(self, host_url, login_api):
        filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'config.ini'))
        self.filepath_write_log = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'report', 'log.txt'))
        # 传入获取配置文件的关键字
        self.host = ReadConfig(filepath).get("URL", host_url)
        self.interface = ReadConfig(filepath).get("interface", login_api)
        self.url = self.host + self.interface
        self.s = requests.Session()
        self.login = login_api

    def login_b(self):
        data = {}
        user = "李杰1"
        data['username'] = user
        data['password'] = "123456"
        response = self.s.post(url=self.url, json=data)
        try:
            self.s.headers = {"Authorization": "Bearer " + response.json()['data']['token']}
            WriteLog(self.filepath_write_log).write_str(content=user + "在B端登录成功")
            return self.s
        except KeyError:
            WriteLog(self.filepath_write_log).write_str(content="登录接口报错")
            print(response.json())

    def login_c(self):
        pass


class GetView(object):
    """
    获取data配置文件中的images和videos
    """

    def __init__(self):
        self.filepath = os.path.abspath(
            os.path.join(os.path.dirname('__file__'), os.path.pardir, os.path.pardir, 'conf', 'data.ini'))

    def get_images(self, number):
        images = []
        for i in range(0, number):
            temp = random.randint(0, 1)
            name = "image" + str(temp)
            image_url = ReadConfig(self.filepath).get("images", name)
            images.append(image_url)
        return images

    def get_video(self, number):
        videos = []
        for i in range(0, number):
            temp = random.randint(0, 1)
            name = "video" + str(temp)
            video_url = ReadConfig(self.filepath).get("videos", name)
            videos.append(video_url)
        return videos


if __name__ == '__main__':
    # Login("host_star_b", "admin_login").login_b()
    print(GetView().get_images(3))
    print(GetView().get_video(3))
