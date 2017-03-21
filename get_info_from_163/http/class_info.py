#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = class_info
#author = tangtao
#time   = 2017/3/21 16:41
#Description=根据main函数中的kind来计算每个kind中的数据
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

from get_info_from_163.main import kind1, kind2, kind3, kind4, kind5

reload(sys)
sys.setdefaultencoding('utf-8')


def calculate_kind(kind=1):
    f = open('./linux_curl_log', 'w')
    f.close()
    if kind == 1:
        kind1(False)
    elif kind == 2:
        kind2(False)
    elif kind == 3:
        kind3(False)
    elif kind == 4:
        kind4(False)
    elif kind == 5:
        kind5(False)
    f = open('./linux_curl_log', 'r')
    total_cache_size = 0
    lines = f.readlines()
    x = open('./kind_info/cache_service_kind' + str(kind), "w")
    x.close()
    for line in lines:
        if 'curl' in line:
            url = line.split()[4]
            x = open('./kind_info/cache_service_kind' + str(kind), "a+")
            x.write(url + '  ')
            x.close()
        if 'class' in line:
            cache_size_temp = line.split()[2]
            cache_size = int(cache_size_temp.replace("cache_size=", ''))
            total_cache_size += cache_size
            x = open('./kind_info/cache_service_kind' + str(kind), "a+")
            x.write(str(cache_size) + '\n')
            x.close()
    x = open('./kind_info/cache_service_kind' + str(kind), "a+")
    x.write(str(total_cache_size) + '\n')
    x.write('-------------------------------------')
    x.close()
