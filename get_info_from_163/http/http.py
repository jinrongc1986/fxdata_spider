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
    str1 = "SELECT uri FROM video_cache WHERE category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    return execute_mysql_fetchall(execute, filepath, category)


def get_mobile_cache_top(category='0', limit='10', filepath='./cache/mobilecache'):
    str1 = "SELECT uri FROM mobile_cache WHERE category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    return execute_mysql_fetchall(execute, filepath, category)


if __name__ == '__main__':
    get_mobile_cache_top('0', '5')
    get_video_cache_top('2', '10')
    get_http_cache_top('3','20')
