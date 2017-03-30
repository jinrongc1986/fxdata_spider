#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = assert
#author = tangtao
#time   = 2017/3/27 13:58
#Description=各种校验信息
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
from datetime import datetime
import time

from get_info_from_163.tools.log.operation_log import my_log
from get_info_from_163.tools.mysql_db import get_location_log, get_service_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def assert_location_log(classes, category, url, cache_size, timestamp):
    """
    在执行curl操作后校验 理论上每次执行一次curl操作的话都会产生一个location_kog
    此处我们需要校验的是class category size 以及生成时间是否正确
    :param classes: 
    :param category: 
    :param url: 
    :param cache_size: 
    :param timestamp: 
    :return: 
    """
    info = get_location_log(url)
    log.info(u'从数据库中获取到的资源为：' + unicode(info))
    if info is None:
        log.info(u"没有在重定向日志中找到信息")
        f = open('./judge/location_log/' + timestamp, 'a')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(current_time + ':\n')
        f.write(url + '\n')
        f.write(u'重定向日志中没有此url的信息' + '\n')
        f.write('***************************************\n')
    else:
        log_classes = info[0]
        log_category = info[1]
        log_cache_size = info[2]
        log_create_time = info[3]
        current_time = datetime.now()
        time_lag = abs(current_time - log_create_time)  # 校验时间差，理论上执行完curl之后 会马上生成一个数据 随后时间差不会超过3秒
        time_lag_float = float(str(time_lag).split(':')[2])
        if classes != log_classes or category != log_category or cache_size != log_cache_size or time_lag_float > 10:
            log.warn(unicode(url) + u"重定向日志存在问题")
            is_judge_exist = os.path.exists('./judge')
            if is_judge_exist is True:
                pass
            else:
                os.mkdir('./judge')
            is_dir_exist = os.path.exists('./judge/location_log/')
            if is_dir_exist is True:
                pass
            else:
                os.mkdir('./judge/location_log')
            f = open('./judge/location_log/' + timestamp, 'a')
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(current_time + ':\n')
            f.write(url + '\n')
            f.write(str(u'从数据库中读到的资源：') + '\t' + str(log_classes) + '\t' + str(log_category) + '\t' + str(
                log_cache_size) + '\t' + str(log_create_time) + ':\n')
            f.write(
                str(u'实际curl到的资源：') + '\t' + str(log_classes) + '\t' + str(log_category) + '\t' + str(
                    cache_size) + '\t' + str(time_lag) + ':\n')
            # print '*****************************************'
            if classes != log_classes:
                log.info(u'class与预期不符')
                f.write("cache_size was wrong" + '\n')
            elif category != log_category:
                log.info(u'category与预期不符')
                f.write("category was wrong" + '\n')
            elif cache_size != log_cache_size:
                log.info(u'cache_size与预期不符')
                f.write("cache_size was wrong" + '\n')
            elif time_lag_float > 10:
                log.info(u'create_time与预期不符')
                f.write("create_time was wrong" + '\n')
            f.write('***************************************\n')
        else:
            log.info(unicode(url) + u"重定向日志没有问题")


def assert_service_log(classes, category, cache_size, service_size, md5, timestamp):
    info = get_service_log(classes, md5)
    if info is None:
        log.info(u"没有在重定向日志中找到信息")
        f = open('./judge/service_log/' + timestamp, 'a')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(current_time + ':\n')
        f.write(md5 + '\n')
        f.write(u'重定向日志中没有此md5的信息' + '\n')
        f.write('***************************************\n')
    else:
        log.info(u'从数据库中读取到的资源如下：' + unicode(info))
        log_category = info[0]
        log_cache_size = info[1]
        log_service_size = info[2]
        log_create_time = info[3]
        current_time = datetime.now()
        time_lag = abs(current_time - log_create_time)  # 校验时间差，理论上执行完curl之后 会马上生成一个数据 随后时间差不会超过3秒
        time_lag_float = float(str(time_lag).split(':')[2])
        if cache_size != log_cache_size or category != log_category or service_size != log_service_size or time_lag_float > 10:
            log.warn(unicode(md5) + u"服务日志有问题")
            is_judge_exist = os.path.exists('./judge')
            if is_judge_exist is True:
                pass
            else:
                os.mkdir('./judge')
            is_dir_exist = os.path.exists('./judge/service_log/')
            if is_dir_exist is True:
                pass
            else:
                os.mkdir('./judge/service_log')
            f = open('./judge/service_log/' + timestamp, 'a')
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(current_time + ':\n')
            f.write(md5 + '\n')
            f.write(str(u'从数据库中读到的资源：') + '\t' + str(log_category) + '\t' + str(log_cache_size) + '\t' + str(
                log_service_size) + '\t' + str(log_create_time) + ':\n')
            f.write(
                str(u'实际curl到的资源：') + '\t' + str(category) + '\t' + str(cache_size) + '\t' + str(service_size) + '\t' + str(
                    time_lag) + ':\n')
            if cache_size != log_cache_size:
                log.info(u'cache_size与预期不符')
                f.write("cache_size was wrong" + '\n')
            elif category != log_category:
                log.info(u'category与预期不符')
                f.write("category was wrong" + '\n')
            elif service_size != log_service_size:
                log.info(u'service_size与预期不符')
                f.write("service_size was wrong" + '\n')
            elif time_lag_float > 10:
                log.info(u'create_time与预期不符')
                f.write("create_time was wrong" + '\n')
            f.write('***************************************\n')
        else:
            log.info(unicode(md5) + u"服务日志没有问题")
