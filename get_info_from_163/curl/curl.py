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

from get_info_from_163.tools.connect_Linux import connect_linux

reload(sys)
sys.setdefaultencoding('utf-8')




def do_curl(command, system="windows"):
    """
    执行curl命令，目前只支持windows系统和linux系统
    :param command:命令语句
    :param system:linux or windows
    :return:
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if system == 'windows':
        p = os.popen(command)
        info = p.readlines()  # 读取命令行的输出到一个list
        x = open("windows_curl_log", "a")
        x.write(current_time + '\n' + command + '\n')
        for line in info:  # 按行遍历
            with open("windows_curl_log", "a") as f:
                line = line.strip('\r\n')
                json.dump(line, f, ensure_ascii=False)
                f.write('\n')
        x.write("-----------------------------------------------" )
    else:  # 此处编写linux下的命令
        x = open("linux_curl_log", "a")
        x.write(current_time + '\n' + command + '\n')
        # 在此增加读取linux配置的语句
        f = open('./http/config_linux_to_curl', 'r')
        linux_config = f.readline().split()
        ip_add = linux_config[0]
        user = linux_config[1]
        pwd = linux_config[2]
        info = connect_linux(command, ip_add, user, pwd)
        with open("linux_curl_log", "a") as f:
            # line = info.strip('\n')
            f.write(info)
            f.write('\n')
        x.write("-----------------------------------------------" )


def curl_resource_verbose(kind=0, category=0, limit=5, system='windows', ua='iphone'):
    """
    根据class（就是上面的kind，因为class是自带的关键字，故换成kind）和category，还有limit来执行curl动作
    :param ua:
    :param system:
    :param kind:http mobile or video
    :param category:
    :param limit:最近的n个资源
    :return:
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if kind == 0:
        kind_ = 'httpcache'
    elif kind == 1:
        kind_ = 'mobilecache'
    else:
        kind_ = 'videocache'
    filepath = './http/cache/' + kind_ + str(category)  # 找到存放资源地址的文件 随后遍历
    cache_url_list = []
    cache_size_list=[]
    # print filepath
    count = 0  # 计算文件中一共有多少资源 从0开始
    cache_size_total = 0
    for line in open(filepath):
        cache_size = line.split(',')[1]  # 此处获取资源的缓存大小
        line = line.split(',')[0]  # 此处获取的地址
        line = line.replace('["', '')
        line = line.replace('"', '')
        line = line.replace('\n', '')
        cache_url_list.append(line)
        cache_size = int(cache_size.replace(']', ''))
        cache_size_total += cache_size  # 这个文件中所有资源的cache_size的总和
        cache_size_list.append(cache_size)
        count += 1

    if count <= limit:  # 如果出现limit为5而实际只存在两个或三个数据的时候
        limit = count
    i = 0
    while i < limit:
        command1 = 'curl -o test666 -L "'
        command2 = '" '
        command3 = ' --user-agent "' + ua + '"'
        command = command1 + cache_url_list[i] + command2 + command3
        cache_size_total=cache_size_list[i]+cache_size_total
        x = open("cache_size_log", "a")
        x.write(
            current_time + '\n' + ' class= ' + str(kind_) + ' category= ' + str(
                category) + ' cache_size=' + str(cache_size_list[i]) + ' cache_size_total:' + str(
                cache_size_total) + '\n' + '----------------------------------------------------------------------------------' + '\n')
        do_curl(command, system)
        i += 1
    if system == 'windows':
        os.remove('test666')


def curl_resource_class(kind=0, limit=10, system='windows', ua='iphone'):
    """
    根据class的种类来curl所有的这个class下的cache资源（存放于文件中）
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
            # print is_unempty
            # print filepath1
            if is_unempty:  # 如果不为空 则执行读取和curl操作
                curl_resource_verbose(int(kind), category, limit, system, ua)
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
                curl_resource_verbose(int(kind), category, limit, system, ua)
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
                curl_resource_verbose(int(kind), category, limit, system, ua)
            else:  # 如果为空则跳过
                pass
            category += 1


if __name__ == '__main__':
    curl_resource_verbose(0, 1, 5)
    curl_resource_class(0, )
