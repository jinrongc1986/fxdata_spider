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


def my_log():
    logging.config.fileConfig("./tools/log/logging.conf")
    # create logger
    logger_name = "example01"
    logger_ = logging.getLogger(logger_name)
    return logger_


def modify_my_log_file_path(filepath):
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


if __name__ == '__main__':
    logger = my_log()
    logger.warn('warn message')
