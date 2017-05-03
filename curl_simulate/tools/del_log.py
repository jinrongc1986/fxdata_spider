#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = del
#author = tangtao
#time   = 2017/3/27 17:43
#Description=删除没必要的多余的日志文件
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
import os
import shutil
import sys

from curl_simulate.tools.log.operation_log import my_log
import logging

basedir = os.path.dirname(__file__)
sys.path.append(basedir)  # 添加路径，方便在linux下使用

log = my_log()
reload(sys)
sys.setdefaultencoding('utf-8')


def del_dir(*args):
    """
    输入文件夹的地址，随后删除
    :return:
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    dir_path = os.path.join(base_dir, *args)
    is_curl_log_exist = os.path.exists(dir_path)
    if is_curl_log_exist is True:
        shutil.rmtree(dir_path, ignore_errors=True)
    else:
        pass


def del_all_log():
    """
    删除所有的日志文件
    :return:
    """
    del_dir('kind_info')
    del_dir('http', 'cache_info')
    del_dir('curl_log')
    del_dir('judge')
    logging.shutdown()  # 关闭日志文件，否则无法删除下面的日志文件夹
    del_dir('operation_log')


