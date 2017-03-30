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


def my_log():
    is_dir_exist = os.path.exists('./operation_log')
    if is_dir_exist is True:
        pass
    else:
        os.mkdir('./operation_log')
    logging.config.fileConfig("./tools/log/logging.conf")
    logger_name = "example01"
    logger_ = logging.getLogger(logger_name)
    return logger_


def modify_my_log_file_path(filepath):
    is_dir_exist = os.path.exists('./operation_log')
    if is_dir_exist is True:
        pass
    else:
        print "1111111111111111111"
        os.mkdir('./operation_log')

    global src
    f = open("./tools/log/logging.conf", 'a+')
    lines = f.readlines()
    for line in lines:
        if 'args=(' in line:
            if 'args=(sys.stderr,)' not in line:
                src = line
                f.close()
    f = open("./tools/log/logging.conf", 'a+')
    x = f.read()
    des = x.replace(src, "args=('" + filepath + ".log', 'a')\n")
    f.close()
    f = open("./tools/log/logging.conf.", 'w')
    f.write(des)


def del_operation_log(timestamp):
    """
    如果日志大于8mb则删除里面的所有信息，因为此时已经没有意义了，日志只是单纯的用来判断错误程序的
    :param timestamp: 
    :return: 
    """
    filepath = './operation_log/' + timestamp + '.log'
    file_size = os.path.getsize(filepath) / 1024 / 1024
    if file_size > 8:
        open(filepath, 'w')
    else:
        log = my_log()
        log.info(u'目前文件大小为：' + unicode(file_size) + u'，请放心使用')


if __name__ == '__main__':
    logger = my_log()
    logger.warn('warn message')
