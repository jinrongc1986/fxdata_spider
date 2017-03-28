#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = test
#author = tangtao
#time   = 2017/3/20 15:25
#Description=sched用法举例
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
import datetime
import time

from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')
import subprocess
import os
#
#
# def loop():
#     driver = webdriver.Chrome()
#     try:
#         driver.get("http://www.lhtangtao.com")
#         driver.maximize_window()
#         time.sleep(100)
#         driver.quit()
#     except:
#         driver.quit()
#
# if __name__ == '__main__':
#     while True:
#         loop()

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')

#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
