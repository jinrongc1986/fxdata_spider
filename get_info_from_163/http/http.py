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

from get_info_from_163.http.connect_Linux import connect_linux
from get_info_from_163.mysql_db import execute_mysql_fetchall

reload(sys)
sys.setdefaultencoding('utf-8')


def get_http_cache_top(category="1", limit='10', filepath='./cache/httpcache'):
    """
    在httpcache这个表里根据category和limit选择uri
    :param filepath:
    :param category:种类
    :param limit:限定条数，从根据createtime来排序，取最新的limit条数
    :return:
    """
    str1 = "SELECT uri FROM http_cache WHERE category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    return execute_mysql_fetchall(execute, filepath, category)


def get_video_cache_top(category='1', limit='10', filepath='./cache/videocache'):
    """
    在videocache这个表里根据category和limit选择uri
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    str1 = "SELECT uri FROM video_cache WHERE category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    return execute_mysql_fetchall(execute, filepath, category)


def get_mobile_cache_top(category='0', limit='10', filepath='./cache/mobilecache'):
    """
    在mobilecache这个表里根据category和limit选择uri
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    str1 = "SELECT uri FROM mobile_cache WHERE category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    return execute_mysql_fetchall(execute, filepath, category)


def get_all_cache(limit=10):
    """
    获取全部种类的资源
    class=0 时 category有0--4
    class=1 时 category有0--2
    class=2 时 category有0--19
    :return:
    """
    connect_linux()  # 初始化 免得数据库无法连上
    kind = 0
    while kind < 5:
        get_http_cache_top(str(kind), str(limit))
        kind += 1
    kind = 0
    while kind < 3:
        get_mobile_cache_top(str(kind), str(limit))
        kind += 1
    kind = 0
    while kind < 20:
        get_video_cache_top(str(kind), str(limit))
        kind += 1


if __name__ == '__main__':
    get_all_cache()
