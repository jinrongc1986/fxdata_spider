#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = other
#author = tangtao
#time   = 2017/3/29 15:11
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

from get_info_from_163.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
logger = my_log()
logger.info('info message')
