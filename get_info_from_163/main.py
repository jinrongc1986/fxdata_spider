#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = main
#author = tangtao
#time   = 2017/3/17 10:37
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
import os
import sys
import time
from datetime import date
import datetime

from get_info_from_163.curl.curl import curl_resource_verbose, curl_resource_class
from get_info_from_163.http.http import get_all_cache, get_http_cache_top

reload(sys)
sys.setdefaultencoding('utf-8')


def kind1(time_line=125):
    """
    :return:
    """
    # 第一个五分钟 执行如下操作 下载
    curl_resource_verbose(0, 2, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 15, 5, 'linux', 'iphone')
    time.sleep(time_line)
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')

    """
    curl_resource_verbose(0, 2, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'windows')
    curl_resource_verbose(0, 5, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')
    curl_resource_verbose(2, 14, 5, 'linux', 'windows')
    curl_resource_verbose(2, 15, 5, 'linux', 'windows')
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')
    """


def kind2(time_line=125):
    curl_resource_verbose(2, 14, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'iphone')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    time.sleep(time_line)
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')


def kind3(time_line=125):
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(0, 5, 5, 'linux', 'windows')
    time.sleep(time_line)
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')


def kind4(time_line=125):
    curl_resource_verbose(0, 5, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    time.sleep(time_line)
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')


def kind5(time_line=125):
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'windows')
    time.sleep(time_line)
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')
    curl_resource_verbose(2, 14, 5, 'linux', 'windows')
    curl_resource_verbose(2, 15, 5, 'linux', 'windows')
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')


def timer(expect_time='2017-03-20 17:57:00'):
    """
    输入期望开始的时间随后每隔五分钟会调用一次
    :param expect_time:
    :return:
    """
    expect_time = datetime.datetime.strptime(expect_time, '%Y-%m-%d %H:%M:%S')
    node = 1
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
        wait_time = str(expect_time - current_time)
        minute = int(wait_time.split(':')[1])
        seconds = int(wait_time.split(':')[2])
        seconds_to_wait = minute * 60 + seconds
        time.sleep(seconds_to_wait)
        if node == 1:
            kind1()
        elif node == 2:
            kind2()
        time_line = datetime.timedelta(minutes=5)
        expect_time = expect_time + time_line
        node += 1
        if node == 6:
            node = 1


if __name__ == '__main__':
    """
    所有的curl指令，因为涉及到相对路径，请都在main这个页面下执行
    """

    timer()
