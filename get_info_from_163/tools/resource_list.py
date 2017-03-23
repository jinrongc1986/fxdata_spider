#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = resource_list
#author = tangtao
#time   = 2017/3/23 11:08
#Description=资源榜单 从linux_curl_log中取出数据来进行分析操作
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

from get_info_from_163.tools.mysql_db import execute_mysql

reload(sys)
sys.setdefaultencoding('utf-8')


def get_resource_list_by_time():
    """
    根据linux_curl_log来计算出每个url被执行了多少次并且写入日志中
    :return:
    """
    f = open("linux_curl_log", "r")
    x = open("./kind_info/resource_list", 'w')
    result = dict()
    lines = f.readlines()
    for line in lines:
        if 'curl' in line:
            url = line.split()[4].replace('"', '')
            if url in result:
                result[url] += 1
            else:
                result[url] = 1
    for url in result:
        message = url + '\t' + 'times:' + str(result[url]) + '\n'
        x.write(message)
    x.close()


def get_resource_size(url):
    """
    根据资源的url来获取资源的大小用来计算热榜（注意分类）
    :param url:
    :return:class category size组成的列表
    """
    info = []
    command1 = 'SELECT cache_size,category FROM '
    kind1 = 'http_cache'
    kind2 = 'mobile_cache'
    kind3 = 'video_cache'
    command2 = ' WHERE uri like"%'
    command3 = '%"'
    command = command1 + kind1 + command2 + url + command3
    # print command
    res = execute_mysql(command)
    if res is None:
        command = command1 + kind2 + command2 + url + command3
        res = execute_mysql(command)
        if res is None:
            command = command1 + kind3 + command2 + url + command3
            res = execute_mysql(command)
            info.append("video")
            info.append(res[1])
            info.append(res[0])
        else:
            info.append("mobile")
            info.append(res[1])
            info.append(res[0])
    else:
        info.append("httpcache")
        info.append(res[1])
        info.append(res[0])
    return info


def get_resource_verbose():
    """
    获取热点榜单后进行写入文件，可进行下一步分析操作
    :return:
    """
    x = open("./kind_info/resource_list_verbose", 'w')
    f = open("./kind_info/resource_list", 'r')
    lines = f.readlines()
    for line in lines:
        url = line.split()[0]
        times = line.split()[1].replace("times:", "")
        info = get_resource_size(url)
        kind = info[0]
        category = str(info[1])
        cache_size = str(info[2])
        total_size = int(times) * int(cache_size)
        x.write(
            "url:" + url + '\t' + 'class=' + kind + ' category=' + category + ' times:' + times + '\t' + 'cache_size:' + cache_size + '\t' + 'total_size:' + str(
                total_size) + '\n')
    x.close()


def hot_list(kind=0):
    """
    根据curl_log列出热榜资源并写入到文件中
    :param kind: 0表示所有资源
    :return:
    """
    x = open("./kind_info/resource_list_verbose", 'r')
    lines = x.readlines()
    info_all = []  # 把所有的数据写入二维数组 随后开始对二维数组进行操作
    for line in lines:
        info = []
        line = line.split()
        url = line[0].replace("url:", '')
        class_kind = line[1].replace('class=', '')
        category = int(line[2].replace('category=', ''))
        total_size = int(line[5].replace('total_size:', ''))
        info.append(url)
        info.append(class_kind)
        info.append(category)
        info.append(total_size)
        info = tuple(info)
        info_all.append(info)
    # print info_all
    info_all = sorted(info_all, key=lambda totalsize: totalsize[3], reverse=True)  # 根据total_size 从大到小排序
    f = open("./kind_info/hot_resource", 'w')
    i = 0
    while i < len(info_all):
        f.write(str(info_all[i])+'\n')
        i += 1


if __name__ == '__main__':
    pass
