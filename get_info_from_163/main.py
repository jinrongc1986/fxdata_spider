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
from get_info_from_163.tools.connect_Linux import connect_linux

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
    print u'执行kind1的上半部分'
    time.sleep(time_line)
    print u'执行kind1的上半部分'
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
    print u'执行kind2的上半部分'
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'iphone')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    time.sleep(time_line)
    print u'执行kind2的下半部分'
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')


def kind3(time_line=125):
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(0, 3, 5, 'linux', 'windows')
    print u'执行kind3的上半部分'
    time.sleep(time_line)
    print u'执行kind3的上半部分'
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')


def kind4(time_line=125):
    curl_resource_verbose(0, 2, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    print u'执行kind4的上半部分'
    time.sleep(time_line)
    print u'执行kind4的上半部分'
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')


def kind5(time_line=125):
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(1, 0, 5, 'linux', 'windows')
    curl_resource_verbose(0, 4, 5, 'linux', 'windows')
    print u'执行kind5的上半部分'
    time.sleep(time_line)
    print u'执行kind5的上半部分'
    curl_resource_verbose(2, 1, 5, 'linux', 'windows')
    curl_resource_verbose(2, 6, 5, 'linux', 'windows')
    curl_resource_verbose(2, 8, 5, 'linux', 'windows')
    curl_resource_verbose(2, 13, 5, 'linux', 'windows')
    curl_resource_verbose(2, 15, 5, 'linux', 'windows')
    curl_resource_verbose(2, 16, 5, 'linux', 'windows')


def timer(expect_start_time='2017-03-21 14:59:00', expect_end_time='2017-03-21 15:08:00'):
    """
    输入期望开始的时间随后每隔五分钟会调用一次
    :param expect_end_time:
    :param expect_start_time:
    :return:
    """
    expect_start_time = datetime.datetime.strptime(expect_start_time, '%Y-%m-%d %H:%M:%S')
    expect_end_time = datetime.datetime.strptime(expect_end_time, '%Y-%m-%d %H:%M:%S')
    node = 1
    init_debug_info = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    f = open('linux_curl_log', 'a')
    f.write(init_debug_info)
    f.flush()
    print u"开始写入日志操作"
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
        # print current_time
        # expect_end_time = expect_end_time - datetime.timedelta(minutes=5)
        print expect_end_time  # 离结束还有多久
        wait_to_end = str(expect_end_time - current_time)
        print wait_to_end  # 离结束还有几秒
        end_minute = int(wait_to_end.split(':')[1])
        end_second = int(wait_to_end.split(':')[2])
        seconds_to_wait_end = end_minute * 60 + end_second
        print seconds_to_wait_end
        if seconds_to_wait_end < 300:
            print str(seconds_to_wait_end) + u'秒后自动退出程序，请查看基础日志'
            time.sleep(seconds_to_wait_end)
            break
        print u"倒计时还没结束"
        wait_time = str(expect_start_time - current_time)
        minute = int(wait_time.split(':')[1])
        seconds = int(wait_time.split(':')[2])
        seconds_to_wait = minute * 60 + seconds
        print u"等待时间为" + str(seconds_to_wait) + u'秒后开始执行'
        time.sleep(seconds_to_wait)
        if node == 1:
            print u'执行kind1'
            kind1()
        elif node == 2:
            print u'执行kind2'
            kind2()
        elif node == 3:
            print u'执行kind3'
            kind3()
        elif node == 4:
            print u'执行kind4'
            kind4()
        elif node == 5:
            print u'执行kind5'
            kind5()
        time_line = datetime.timedelta(minutes=5)
        expect_start_time = expect_start_time + time_line
        node += 1
        if node == 6:
            node = 1

    end_debug_info = connect_linux('/home/icache/icached debug', '192.168.1.106')
    f.write(end_debug_info)
    f.close()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print current_time


if __name__ == '__main__':
    """
    所有的curl指令，因为涉及到相对路径，请都在main这个页面下执行
    """
    # curl_resource_verbose(0, 1, 5, 'linux', 'windows')
    # curl_resource_verbose(0, 1, 5, 'linux', 'windows')
    # get_all_cache()
    timer()
