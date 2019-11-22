#!/usr/bin/env Python
# coding=utf-8
# the url structure of website
from handlers.Bilibili import GetAreaListHanlder, LoginHanlder, OpenLiveHandler
from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
    (r'/getAreaList', GetAreaListHanlder),
    (r'/login', LoginHanlder),
    (r'/openLive', OpenLiveHandler),

]
