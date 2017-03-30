#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = wrong_statistics_by_judge
#author = tangtao
#time   = 2017/3/30 15:38
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

from get_info_from_163.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def statics_location_log(timestamp):
    """
    从location_log中某个采集失败了多少次并且写入到指定的文件中
    :param timestamp: 
    :return: 
    """
    filepath = "./judge/location_log/" + timestamp
    f = open(filepath)
    x = open(filepath + "-statistics", 'w')
    info = f.read().split('***************************************')
    account = len(info) - 1
    log.info(u'未采集到的重定向日志有' + str(account) + u'条')
    result = dict()
    for i in range(0, account):
        url = info[i].split()[2]
        if url in result:
            result[url] += 1
        else:
            result[url] = 1

    result = sorted(result.iteritems(), key=lambda times: times[1], reverse=True)  # 根据total_size 从大到小排序
    for url in result:
        log.info(url[0] + '\t' + u'失败次数:' + str(url[1]) + '\n')
        message = url[0] + '\t' + u'失败次数:' + str(url[1]) + '\n'
        x.write(message)
    x.close()


def statics_service_log(timestamp):
    """
    从location_log中某个采集失败了多少次并且写入到指定的文件中
    :param timestamp: 
    :return: 
    """
    filepath = "./judge/service_log/" + timestamp
    f = open(filepath)
    x = open(filepath + "-statistics", 'w')
    info = f.read().split('***************************************')
    account = len(info) - 1
    log.info(u'未采集到的服务日志有' + str(account) + u'条')
    result = dict()
    for i in range(0, account):
        md5 = info[i].split()[2]
        if md5 in result:
            result[md5] += 1
        else:
            result[md5] = 1
    result = sorted(result.iteritems(), key=lambda times: times[1], reverse=True)  # 根据total_size 从大到小排序
    for md5 in result:
        log.info(md5[0] + '\t' + u'失败次数:' + str(md5[1]) + '\n')
        message = md5[0] + '\t' + u'失败次数:' + str(md5[1]) + '\n'
        x.write(message)
    x.close()


def wrong_statistics_log(timestamp):
    """
    错误日志的信息统计
    :param timestamp: 
    :return: 
    """
    statics_service_log(timestamp)
    statics_location_log(timestamp)
