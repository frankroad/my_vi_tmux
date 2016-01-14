#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import re
import requests
import time
from BeautifulSoup import BeautifulSoup

def get_data(url):
    headers={
    "Host": "njbus.zhihui.cc",
    "User-Agent": "ozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
    }


    req = requests.get(url,headers=headers)
    if 'set-cookie' in req.headers.keys():
        cookie = cookielib.CookieJar()
        handler=urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        response = opener.open(url)
        cookies = ''
        i = 0
        for item in cookie:
            i +=1
            cookies += item.name+'='+item.value+';'
        if i < 3:
            cookies = 'JSESSIONID=CE7CF3393C7D8713B70A065BE73F7076; Hm_lvt_d2feb2a25015d9085e35393fc9143538=1452785844; Hm_lpvt_d2feb2a25015d9085e35393fc9143538=1452785844'
        headers['Cookie'] = cookies   #buffer cookie

        req = requests.get(url,headers=headers)
        print(req.content)


    # req = requests.get(url,headers=headers)

    # print(req.content)



url = 'http://njbus.zhihui.cc/njgjc/webapp.do?method=snapshot&stId=5192&stName=江苏软件园&stStopLevel=11'

get_data(url)