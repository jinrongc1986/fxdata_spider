#!/usr/bin/python2.7
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
import os

basedir = os.path.dirname(os.getcwd())
sys.path.append(basedir)  # 添加路径，方便在linux下使用
from curl_simulate.http.kind_info import calculate_kind
from curl_simulate.http.get_cache import get_all_cache, get_mobile_cache, get_http_cache
from curl_simulate.tools.connect_Linux import connect_linux, modify_linux_config
from curl_simulate.tools.curl import curl_resource_verbose, curl_all, do_curl
from curl_simulate.tools.curl_kind import kind0, kind100
from curl_simulate.tools.del_log import del_all_log
from curl_simulate.tools.log.operation_log import my_log, modify_my_log_file_path
from curl_simulate.tools.resource_list import get_all_hot_list, get_resource_verbose
from curl_simulate.tools.timer import timer_customize, timer_customize_all_kind
from curl_simulate.tools.wrong_statistics_by_judge import wrong_statistics_log, statics_location_log, \
    statics_service_log
import time

reload(sys)
sys.setdefaultencoding('utf-8')


# def main_all(start_time, end_time, host, user, src_pwd, limit, kind_timeline,
#              cds_ip, database_user, database_pwd, cds_pwd):
#     """
#     :param cds_pwd:
#     :param database_pwd:
#     :param database_user:
#     :param cds_ip:
#     :param start_time: 开始时间
#     :param end_time: 结束时间
#     :param host: 执行curl动作的ip
#     :param user: 上述ip的帐号
#     :param src_pwd: 上述ip的密码
#     :param limit: curl每种资源的个数
#     :param kind_timeline: 每个kind中上下部分的时间差
#     :return:
#     """
#     modify_linux_config(host, user, src_pwd, cds_ip, database_pwd, database_user, cds_pwd)
#     start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
#     timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
#     filepath = './operation_log/' + timestamp
#     modify_my_log_file_path(filepath)
#     log = my_log()
#     while True:
#         now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 显示现在的时间
#         now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')  # 格式化当前的时间
#         if start_time - now_time < datetime.timedelta(minutes=3):
#             log.info(u'离开始执行的时间只有3分钟，3分钟后准时执行')
#             break
#         else:
#             log.info(u'请耐心等待，离开始的时间还有' + str(start_time - now_time))
#             time.sleep(60)
#     log.info(u'全场关键字 timestamp为：' + timestamp)
#     log.info(u'获取全部资源放入到指定的文件夹中')
#     get_all_cache(timestamp, 100)  # 获取全部资源放入到指定的文件夹中
#     log.info(u"现在的时间戳节点为：" + timestamp)
#     log.info(u'开始准备工作，计算每种kind的资源和大小')
#     calculate_kind_all(timestamp)
#     log.info(u'准备工作就绪，现在可以开始进行真正的curl操作')
#     log.info(u'执行time_customize前的当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     timer_customize_all_kind(timestamp, str(start_time), end_time, limit, kind_timeline)
#     log.info(u'执行完成time_customize函数，开始统计函数的执行')
#     get_all_hot_list(timestamp)
#     wrong_statistics_log(timestamp)
#     log.info(u"执行完成")
def curl_class(host, host_user, host_pwd, limit,
               cds_ip, database_user, database_pwd, cds_pwd, src_system='linux', ):
    """
    单线程顺序执行curl动作，从class=0 category=0开始 
    :return: 
    """
    modify_linux_config(host, host_user, host_pwd, cds_ip, database_pwd, database_user, cds_pwd, src_system)
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    curl_log = "./curl_log/curl_log_" + timestamp
    if not os.path.exists('./curl_log'):
        os.mkdir('./curl_log')
    f = open(curl_log, 'w')
    f.close()
    filepath = './operation_log/' + timestamp
    modify_my_log_file_path(filepath)
    get_all_cache(timestamp, 100, cds_ip, database_user, database_pwd, cds_pwd)
    for i in range(5):  # 执行curl的动作，从class=0，category=0 到category=4
        curl_resource_verbose(timestamp, 0, i, limit, src_system, 'iphone', True, True)
    for i in range(3):  # 执行curl的动作，从class=1，category=0 到category=2
        curl_resource_verbose(timestamp, 1, i, limit, src_system, 'iphone', True, True)
    for i in range(20):  # 执行curl的动作，从class=2，category=0 到category=19
        curl_resource_verbose(timestamp, 2, i, limit, src_system, 'iphone', True, True)


def main(start_time, end_time, host, host_user, host_pwd, limit, kind_timeline,
         cds_ip, database_user, database_pwd, cds_pwd, do_all, src_system='linux', resource_ip='empty',
         resource_user='empty',
         resource_pwd='empty', resource_device_pwd='empty'):
    """
    如果src_system为windows 则输入的host_user host_pwd等没有意义，可以不用修改
    :param do_all: 布尔类型 true or false true为在五分钟内执行所有的资源
    :param resource_device_pwd: 获取资源的设备的密码
    :param resource_pwd: 获取资源的设备的数据库密码
    :param resource_user: 获取资源的设备的帐号
    :param resource_ip: 获取资源的设备的ip（默认是cds的ip）
    :param src_system: 所执行curl的设备是属于linux 或者 windows 
    :param cds_pwd: cds设备的密码
    :param database_pwd: cds 数据库的密码
    :param database_user: cds数据库的帐号
    :param cds_ip: cds的ip地址 字符串
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param host: 执行curl动作的ip
    :param host_user: 执行curl动作的设备的帐号
    :param host_pwd: 执行curl动作的设备的密码
    :param limit: curl每种资源的个数
    :param kind_timeline: 每个kind中上下部分的时间差
    :return: 
    """
    modify_linux_config(host, host_user, host_pwd, cds_ip, database_pwd, database_user, cds_pwd,
                        src_system)  # 把所用到的信息写入到配置文件中
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
    if resource_ip == 'empty':
        resource_ip = cds_ip
    if resource_user == 'empty':
        resource_user = database_user
    if resource_pwd == 'empty':
        resource_pwd = database_pwd
    if resource_device_pwd == 'empty':
        resource_device_pwd = cds_pwd
    get_all_cache(timestamp, 100, resource_ip, resource_user, resource_pwd, resource_device_pwd)  # 获取全部资源放入到指定的文件夹中
    log.info(u"现在的时间戳节点为：" + timestamp)
    log.info(u'开始准备工作，计算每种kind的资源和大小')
    # calculate_kind(timestamp, 0, limit)
    i = 0
    while i < 6:
        calculate_kind(timestamp, i, limit)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    log.info(u'准备工作就绪，现在可以开始进行真正的curl操作')
    log.info(u'执行time_customize前的当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    timer_customize(timestamp, str(start_time), end_time, limit, kind_timeline, do_all)
    log.info(u'执行完成time_customize函数，开始统计函数的执行')
    # get_all_hot_list(timestamp)
    # wrong_statistics_log(timestamp)
    if src_system == 'windows':
        os.remove('test666')
    log.info(u"执行完成")


def get_info_from_other_cds(resource_ip, resource_user, resource_pwd,
                            resource_device_pwd, host, host_user, host_pwd, src_system='linux', limit=100):
    """
    从163中获取资源并且执行curl操作，无需进行校验,直接进行curl操作
    :param host_pwd: 
    :param host: 
    :param host_user: 
    :param src_system: 
    :param resource_ip: 
    :param resource_user: 
    :param resource_pwd: 
    :param resource_device_pwd: 
    :param limit: 
    :return: 
    """
    modify_linux_config(host, host_user, host_pwd, resource_ip, resource_pwd, resource_user, '1',
                        src_system)  # 我们只需要在一台设备上执行curl动作而不需要校验等其他动作，因此这里cds_pwd可以随意输入cds信息
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    filepath = './operation_log/' + timestamp
    modify_my_log_file_path(filepath)
    log = my_log()
    log.info(u'全场关键字 timestamp为：' + timestamp)
    log.info(u'获取全部资源放入到指定的文件夹中')
    get_all_cache(timestamp, 1000, resource_ip, resource_user, resource_pwd, resource_device_pwd)  # 获取全部资源放入到指定的文件夹中
    log.info(u'获取全部资源操作完成')
    curl_log = "./curl_log/curl_log_" + timestamp
    if not os.path.exists('./curl_log'):
        os.mkdir('./curl_log')
    f = open(curl_log, 'w')
    f.close()
    log.info(u"下面开始执行kind的操作 以上只是获取信息")
    # kind100(time_stamp=timestamp, limit=limit, src_system=src_system)


if __name__ == '__main__':
    del_all_log()
    # get_info_from_other_cds(resource_ip='20.20.20.2', resource_user='root', resource_device_pwd='123',
    #                         resource_pwd='0rd1230ac', host='192.168.0.56', host_user='root', host_pwd='123',
    #                         src_system='windows')
    main(start_time='2017-05-03 18:15:00', end_time='2017-05-03 20:30:00', host='192.168.0.56', host_user='root',
         host_pwd='123', limit=10, kind_timeline=60, cds_ip='192.168.1.106', database_user='root',
         database_pwd='0rd1230ac', cds_pwd='123', do_all=True, src_system='windows'
         )  # 106为59提供服务，在59上执行curl动作，资源获取来自106上的数据库
    # main('2017-04-26 10:07:00', '2017-04-26 09:00:00', host='192.168.1.109', user='root', src_pwd='FxData!Cds@2016_',
    #      limit=10,
    #      kind_timeline=60,
    #      cds_ip='20.20.20.2', database_user='root', database_pwd='0rd1230ac', cds_pwd="123", do_all=True) # 20.20.20.2为109提供服务，在109上执行curl动作，资源取自20.20.20.2
    # while True:
    #     curl_class(host='192.168.0.56', host_pwd='123', host_user='root', limit=100, cds_ip='192.168.1.106',
    #                database_user='root', database_pwd='0rd1230ac', cds_pwd='123', src_system='windows')
