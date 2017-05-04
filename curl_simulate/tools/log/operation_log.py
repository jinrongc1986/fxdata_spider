#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = operation_log
#author = tangtao
#time   = 2017/3/28 18:25
#Description=自定义的日志类
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
import logging
import logging.config
import os
from curl_simulate import total_base_dir


def my_log():
    """
    初始化函数操作
    :return: 
    """
    operation_log_path = os.path.join(total_base_dir, 'operation_log')
    conf_log = os.path.join(total_base_dir, 'tools', 'log', 'logging.conf')
    if not os.path.exists(operation_log_path):
        os.mkdir(operation_log_path)
    logging.config.fileConfig(conf_log)
    logger_name = "example01"
    logger_ = logging.getLogger(logger_name)
    return logger_


def modify_my_log_file_path(filepath):
    """
    修改日志名字，否则会一直覆盖
    :param filepath: 
    :return: 
    """
    operation_log_path = os.path.join(total_base_dir, 'operation_log')
    conf_log = os.path.join(total_base_dir, 'tools', 'log', 'logging.conf')
    is_dir_exist = os.path.exists(operation_log_path)
    if not is_dir_exist:
        os.mkdir(operation_log_path)
    global src
    f = open(conf_log, 'a+')
    lines = f.readlines()
    for line in lines:
        if 'args=(' in line:
            if 'args=(sys.stderr,)' not in line:
                src = line
                f.close()
    f = open(conf_log, 'a+')
    x = f.read()
    des = x.replace(src, "args=('" + filepath + "', 'a')\n")
    f.close()
    f = open(conf_log, 'w+')
    f.write(des)


def del_operation_log(timestamp):
    """
    如果日志大于8mb则删除里面的所有信息，因为此时已经没有意义了，日志只是单纯的用来判断错误程序的
    :param timestamp: 
    :return: 
    """
    filepath = './operation_log/' + timestamp + ''
    file_size = os.path.getsize(filepath) / 1024 / 1024
    if file_size > 8:
        open(filepath, 'w+')
    else:
        log = my_log()
        log.info(u'目前文件大小为：' + unicode(file_size) + u'，请放心使用')
