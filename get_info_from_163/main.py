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
import os
import sys

from get_info_from_163.curl.curl import curl_resource, curl_resource_class
from get_info_from_163.http.http import get_all_cache, get_http_cache_top

reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    """
    所有的curl指令，因为涉及到相对路径，请都在main这个页面下执行
    """
    # get_all_cache()
    # curl_resource(0, 1, 5)
    curl_resource_class(2)
