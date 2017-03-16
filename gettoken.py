# -*- coding=utf-8 -*-
import requests
import time
import json
import os

os.environ['start_time'] = str(time.time())
start_time = float(os.environ['start_time'])
# appid = 'wx1c97de4c524b412b'
# appSecret = '4857a57c6d377b606b83463f00ef8afe'
appid = os.environ.get('appid')
appSecret = os.environ.get('appSecret')
os.environ['token'] = ''

class Token(object):
    def __init__(self):
        self.start_time = os.environ['start_time']
        self.token = os.environ['token']
        # self.left_time = 0

    def GetInitToken(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(appid,appSecret)
        response = requests.get(url).content
        data = json.loads(response)
        self.token = data['access_token']
        # self.left_time = int(time.time() - self.start_time)
        os.environ['start_time'] = str(time.time())
        # self.start_time = os.environ['start_time']
        os.environ['token'] = self.token
        return self.token

    def CheckValidateToken(self):
        self.__init__()
        if int(time.time() - int(self.start_time)) > 7190:
            self.GetInitToken()
        else:
            return self.token

# if __name__ == '__main__':
#     a = Token()
#     a.GetInitToken()
#     while True:
#         print a.GetInitToken()
#         time.sleep(10)