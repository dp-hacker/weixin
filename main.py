# -*- coding=utf-8 -*-
import web
from validate import Validate
import time
from handle import Handle


urls = ('/wx', 'Handle',

)

def check_token():
    pass


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()