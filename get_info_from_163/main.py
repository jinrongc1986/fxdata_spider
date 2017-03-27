#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = main
#author = tangtao
#time   = 2017/3/17 10:37
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

from get_info_from_163.curl.curl import curl_resource_verbose
from get_info_from_163.http.class_info import calculate_kind
from get_info_from_163.http.http import get_all_cache
from get_info_from_163.tools.resource_list import get_all_hot_list
from get_info_from_163.tools.timer import timer
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    time_stamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    print 'time_stamp:' + time_stamp
    get_all_cache(time_stamp)  # 获取全部资源放入到指定的文件夹中
    i = 1
    print u'开始准备工作，计算每种kind的资源和大小'
    while i < 6:
        calculate_kind(time_stamp, i)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    print u"准备工作就绪 开始进行curl操作"
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 打印当前的时间
    timer(time_stamp, '2017-03-27 14:56:00', '2017-03-27 15:10:00')
    get_all_hot_list(time_stamp)


if __name__ == '__main__':
    # main()
    curl_resource_verbose('2017-03-27-15-08', 2, 16)
