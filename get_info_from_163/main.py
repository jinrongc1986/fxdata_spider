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
import sys

from get_info_from_163.http.class_info import calculate_kind
from get_info_from_163.http.http import get_all_cache
from get_info_from_163.tools.log.operation_log import my_log, modify_my_log_file_path
from get_info_from_163.tools.resource_list import get_all_hot_list
from get_info_from_163.tools.timer import timer_customize

reload(sys)
sys.setdefaultencoding('utf-8')


def main_kind():
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    filepath = './operation_log/' + timestamp
    print filepath
    modify_my_log_file_path(filepath)
    log = my_log()
    log.info(u'获取全部资源放入到指定的文件夹中')
    get_all_cache(timestamp)  # 获取全部资源放入到指定的文件夹中
    log.info(u"现在的时间戳节点为：" + timestamp)
    # sys.exit()
    i = 1
    # print u'开始准备工作，计算每种kind的资源和大小'
    log.info(u'开始准备工作，计算每种kind的资源和大小')
    while i < 6:
        calculate_kind(timestamp, i)  # 目前一共五钟kind，把每个kind的cache文件信息存放在kind_info中
        i += 1
    log.info(u'准备工作就绪，现在可以开始进行真正的curl操作')
    log.info(u'当前的时间为' + unicode(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    timer_customize(timestamp, '2017-03-29 18:15:00', '2017-03-29 19:50:00')
    get_all_hot_list(timestamp)


if __name__ == '__main__':
    # modify_my_log_file_path('sj')
    # del_all_log()
    main_kind()
    # curl_resource_verbose("2017-03-28-18-54", 0, 2, 10, 'linux', 'windows')
    # kind2('2017-03-28-16-45')
