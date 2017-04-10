#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = login
#author = tangtao
#time   = 2017/4/7 10:43
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
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


def get_token():
    payload = {'username': 'root', 'password': 'a1812869b7af699352f3cb8b9403a8ef'}
    res = requests.post("https://192.168.1.106:4433/#index", json=payload)
    print res.text


if __name__ == '__main__':
    get_token()
