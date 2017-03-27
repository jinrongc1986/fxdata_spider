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

from get_info_from_163.tools.mysql_db import get_location_log, get_service_log

reload(sys)
sys.setdefaultencoding('utf-8')


def assert_location_log(classes, category, url, cache_size, timestamp):
    info = get_location_log(url)
    log_classes = info[0]
    log_category = info[1]
    log_cache_size = info[2]
    if classes != log_classes or category != log_category or cache_size != log_cache_size:
        print u'location_log与预期不符，请查看日志'
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
            log_cache_size) + ':\n')
        f.write(
            str(u'实际curl到的资源：') + '\t' + str(log_classes) + '\t' + str(log_category) + '\t' + str(cache_size) + ':\n')


def assert_service_log(classes, category, cache_size, service_size, md5, timestamp):
    info = get_service_log(classes, md5)
    log_category = info[0]
    log_cache_size = info[1]
    log_service_size = info[2]
    if cache_size != log_cache_size or category != log_category or service_size != log_service_size:
        print u'service_log与预期不符，请查看日志'
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
            log_service_size) + ':\n')
        f.write(
            str(u'实际curl到的资源：') + '\t' + str(category) + '\t' + str(cache_size) + '\t' + str(service_size) + ':\n')
