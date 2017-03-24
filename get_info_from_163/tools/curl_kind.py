#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = curl_kind
#author = tangtao
#time   = 2017/3/24 17:53
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
import time

from get_info_from_163.curl.curl import curl_resource_verbose

reload(sys)
sys.setdefaultencoding('utf-8')


def kind1(time_stamp, is_sleep=True, time_line=115):
    """
    :return:
    """
    # 第一个五分钟 执行如下操作 下载
    print u'执行kind1的上半部分'
    curl_resource_verbose(time_stamp, 0, 2, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 2, 15, 10, 'linux', 'iphone')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind1的下半部分'
    curl_resource_verbose(time_stamp, 2, 1, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 1, 10, 'linux', 'windows')

    """
    curl_resource_verbose(0, 2, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')
    curl_resource_verbose(2, 14, 5, 'linux', 'windows')
    curl_resource_verbose(2, 15, 5, 'linux', 'windows')
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')
    """


def kind2(time_stamp, is_sleep=True, time_line=115):
    print u'执行kind2的上半部分'
    curl_resource_verbose(time_stamp, 2, 13, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 4, 10, 'linux', 'iphone')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind2的下半部分'
    curl_resource_verbose(time_stamp, 2, 16, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 3, 10, 'linux', 'iphone')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')


def kind3(time_stamp, is_sleep=True, time_line=115):
    print u'执行kind3的上半部分'
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 2, 6, 10, 'linux', 'iphone')
    curl_resource_verbose(time_stamp, 0, 3, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind3的下半部分'
    curl_resource_verbose(time_stamp, 2, 13, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 4, 10, 'linux', 'windows')


def kind4(time_stamp, is_sleep=True, time_line=115):
    print u'执行kind4的上半部分'
    curl_resource_verbose(time_stamp, 0, 2, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 2, 1, 10, 'linux', 'iphone')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind4的下半部分'
    curl_resource_verbose(time_stamp, 2, 6, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 3, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')


def kind5(time_stamp, is_sleep=True, time_line=115):
    print u'执行kind5的上半部分'
    curl_resource_verbose(time_stamp, 2, 8, 10, 'linux', 'iphone')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 4, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind5的下半部分'
    curl_resource_verbose(time_stamp, 2, 1, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(time_stamp, 0, 1, 10, 'linux', 'windows')
