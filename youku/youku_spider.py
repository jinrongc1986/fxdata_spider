#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = youku_spider
#author = tangtao
#time   = 2017/3/15 10:07
#Description=添加描述信息
#eMail   =tangtao@lhtangtao.com
#git     =lhtangtao
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
import sys
import urllib2
from bs4 import BeautifulSoup
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def get_youku_href():
    """
    获取优酷的剧集的信息
    :return:
    """
    url = 'http://www.youku.com/'
    # list = ['tv', 'movie', 'zy', 'music', 'child']
    url = 'http://movie.youku.com/'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html5lib")
    for info in soup.find_all("a", attrs={'target': "video"}):
        title = info.get('title')
        if title is None:
            pass
        else:
            href = info.get('href')
            # print title + "   " + href
            data = {
                u'标题': title,
                u"网址": href,
            }
            with open('youku.txt', "a+") as f:
                f.write('\n')
                json.dump([data], f, ensure_ascii=False)


if __name__ == '__main__':
    get_youku_href()
