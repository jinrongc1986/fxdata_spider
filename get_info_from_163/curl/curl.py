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
        x.write("-----------------------------------------------" + '\n')
    else:  # 此处编写linux下的命令
        x = open("linux_curl_log", "a")
        x.write(current_time + '\n' + command + '\n')
        info = connect_linux(command)
        with open("linux_curl_log", "a") as f:
            # line = info.strip('\n')
            f.write(info)
            f.write('\n')
        x.write("-----------------------------------------------" + '\n')


def curl_resource(kind=0, category=0, limit=5, system='windows', ua='iphone'):
    """
    根据class（就是上面的kind，因为class是自带的关键字，故换成kind）和category，还有limit来执行curl动作
    :param ua:
    :param system:
    :param kind:http mobile or video
    :param category:
    :param limit:最近的n个资源
    :return:
    """
    if kind == 0:
        kind = 'httpcache'
    elif kind == 1:
        kind = 'mobilecache'
    else:
        kind = 'videocache'
    filepath = './http/cache/' + kind + str(category)  # 找到存放资源地址的文件 随后遍历
    cache_url_list = []
    # print filepath
    count = 0
    for line in open(filepath):
        line = line.replace('["', '')
        line = line.replace('"]', '')
        line = line.replace('\n', '')
        cache_url_list.append(line)
        count += 1
    # print cache_url_list
    if count <= limit:  # 如果出现limit为5而实际只存在两个或三个数据的时候
        limit = count
    i = 0
    while i < limit:
        command1 = 'curl -o test666 -L "'
        command2 = '" '
        command3 = ' --user-agent "' + ua + '"'
        command = command1 + cache_url_list[i] + command2 + command3
        # print command
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
                curl_resource(int(kind), category, limit, system, ua)
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
                curl_resource(int(kind), category, limit, system, ua)
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
                curl_resource(int(kind), category, limit, system, ua)
            else:  # 如果为空则跳过
                pass
            category += 1


if __name__ == '__main__':
    # curl_resource(0, 1, 5)
    curl_resource_class()
