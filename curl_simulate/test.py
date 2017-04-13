#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = test
#author = tangtao
#time   = 2017/4/13 17:36
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
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    now_time1 = datetime.datetime.now()  # 显示现在的时间
    time.sleep(1)
    now_time2 = datetime.datetime.now()
    x = now_time1 - now_time2
    y = now_time2 - now_time1
    print x
    print y
    print datetime.timedelta(seconds=0.5)
    if x>datetime.timedelta(seconds=0.5):
        print '1111111111'
