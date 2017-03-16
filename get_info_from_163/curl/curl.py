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
import sys
import os
import json
import datetime
from datetime import datetime

from get_info_from_163.http.connect_Linux import connect_linux

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


def curl(kind=0, category=1, limit=5, system='windows'):
    """
    根据class（就是上面的kind，因为class是自带的关键字，故换成kind）和category，还有limit来执行curl动作
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
    filepath = '../http/cache/' + kind + str(category)
    cache_url_list = []
    for line in open(filepath):
        line = line.replace('["', '')
        line = line.replace('"]', '')
        line = line.replace('\n', '')
        cache_url_list.append(line)
    i = 0
    while i < limit:
        command1 = 'curl -o test -L "'
        command2 = '"'
        command = command1 + cache_url_list[i] + command2
        do_curl(command, system)
        i += 1


if __name__ == '__main__':
    # do_curl(
    #     'curl -o test -L "http://officecdn.microsoft.com/pr/64256afe-f5d9-4f86-8936-8840a6a4f5be/Office/Data/16.0.7870.2013/i640.cab"',
    #     'linux')
    curl(0, 1, 5, 'linux')
