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
import datetime
import sys
import threading
import time

from curl_simulate.tools.curl import curl_resource_verbose, curl_all, curl_resource_class
from curl_simulate.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()
f = open('./http/config_linux_to_curl', 'r')
information = f.read().split()
src_system = information[7]


def kind1(time_stamp, limit, time_line, is_sleep=True):
    """
    :return:
    """
    if is_sleep:
        # log.info(u"开始执行kind1的操作")
        # curl_resource_verbose(time_stamp, 0, 0, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=0 成功')
        # curl_resource_verbose(time_stamp, 1, 0, limit, src_system, 'windows', True, True)
        # log.info(u'curl mobilecache category=0 成功')
        # curl_resource_verbose(time_stamp, 2, 1, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=1 成功')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u'等待两分钟后继续执行')
        # time.sleep(time_line)
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u"开始执行kind1的下半部分操作")
        # curl_resource_verbose(time_stamp, 0, 1, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=1 成功')
        # curl_resource_verbose(time_stamp, 2, 2, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=2 成功')
        # curl_resource_verbose(time_stamp, 2, 14, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=14 成功')
        # log.info(u"kind1的操作执行完成")
        log.info(u'开始多线程')
        for i in range(0, 2):
            t1 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 0, limit, src_system, 'windows', True, True))
            t1.start()
            t2 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 1, 0, limit, src_system, 'windows', True, True))
            t2.start()
            t3 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 1, limit, src_system, 'windows', True, True))
            t3.start()
            t4 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 1, limit, src_system, 'windows', True, True))
            t4.start()
            t5 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 2, limit, src_system, 'windows', True, True))
            t5.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
        log.info(u"结束多线程")

    else:
        curl_resource_verbose(time_stamp, 0, 0, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 1, 0, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 1, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 0, 1, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 2, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 14, limit, 'linux', 'windows', False, False)
        message = u"kind1 的curl_log伪造成功"
        log.info(message)


def kind2(time_stamp, limit, time_line, is_sleep=True):
    if is_sleep:
        # log.info(u"开始执行kind2的操作")
        # curl_resource_verbose(time_stamp, 0, 2, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=2 成功')
        # curl_resource_verbose(time_stamp, 1, 1, limit, src_system, 'windows', True, True)
        # log.info(u'curl mobilecache category=1 成功')
        # curl_resource_verbose(time_stamp, 2, 4, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=4 成功')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u'等待两分钟后继续执行')
        # time.sleep(time_line)
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u"开始执行kind2的下半部分操作")
        # curl_resource_verbose(time_stamp, 2, 5, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=5 成功')
        # curl_resource_verbose(time_stamp, 0, 3, limit, src_system, 'iphone', True, True)
        # log.info(u'curl httpcache category=3 成功')
        # curl_resource_verbose(time_stamp, 2, 15, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=15 成功')
        # log.info(u"kind2的操作执行完成")
        log.info(u'开始多线程')
        for i in range(0, 2):
            t1 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 4, limit, src_system, 'windows', True, True))
            t1.start()
            t2 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 2, limit, src_system, 'windows', True, True))
            t2.start()
            t3 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 1, 1, limit, src_system, 'windows', True, True))
            t3.start()
            t4 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 5, limit, src_system, 'windows', True, True))
            t4.start()
            t5 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 3, limit, src_system, 'windows', True, True))
            t5.start()
            t6 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 15, limit, src_system, 'windows', True, True))
            t6.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
        log.info(u"结束多线程")
    else:
        curl_resource_verbose(time_stamp, 2, 4, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 2, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 1, 1, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 5, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 3, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 2, 15, limit, 'linux', 'iphone', False, False)
        message = u"kind2 的curl_log伪造成功"
        log.info(message)


def kind3(time_stamp, limit, time_line, is_sleep=True):
    if is_sleep:
        # log.info(u"开始执行kind3的操作")
        # curl_resource_verbose(time_stamp, 1, 0, limit, src_system, 'windows', True, True)
        # log.info(u'curl mobilecache category=0 成功')
        # curl_resource_verbose(time_stamp, 2, 6, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=6 成功')
        # curl_resource_verbose(time_stamp, 0, 4, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=4 成功')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u'等待两分钟后继续执行')
        # time.sleep(time_line)
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u"开始执行kind3的下半部分操作")
        # curl_resource_verbose(time_stamp, 2, 8, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=8 成功')
        # curl_resource_verbose(time_stamp, 0, 0, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=0 成功')
        # curl_resource_verbose(time_stamp, 2, 16, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=16 成功')
        # log.info(u"kind3的操作执行完成")
        log.info(u'开始多线程')
        for i in range(0, 2):
            t1 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 1, 0, limit, src_system, 'windows', True, True))
            t1.start()
            t2 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 6, limit, src_system, 'windows', True, True))
            t2.start()
            t3 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 4, limit, src_system, 'windows', True, True))
            t3.start()
            t4 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 8, limit, src_system, 'windows', True, True))
            t4.start()
            t5 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 0, limit, src_system, 'windows', True, True))
            t5.start()
            t6 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 16, limit, src_system, 'windows', True, True))
            t6.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
        log.info(u"结束多线程")
    else:
        curl_resource_verbose(time_stamp, 1, 0, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 6, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 0, 4, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 8, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 0, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 16, limit, 'linux', 'windows', False, False)
        message = u"kind3 的curl_log伪造成功"
        log.info(message)


def kind4(time_stamp, limit, time_line, is_sleep=True):
    if is_sleep:
        # log.info(u"开始执行kind4的操作")
        # curl_resource_verbose(time_stamp, 0, 1, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=1 成功')
        # curl_resource_verbose(time_stamp, 1, 1, limit, src_system, 'windows', True, True)
        # log.info(u'curl mobilecache category=1 成功')
        # curl_resource_verbose(time_stamp, 2, 10, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=limit 成功')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u'等待两分钟后继续执行')
        # time.sleep(time_line)
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u"开始执行kind4的下半部分操作")
        # curl_resource_verbose(time_stamp, 2, 11, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=11 成功')
        # curl_resource_verbose(time_stamp, 0, 2, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=2 成功')
        # curl_resource_verbose(time_stamp, 2, 19, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=19 成功')
        # log.info(u"kind4的操作执行完成")
        log.info(u'开始多线程')
        for i in range(0, 2):
            t1 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 1, limit, src_system, 'windows', True, True))
            t1.start()
            t2 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 1, 1, limit, src_system, 'windows', True, True))
            t2.start()
            t3 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 10, limit, src_system, 'windows', True, True))
            t3.start()
            t4 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 11, limit, src_system, 'windows', True, True))
            t4.start()
            t5 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 2, limit, src_system, 'windows', True, True))
            t5.start()
            t6 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 19, limit, src_system, 'windows', True, True))
            t6.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
        log.info(u"结束多线程")
    else:
        curl_resource_verbose(time_stamp, 0, 1, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 1, 1, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 10, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 2, 11, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 2, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 19, limit, 'linux', 'windows', False, False)
        message = u"kind4 的curl_log伪造成功"
        log.info(message)


def kind5(time_stamp, limit, time_line, is_sleep=True):
    if is_sleep:
        # log.info(u"开始执行kind5的操作")
        # curl_resource_verbose(time_stamp, 2, 11, limit, src_system, 'iphone', True, True)
        # log.info(u'curl videocache category=11 成功')
        # curl_resource_verbose(time_stamp, 1, 0, limit, src_system, 'windows', True, True)
        # log.info(u'curl mobilecache category=0 成功')
        # curl_resource_verbose(time_stamp, 0, 3, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=3 成功')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # log.info(u'等待两分钟后继续执行')
        # log.info(u'现在的时间是' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # time.sleep(time_line)
        # log.info(u"开始执行kind5的下半部分操作")
        # curl_resource_verbose(time_stamp, 2, 13, limit, src_system, 'windows', True, True)
        # log.info(u'curl videocache category=13 成功')
        # curl_resource_verbose(time_stamp, 0, 4, limit, src_system, 'windows', True, True)
        # log.info(u'curl httpcache category=4 成功')
        # log.info(u"kind5的操作执行完成")
        log.info(u'开始多线程')
        for i in range(0, 2):
            t1 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 11, limit, src_system, 'windows', True, True))
            t1.start()
            t2 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 1, 0, limit, src_system, 'windows', True, True))
            t2.start()
            t3 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 3, limit, src_system, 'windows', True, True))
            t3.start()
            t4 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 2, 13, limit, src_system, 'windows', True, True))
            t4.start()
            t5 = threading.Thread(target=curl_resource_verbose,
                                  args=(time_stamp, 0, 4, limit, src_system, 'windows', True, True))
            t5.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
        log.info(u"结束多线程")
    else:
        curl_resource_verbose(time_stamp, 2, 11, limit, 'linux', 'iphone', False, False)
        curl_resource_verbose(time_stamp, 1, 0, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 3, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 2, 13, limit, 'linux', 'windows', False, False)
        curl_resource_verbose(time_stamp, 0, 4, limit, 'linux', 'windows', False, False)
        message = u"kind5 的curl_log伪造成功"
        log.info(message)


def kind0(time_stamp, limit, time_line, is_sleep=True):
    if is_sleep:
        threadpool = []
        for t in range(0, 1):  # 如果此处改为2的话 会存现问题
            for i in range(5):
                th = threading.Thread(target=curl_resource_verbose,
                                      args=(time_stamp, 0, i, limit, src_system, 'windows', True, True))
                threadpool.append(th)
            for x in range(3):
                th = threading.Thread(target=curl_resource_verbose,
                                      args=(time_stamp, 1, x, limit, src_system, 'windows', True, True))
                threadpool.append(th)
            for z in range(20):
                th = threading.Thread(target=curl_resource_verbose,
                                      args=(time_stamp, 2, z, limit, src_system, 'windows', True, True))
                threadpool.append(th)
            for ths in threadpool:
                log.info(u" ths.start()所执行的线程为：" + str(ths))
                ths.start()
            for ths in threadpool:
                log.info(u" ths.join()所join的线程为：" + str(ths))
                threading.Thread.join(ths)
            log.info(u'等待两分钟后继续执行')
            time.sleep(time_line)
    else:
        for i in range(0, 5):
            curl_resource_verbose(time_stamp, 0, i, limit, 'linux', 'windows', False, False)
        for y in (0, 2):
            curl_resource_verbose(time_stamp, 1, y, limit, 'linux', 'windows', False, False)
        for x in range(0, 20):
            curl_resource_verbose(time_stamp, 2, x, limit, 'linux', 'windows', False, False)
