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

import sys
stdout_backup = sys.stdout
log_file = open("message.log", "w")
sys.stdout = log_file
print "Now all print info will be written to message.log"
log_file.close()
sys.stdout = stdout_backup
print "Now this will be presented on screen"