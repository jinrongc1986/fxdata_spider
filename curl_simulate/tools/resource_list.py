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
from curl_simulate.tools.log.operation_log import my_log
from curl_simulate.tools.mysql_db import execute_mysql

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def get_resource_list_by_time(time_stamp):
    """
    根据linux_curl_log来计算出每个url被执行了多少次并且写入日志中
    :return:
    """
    curl_log = './curl_log/curl_log_' + time_stamp
    f = open(curl_log, "r")
    resource_list_file = './kind_info/' + time_stamp + '/resource_list'
    log.info(resource_list_file + u' 这个文件中包含了资源和执行的次数两个信息')
    x = open(resource_list_file, 'w')
    result = dict()
    lines = f.readlines()
    for line in lines:
        if 'curl --connect-timeout' in line:
            url = line.split()[8].replace('"', '')  # 如果修改了curl指令请记得修改这里
            log.info(u'提取到的url信息为：' + url)
            if url in result:
                result[url] += 1
            else:
                result[url] = 1
    for url in result:
        log.info(u'在' + resource_list_file + u'文件夹中url=' + url + u'被执行了' + str(result[url]) + u'次')
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
    log.info(u'输入uri获取他的cache_size和category:' + command)
    res = execute_mysql(command)
    log.info(u"执行的筛选数据res为：" + unicode(res))
    if res is None:
        command = command1 + kind2 + command2 + url + command3
        res = execute_mysql(command)
        if res is None:
            command = command1 + kind3 + command2 + url + command3
            res = execute_mysql(command)
            info.append("videocache")
            info.append(res[1])
            info.append(res[0])
        else:
            info.append("mobilecache")
            info.append(res[1])
            info.append(res[0])
    else:
        info.append("httpcache")
        info.append(res[1])
        info.append(res[0])
    return info


def get_resource_verbose(time_stamp):
    """
    获取热点榜单后进行写入文件，可进行下一步分析操作 文件名为resource_list_verbose
    :return:
    """
    file_path = './kind_info/' + time_stamp + '/'
    log.info(u"执行get_resource_list_by_time函数")
    get_resource_list_by_time(time_stamp)
    f = open(file_path + "resource_list", 'r')
    lines = f.readlines()
    for line in lines:
        log.info("resource_list" + u'中采集到的line信息为' + line)
        url = line.split()[0]
        times = line.split()[1].replace("times:", "")
        info = get_resource_size(url)
        log.info(u'输入uri获取得到的cache_size和category' + unicode(info))
        kind = info[0]
        category = str(info[1])
        cache_size = str(info[2])
        total_size = int(times) * int(cache_size)
        x = open(file_path + "resource_list_verbose", 'a')
        x.write(
            "url:" + url + '\t' + 'class=' + kind + ' category=' + category + ' times:' + times + '\t' + 'cache_size:' + cache_size + '\t' + 'total_size:' + str(
                total_size) + '\n')
        x.close()
        log.info(u'从resource_list采集到的写入resource_list_verbose信息为：' +
                 "url:" + url + '\t' + 'class=' + kind + ' category=' + category + ' times:' + times + '\t' + 'cache_size:' + cache_size + '\t' + 'total_size:' + str(
            total_size) + '\n')


def hot_list(time_stamp, kind=0):
    """
    根据curl_log列出热榜资源并写入到文件中
    :param time_stamp:
    :param kind: 0表示所有资源
    :return:
    """
    resource_list_verbose_file = './kind_info/' + time_stamp + '/resource_list_verbose'
    log.info(
        u'resource_list_verbose_file(主要内容为包含了URL class category 执行次数，单次缓存大小，总的缓存大小 )\n' + resource_list_verbose_file)
    x = open(resource_list_verbose_file, 'r')
    lines = x.readlines()
    info_all = []  # 把所有的数据写入二维数组 随后开始对二维数组进行操作
    if kind == 0:
        for line in lines:
            log.info(line)
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
        info_all = sorted(info_all, key=lambda totalsize: totalsize[3], reverse=True)  # 根据total_size 从大到小排序
        hot_resource_file = './kind_info/' + time_stamp + '/hot_resource'
        f = open(hot_resource_file, 'w')
        i = 0
        while i < len(info_all):
            f.write(str(info_all[i]) + '\n')
            i += 1
    else:
        if kind == 1:
            kind = 'httpcache'
        elif kind == 2:
            kind = 'mobilecache'
        elif kind == 3:
            kind = 'videocache'
        for line in lines:
            line = line.split()
            class_kind = line[1].replace('class=', '')
            if class_kind == kind:
                info = []
                url = line[0].replace("url:", '')
                category = int(line[2].replace('category=', ''))
                total_size = int(line[5].replace('total_size:', ''))
                info.append(url)
                info.append(class_kind)
                info.append(category)
                info.append(total_size)
                info = tuple(info)
                info_all.append(info)
        info_all = sorted(info_all, key=lambda totalsize: totalsize[3], reverse=True)  # 根据total_size 从大到小排序
        hot_resource_kind_file = './kind_info/' + time_stamp + '/hot_resource_'
        f = open(hot_resource_kind_file + kind, 'w')
        i = 0
        while i < len(info_all):
            f.write(str(info_all[i]) + '\n')
            i += 1


def get_all_hot_list(time_stamp):
    """
    从操作日志中分析出各种热榜（包括三种class以及总榜单）
    :param time_stamp:
    :return:
    """
    log.info(u'从操作日志中分析出各种热榜（包括三种class以及总榜单）')
    get_resource_verbose(time_stamp)
    hot_list(time_stamp)
    hot_list(time_stamp, 1)
    hot_list(time_stamp, 2)
    hot_list(time_stamp, 3)


if __name__ == '__main__':
    pass
