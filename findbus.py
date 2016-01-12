#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from BeautifulSoup import BeautifulSoup
from socket import error as SocketError

def get_bus(url):
    try:
        html = urllib2.urlopen(url).read()
    except SocketError as e:
        print(url)
        # time.sleep(600)
        # return self.getAllALink(url) #many times maybe stack over flow
   # soup = BeautifulSoup(html)
   # result = soup.find(html)
   # print(soup)
    try:
        html = urllib2.urlopen('http://njbus.zhihui.cc/njgjc/webapp.do?method=chooseLine')
    except SocketError as e:
        print('choice line')

    try:
        html = urllib2.urlopen('http://njbus.zhihui.cc/njgjc/webapp.do?method=chooseStation&updownId=68')
    except SocketError as e:
        print('choice station')

    try:
        html = urllib2.urlopen(url).read()
    except SocketError as e:
        print('get data')

    soup = BeautifulSoup(html)
    print(soup)
url = 'http://njbus.zhihui.cc/njgjc/webapp.do?method=snapshot&stId=5192&stName=江苏软件园&stStopLevel=11'

get_bus(url)


