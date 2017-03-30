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
import datetime
import os
from get_info_from_163.tools.connect_Linux import connect_linux
from get_info_from_163.tools.log.operation_log import my_log
from get_info_from_163.tools.mysql_db import execute_mysql_get_cache_info

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def get_http_cache_top(category="1", limit='10', host='192.168.1.106', user='root',
                       passwd='0rd1230ac', filepath='./http/cache/httpcache'):
    """
    在httpcache这个表里根据category和limit选择uri
    :param user:
    :param passwd:
    :param host:
    :param filepath:
    :param category:种类
    :param limit:限定条数，从根据createtime来排序，取最新的limit条数
    :return:
    """
    str1 = "SELECT uri,cache_size,md5 FROM http_cache WHERE cache_size < 10485760 AND category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    filepath += 'httpcache'
    res = execute_mysql_get_cache_info(execute, filepath, category, host, user, passwd)
    log.info(u'采集到的放入/http/cache_info的http信息为' + str(res))
    return res


def get_video_cache_top(category='1', limit='10', host='192.168.1.106', user='root',
                        passwd='0rd1230ac', filepath='./http/cache/videocache'):
    """
    在videocache这个表里根据category和limit选择uri
    :param passwd:
    :param user:
    :param host:
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    str1 = "SELECT uri,cache_size,md5 FROM video_cache WHERE cache_size < 10485760 AND category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    filepath += 'videocache'
    res = execute_mysql_get_cache_info(execute, filepath, category, host, user, passwd)
    log.info(u'采集到的放入/http/cache_info的video信息为' + str(res))
    return res


def get_mobile_cache_top(category='0', limit='10', host='192.168.1.106', user='root',
                         passwd='0rd1230ac', filepath='./http/cache/mobilecache'):
    """
    在mobilecache这个表里根据category和limit选择uri
    :param passwd:
    :param user:
    :param host:
    :param category:
    :param limit:
    :param filepath:
    :return:
    """
    str1 = "SELECT uri,cache_size, md5  FROM mobile_cache WHERE cache_size < 10485760 AND category="
    str2 = " ORDER BY create_time DESC LIMIT "
    execute = str1 + category + str2 + limit
    # print execute
    filepath += 'mobilecache'
    res = execute_mysql_get_cache_info(execute, filepath, category, host, user, passwd)
    log.info(u'采集到的放入/http/cache_info的mobile信息为' + str(res))
    return res


def get_all_cache(current_time, limit=100, host='192.168.1.106', user='root', passwd='0rd1230ac'):
    """
    获取全部种类的资源
    class=0 时 category有0--4
    class=1 时 category有0--2
    class=2 时 category有0--19
    :param current_time:
    :param limit:
    :param host:
    :param user:
    :param passwd:
    :return:
    """
    connect_linux('service iptables stop', '192.168.1.106')  # 初始化 免得数据库无法连上（执行关闭防火墙的操作）
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
    kind = 0
    while kind < 5:
        get_http_cache_top(str(kind), str(limit), host, user, passwd, filepath)
        kind += 1
    kind = 0
    while kind < 3:
        get_mobile_cache_top(str(kind), str(limit), host, user, passwd, filepath)
        kind += 1
    kind = 0
    while kind < 20:
        get_video_cache_top(str(kind), str(limit), host, user, passwd, filepath)
        kind += 1


if __name__ == '__main__':
    pass
