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


def get_youku_href(channel_list_addr):
    """
    获取优酷的剧集的信息
    :return:
    """

    length = len(channel_list_addr)
    i = 1

    url = channel_list_addr[0]
    # print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    # print soup
    for link in soup.find_all('div', 'p-thumb'):
        for info in link.find_all("a", attrs={'target': "video"}):
            title = info.get('title')
            if title is None:
                pass
            else:
                href = info.get('href')
                print title + "   " + href
                data = {
                    u'标题': title,
                    u"网址": href,
                }
                with open('youku.txt', "a+") as f:
                    f.write('\n')
                    json.dump([data], f, ensure_ascii=False)
    while i < length:
        url = channel_list_addr[i]
        # print url
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, "lxml")
        # print soup
        for link in soup.find_all('div', 'v-link'):
            for info in link.find_all("a", attrs={'target': "video"}):
                title = info.get('title')
                if title is None:
                    pass
                else:
                    href = info.get('href')
                    print title + "   " + href
                    data = {
                        u'标题': title,
                        u"网址": href,
                    }
                    with open('youku.txt', "a+") as f:
                        f.write('\n')
                        json.dump([data], f, ensure_ascii=False)
        i += 1


def get_youku_list():
    """
    获取优酷各个频道的地址
    :return:
    """
    channel_list_addr = []
    url = 'http://www.youku.com/'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html5lib")
    for link in soup.find_all('ul', 'top-nav-main'):
        for info in link.find_all('a'):
            channel = info.text
            href = str(info.get('href'))
            # print href
            if 'http://' in href:
                pass
            else:
                href = href.replace('//', 'http://')
            channel_list_addr.append(href)
    return channel_list_addr


if __name__ == '__main__':
    x = get_youku_list()
    get_youku_href(x)
