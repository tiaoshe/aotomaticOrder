class ShowCode(object):

    def howell(self, **kwargs):
        if kwargs:
            temp_data = kwargs
        else:
            temp_data = {'pay_type': 1, 'appName': 'ÁñÃ¢´«Ëµ', 'appVersion': 'v0.1.3', 'systemType': 'mp', 'systemVersion': 'Windows 10 x64', 'deviceId': 'mini app', 'deviceModel': 'microsoft'}
        p = self.worker.post("howell", **temp_data)
        return p

