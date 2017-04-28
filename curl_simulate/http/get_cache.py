#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = http
#author = tangtao
#time   = 2017/3/15 14:42
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
import os

from curl_simulate.tools import init_config_file
from curl_simulate.tools.connect_Linux import connect_linux
from curl_simulate.tools.log.operation_log import my_log
from curl_simulate.tools.mysql_db import execute_mysql_get_cache_info
import datetime
import time

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def get_http_cache(category, limit, filepath='./http/cache/httpcache'):
    """
    在httpcache这个表里根据category和limit选择uri
    :param filepath:
    :param category:种类
    :param limit:限定条数，从根据createtime来排序，取最新的limit条数
    :return:
    """
    information = init_config_file().read().split()
    host = information[3]
    database_user = information[5]
    database_pwd = information[4]
    str1 = "SELECT uri,cache_size,md5 FROM http_cache WHERE cache_size < 12428800  AND category="
    str2 = " ORDER BY create_time DESC LIMIT "
    str1_5 = " and expires> '"
    str1_6 = "'"
    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    command = str1 + category + str1_5 + current_time + str1_6 + str2 + limit
    filepath += 'httpcache'
    log.info(u'host:'+str(host)+u'database_user:'+database_user+u'database_pwd'+database_pwd)
    res = execute_mysql_get_cache_info(command, filepath, category, host, database_user, database_pwd)
    log.info(u'采集到的放入/http/cache_info的http信息为' + str(res))
    return res


def get_video_cache(category='1', limit='10', filepath='./http/cache/videocache'):
    """
    在videocache这个表里根据category和limit选择uri
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    information = init_config_file().read().split()
    host = information[3]
    database_user = information[5]
    database_pwd = information[4]
    str1 = "SELECT uri,cache_size,md5 FROM video_cache WHERE cache_size < 12428800 AND category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    filepath += 'videocache'
    res = execute_mysql_get_cache_info(execute, filepath, category, host, database_user, database_pwd)
    log.info(u'采集到的放入/http/cache_info的video信息为' + str(res))
    return res


def get_mobile_cache(category='0', limit='10', filepath='./http/cache/mobilecache'):
    """
    在mobilecache这个表里根据category和limit选择uri
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    information = init_config_file().read().split()
    host = information[3]
    database_user = information[5]
    database_pwd = information[4]
    str1 = "SELECT uri,cache_size, md5  FROM mobile_cache WHERE cache_size < 52428800  AND category="
    str1_5 = " and expires> '"
    str1_6 = "'"
    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str1_5 + current_time + str1_6 + str2 + limit
    # print execute
    filepath += 'mobilecache'
    res = execute_mysql_get_cache_info(execute, filepath, category, host, database_user, database_pwd)
    log.info(u'采集到的放入/http/cache_info的mobile信息为' + str(res))
    return res


def get_all_cache(current_time, limit, resource_ip, resource_user, resource_pwd, device_password):
    """
    获取全部种类的资源
    class=0 时 category有0--4
    class=1 时 category有0--2
    class=2 时 category有0--19
    :param device_password: 
    :param resource_pwd: 
    :param resource_user: 
    :param resource_ip: 
    :param current_time:
    :param limit:
    :return:
    """
    log.info(u"host为：" + resource_ip)
    log.info(u"user为：" + resource_user)
    log.info(u"pwd为：" + resource_pwd)
    # connect_linux('service iptables stop', resource_ip, resource_user, device_password)  # 初始化 免得数据库无法连上（执行关闭防火墙的操作）
    log.info(u'连接到数据库成功')
    is_http_cache_exist = os.path.exists('./http/cache_info')
    if is_http_cache_exist is True:
        pass
    else:
        os.mkdir('./http/cache_info')
        log.info(u'创建文件夹./http/cache_info')
    dir_exist = os.path.exists('./http/cache_info/' + str(current_time))
    if dir_exist is True:
        pass
    else:
        os.mkdir('./http/cache_info/' + str(current_time))
    filepath = './http/cache_info/' + str(current_time) + '/'
    category = 0
    while category < 5:
        get_http_cache(str(category), str(limit), filepath=filepath)
        category += 1
    category = 0
    while category < 3:
        get_mobile_cache(str(category), str(limit), filepath=filepath)
        category += 1
    category = 0
    while category < 20:
        get_video_cache(str(category), str(limit), filepath=filepath)
        category += 1
