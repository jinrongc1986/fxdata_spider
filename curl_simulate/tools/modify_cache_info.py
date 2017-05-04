#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = modify_cache_info
#author = tangtao
#time   = 2017/5/4 18:24
#Description=修改获取到的资源文件，删除以数字开头的url
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
import os
import re

from curl_simulate import total_base_dir

reload(sys)
sys.setdefaultencoding('utf-8')


def modify_cache_info(timestamp):
    path = os.path.join(total_base_dir, 'http', "cache_info", timestamp, 'httpcache1')
    with open(path, 'r') as f:
        infos = f.readlines()
        for info in infos:
            print info


if __name__ == '__main__':
    # modify_cache_info('2017-05-04-18-18')


    pattern = re.compile(
        ur'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)')
    str = u'qq1.168.225.255'
    print(pattern.search(str))
