#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = curl
#author = tangtao
#time   = 2017/3/16 10:10
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
import datetime
import json
import os
import sys
from datetime import datetime
import time

from get_info_from_163.tools.connect_Linux import connect_linux
from get_info_from_163.tools.judge import assert_location_log, assert_service_log

reload(sys)
sys.setdefaultencoding('utf-8')


def do_curl(time_stamp, command, system="windows"):
    """
    执行curl命令，目前只支持windows系统和linux系统
    :param time_stamp:
    :param command:命令语句
    :param system:linux or windows
    :return:
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if system == 'windows':
        p = os.popen(command)
        info = p.readlines()  # 读取命令行的输出到一个list
        x1 = open("windows_curl_log", "a")
        x1.write(current_time + '\n' + command + '\n')
        for line in info:  # 按行遍历
            with open("windows_curl_log", "a") as f:
                line = line.strip('\r\n')
                json.dump(line, f, ensure_ascii=False)
                f.write('\n')
                f.flush()
    else:  # 此处编写linux下的命令
        curl_log = "./curl_log/curl_log_" + time_stamp
        x1 = open(curl_log, 'a')
        # x1 = open("linux_curl_log", "a")
        x1.write(current_time + '\n' + command + '\n')
        # 在此增加读取linux配置的语句
        f = open('./http/config_linux_to_curl', 'r')
        linux_config = f.readline().split()
        ip_add = linux_config[0]
        user = linux_config[1]
        pwd = linux_config[2]
        info = connect_linux(command, ip_add, user, pwd)
        with open(curl_log, "a") as f:
            f.write("                  " + info)
            f.write('\n')
            f.flush()


def curl_resource_verbose(timestamp, kind=0, category=0, limit=5, system='windows', ua='iphone'):
    """
    根据class（就是上面的kind，因为class是自带的关键字，故换成kind）和category，还有limit来执行curl动作
    :param timestamp:
    :param ua:
    :param system:
    :param kind:http mobile or video
    :param category:
    :param limit:最近的n个资源
    :return:
    """
    global x
    if kind == 0:
        kind_ = 'httpcache'
    elif kind == 1:
        kind_ = 'mobilecache'
    else:
        kind_ = 'videocache'
    filepath = './http/cache_info/' + timestamp + '/' + kind_ + str(category)  # 找到存放资源地址的文件 随后遍历
    cache_url_list = []
    cache_size_list = []
    md5_list = []
    count = 0  # 计算文件中一共有多少资源 从0开始
    cache_size_total = 0
    for line in open(filepath):
        md5 = line.split(',')[-1]
        md5 = md5.replace('"', '')
        md5 = md5.replace(']', '')
        md5 = md5.replace('\n', '')
        md5 = md5.replace(" ", "")
        cache_size = line.split(',')[-2]  # 此处获取资源的缓存大小
        line = line.split(',')[0]  # 此处获取的地址
        line = line.replace('["', '')
        line = line.replace('"', '')
        line = line.replace('\n', '')
        cache_size = int(cache_size.replace(']', ''))
        cache_size_list.append(cache_size)
        cache_url_list.append(line)
        md5_list.append(md5)
        count += 1
    if count <= limit:  # 如果出现limit为5而实际只存在两个或三个数据的时候
        limit = count
    i = 0
    while i < limit:
        command1 = 'curl -o test666 -L "'
        command2 = '" '
        command3 = ' --user-agent "' + ua + '"'
        url = cache_url_list[i]
        cache_size_each = cache_size_list[i]
        md5_each = md5_list[i]
        command = command1 + url + command2 + command3
        do_curl(timestamp, command, system)  # 执行curl 操作
        assert_location_log(kind, category, url, cache_size_each, timestamp)
        assert_service_log(kind, category, cache_size_each, cache_size_each, md5_each, timestamp)
        cache_size_total = cache_size_list[i] + cache_size_total  # 写入日志的cache_size_total指的是执行了curl的所有资源的大小总和
        curl_log = './curl_log/curl_log_' + timestamp
        x = open(curl_log, 'a')
        x.write('class=' + str(kind_) + ' category=' + str(
            category) + ' cache_size=' + str(cache_size_list[i]) + ' cache_size_total:' + str(
            cache_size_total) + '\n' + '----------------------------------------------------------------------------------')
        x.flush()
        i += 1
    if system == 'windows':
        os.remove('test666')


def curl_resource_class(time_stamp, kind=0, limit=10, system='windows', ua='iphone'):
    """
    根据class的种类来curl所有的这个class下的cache资源（存放于文件中）
    :param time_stamp:
    :param system:
    :param ua:
    :param limit:
    :param kind:
    :return:
    """
    if kind == 0:
        category = 0
        while category < 5:
            filepath1 = './http/cache/httpcache' + str(category)
            f = open(filepath1)
            is_unempty = any(f)
            if is_unempty:  # 如果不为空 则执行读取和curl操作
                curl_resource_verbose(time_stamp, int(kind), category, limit, system, ua)
            else:  # 如果为空则跳过
                pass
            category += 1
    elif kind == 1:
        category = 0
        while category < 3:
            filepath1 = './http/cache/mobilecache' + str(category)
            f = open(filepath1)
            is_unempty = any(f)
            # print is_unempty
            # print filepath1
            if is_unempty:  # 如果不为空 则执行读取和curl操作
                curl_resource_verbose(time_stamp, int(kind), category, limit, system, ua)
            else:  # 如果为空则跳过
                pass
            category += 1
    elif kind == 2:
        category = 0
        while category < 20:
            filepath1 = './http/cache/videocache' + str(category)
            f = open(filepath1)
            is_unempty = any(f)
            # print is_unempty
            if is_unempty:  # 如果不为空 则执行读取和curl操作
                curl_resource_verbose(time_stamp, int(kind), category, limit, system, ua)
            else:  # 如果为空则跳过
                pass
            category += 1
