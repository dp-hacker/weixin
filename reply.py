# -*- coding=utf-8 -*-
import time
from inter import IP
import re

class Msg(object):
    def __init__(self):
        pass
    def send(self):
        pass

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        Msg.__init__(self)
        self.pattern = re.compile(r'^((2[0-4]\d|25[0-5]|[0-1]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[0-1]?\d\d?)$')
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = IP(content) if re.match(self.pattern,content) else content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class EventMsg(Msg):
    def __init__(self,ToUserName,FromUserName):
        Msg.__init__(self)
        self.__dict = dict()
        self.__dict['ToUserName'] = ToUserName
        self.__dict['FromUserName'] = FromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = 'Fuck You'
    def send(self):
        xmldata = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        <FncFlag>0</FuncFlag>
        </xml>
        """
        return xmldata.format(**self.__dict)

if __name__ == '__main__':
    a = EventMsg('1','2')
    print a.send()