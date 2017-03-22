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
import sys
import time
import datetime

from get_info_from_163.curl.curl import curl_resource_verbose, curl_resource_class
from get_info_from_163.http.class_info import *
from get_info_from_163.http.http import get_all_cache
from get_info_from_163.tools.connect_Linux import connect_linux

reload(sys)
sys.setdefaultencoding('utf-8')


def kind1(is_sleep=True, time_line=115):
    """
    :return:
    """
    # 第一个五分钟 执行如下操作 下载
    print u'执行kind1的上半部分'
    curl_resource_verbose(0, 2, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(2, 15, 10, 'linux', 'iphone')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind1的下半部分'
    curl_resource_verbose(2, 1, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(0, 1, 10, 'linux', 'windows')

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


def kind2(is_sleep=True, time_line=115):
    print u'执行kind2的上半部分'
    curl_resource_verbose(2, 13, 10, 'linux', 'windows')
    curl_resource_verbose(0, 4, 10, 'linux', 'iphone')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind2的下半部分'
    curl_resource_verbose(2, 16, 10, 'linux', 'windows')
    curl_resource_verbose(0, 3, 10, 'linux', 'iphone')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')


def kind3(is_sleep=True, time_line=115):
    print u'执行kind3的上半部分'
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(2, 6, 10, 'linux', 'iphone')
    curl_resource_verbose(0, 3, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind3的下半部分'
    curl_resource_verbose(2, 13, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(0, 4, 10, 'linux', 'windows')


def kind4(is_sleep=True, time_line=115):
    print u'执行kind4的上半部分'
    curl_resource_verbose(0, 2, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(2, 1, 10, 'linux', 'iphone')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind4的下半部分'
    curl_resource_verbose(2, 6, 10, 'linux', 'windows')
    curl_resource_verbose(0, 3, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')


def kind5(is_sleep=True, time_line=115):
    print u'执行kind5的上半部分'
    curl_resource_verbose(2, 8, 10, 'linux', 'iphone')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(0, 4, 10, 'linux', 'windows')
    if is_sleep:
        print u'间隔125秒后再curl'
        time.sleep(time_line)
    print u'执行kind5的下半部分'
    curl_resource_verbose(2, 1, 10, 'linux', 'windows')
    curl_resource_verbose(1, 0, 10, 'linux', 'windows')
    curl_resource_verbose(0, 1, 10, 'linux', 'windows')


def timer(expect_start_time='2017-03-21 17:04:00', expect_end_time='2017-03-21 17:20:00'):
    """
    输入期望开始的时间随后每隔五分钟会调用一次
    :param expect_end_time:
    :param expect_start_time:
    :return:
    """
    expect_start_time = datetime.datetime.strptime(expect_start_time, '%Y-%m-%d %H:%M:%S')
    expect_end_time = datetime.datetime.strptime(expect_end_time, '%Y-%m-%d %H:%M:%S')
    expect_end_time = expect_end_time + datetime.timedelta(minutes=5)
    node = 1
    print u'debug信息如下所示：'
    f = open('linux_curl_log', 'w+')
    f.close()
    init_debug_info = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    f = open('linux_curl_log', 'a')
    f.write(init_debug_info)
    f.flush()
    count_kind1 = 0
    count_kind2 = 0
    count_kind3 = 0
    count_kind4 = 0
    count_kind5 = 0
    print u"开始写入日志操作"
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 显示现在的时间
        current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')  # 格式化当前的时间
        print u'期望结束的时间加上五分钟是：' + str(expect_end_time)  # 离结束还有多久
        wait_to_end = str(expect_end_time - current_time)  # 期望结束的时间+5分钟-当前的时间 即剩下多少时间
        print u'离结束的时间还有几分几秒（请自行减去五分钟）：' + str(wait_to_end)  # 离结束还有几分几秒
        end_hour = int(wait_to_end.split(':')[0])
        end_minute = int(wait_to_end.split(':')[1])
        end_second = int(wait_to_end.split(':')[2])
        seconds_to_wait_end = end_hour * 3600 + end_minute * 60 + end_second  # 离跳出循环还有几秒钟
        print u'离结束时间还有几秒：' + str(seconds_to_wait_end)
        if seconds_to_wait_end < 300:
            print u'马上自动退出程序，请查看基础日志'
            break
        else:
            print u"倒计时还没结束"
        wait_time = str(expect_start_time - current_time)
        minute = int(wait_time.split(':')[1])
        seconds = int(wait_time.split(':')[2])
        seconds_to_wait = minute * 60 + seconds
        print u"等待时间为" + str(seconds_to_wait) + u'秒后开始执行'
        time.sleep(seconds_to_wait)
        print u'开始执行kind的curl操作'
        if node == 1:
            print count_kind1
            kind1()
            count_kind1 += 1
        elif node == 2:
            kind2()
            print count_kind2
            count_kind2 += 1
        elif node == 3:
            kind3()
            print count_kind3
            count_kind3 += 1
        elif node == 4:
            kind4()
            print count_kind4
            count_kind4 += 1
        elif node == 5:
            kind5()
            print count_kind5
            count_kind5 += 1
        time_line = datetime.timedelta(minutes=5)  # 每次curl间隔的时间，要求为5分钟
        expect_start_time = expect_start_time + time_line
        print u'下次执行的时间为：' + str(expect_start_time)
        node += 1
        if node == 6:
            node = 1
    end_debug_info = connect_linux('/home/icache/icached debug', '192.168.1.106')
    f.write(end_debug_info)
    f.write('count_kind1:' + str(count_kind1 - 1) + '\n')
    f.write('count_kind2:' + str(count_kind2 - 1) + '\n')
    f.write('count_kind3:' + str(count_kind3 - 1) + '\n')
    f.write('count_kind4:' + str(count_kind4 - 1) + '\n')
    f.write('count_kind5:' + str(count_kind5 - 1) + '\n')
    f.close()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print current_time


def main():
    get_all_cache()  # 获取全部资源放入到指定的文件夹中
    i = 1
    print u'开始准备工作，计算每种kind的资源和大小'
    while i < 6:
        calculate_kind(i)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    print u"准备工作就绪 开始进行curl操作"
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # timer('2017-03-22 13:50:00', '2017-03-22 19:25:00')


if __name__ == '__main__':
    """
    所有的curl指令，因为涉及到相对路径，请都在main这个页面下执行
    """
    main()
    # kind_info_verbose()