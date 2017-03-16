# -*- coding=utf-8 -*-
import hashlib
import web



class Validate(object):
    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = 'Hacker'
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hash = sha1.hexdigest()
        print "GET Validate Request"
        if hash == signature:
            return echostr
        else:
            return ""

