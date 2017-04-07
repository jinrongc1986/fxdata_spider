#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = main
#author = tangtao
#time   = 2017/3/17 10:37
#Description=主函数 只需要输入预期的开始时间和预期的结束时间即可
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
from get_info_from_163.http.kind_info import calculate_kind
from get_info_from_163.http.get_cache import get_all_cache, get_mobile_cache, get_http_cache
from get_info_from_163.tools.connect_Linux import connect_linux
from get_info_from_163.tools.curl import curl_resource_verbose
from get_info_from_163.tools.del_log import del_all_log
from get_info_from_163.tools.log.operation_log import my_log, modify_my_log_file_path
from get_info_from_163.tools.resource_list import get_all_hot_list
from get_info_from_163.tools.timer import timer_customize
from get_info_from_163.tools.wrong_statistics_by_judge import wrong_statistics_log, statics_location_log, \
    statics_service_log
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def main_kind(start_time, end_time):
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    filepath = './operation_log/' + timestamp
    modify_my_log_file_path(filepath)
    log = my_log()
    while True:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 显示现在的时间
        now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')  # 格式化当前的时间
        if start_time - now_time < datetime.timedelta(minutes=3):
            log.info(u'离开始执行的时间只有3分钟，3分钟后准时执行')
            break
        else:
            log.info(u'请耐心等待，离开始的时间还有' + str(start_time - now_time))
            time.sleep(60)
    log.info(u'全场关键字 timestamp为：' + timestamp)
    log.info(u'获取全部资源放入到指定的文件夹中')
    get_all_cache(timestamp)  # 获取全部资源放入到指定的文件夹中
    log.info(u"现在的时间戳节点为：" + timestamp)
    i = 1
    log.info(u'开始准备工作，计算每种kind的资源和大小')
    while i < 6:
        calculate_kind(timestamp, i)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    log.info(u'准备工作就绪，现在可以开始进行真正的curl操作')
    log.info(u'执行time_customize前的当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    timer_customize(timestamp, str(start_time), end_time)
    get_all_hot_list(timestamp)
    wrong_statistics_log(timestamp)
    log.info(u"执行完成")


def curl_verbose(times, time_interval):
    """
    循环执行curl某个class的某个category
    :param time_interval: 时间间隔
    :param times: 次数
    :return: 
    """
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    filepath = './operation_log/' + timestamp
    modify_my_log_file_path(filepath)
    log = my_log()
    log.info(u"开始测试")
    log.info(u'全场关键字 timestamp为：' + timestamp)
    log.info(u'获取全部资源放入到指定的文件夹中')
    get_all_cache(timestamp)  # 获取全部资源放入到指定的文件夹中

    log.info(u'执行time_customize前的当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    curl_log = "./curl_log/curl_log_" + timestamp

    i = 1
    log.info(u'开始准备工作，计算每种kind的资源和大小')
    while i < 6:
        calculate_kind(timestamp, i)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    time.sleep(30)
    log.info(u'准备工作就绪，现在可以开始进行真正的curl操作')
    log.info(u'执行time_customize前的当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    init_debug_info = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    f = open(curl_log, 'w')
    log.info(u'debug信息如下所示：' + '\n' + init_debug_info)
    f.write(init_debug_info)
    f.flush()
    f.close()
    for i in range(0, times):
        log.info(u"开始执行第" + str(i) + u'次')
        curl_resource_verbose(timestamp, 1, 0, 10, 'linux', 'windows')
        log.info(u"请再等待" + str(time_interval) + u'秒')
        if i == times:
            pass
        else:
            time.sleep(time_interval)
    end_debug_info = connect_linux('/home/icache/icached debug', '192.168.1.106')
    log.info(u'结束所有的curl操作，debug_info如下所示：' + end_debug_info)
    f = open(curl_log, 'a')
    f.write(end_debug_info)
    get_all_hot_list(timestamp)
    wrong_statistics_log(timestamp)
    log.info(u"执行完成")


if __name__ == '__main__':
    del_all_log()
    # main_kind('2017-04-06 18:20:00', '2017-04-07 08:00:00')
    # curl_verbose(1, 30)
    # curl_resource_verbose('2017-04-05-12-51', 1, 0, 10, 'windows', 'windows')
