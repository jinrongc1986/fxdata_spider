#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = modify_iptaboles
#author = tangtao
#time   = 2017/5/5 10:53
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

from curl_simulate.tools.connect_Linux import connect_linux

reload(sys)
sys.setdefaultencoding('utf-8')


def modify_iptables(cds_ip, cds_user, cds_pwd):
    """
    修改防火墙配置，因为初始的情况下在防火墙中3306这个端口是不能使用的
    :param cds_ip: 
    :param cds_user: 
    :param cds_pwd: 
    :return: 
    """
    iptables = "cat /etc/icache/iptables"
    cmd = "-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT"
    cmd2 = "sed -i '15i -A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/icache/iptables"
    info = connect_linux(iptables, cds_ip, cds_user, cds_pwd)
    if cmd not in info:
        connect_linux(cmd2, cds_ip, cds_user, cds_pwd)
        iptable_restart = 'service iptables restart'
        connect_linux(iptable_restart, cds_ip, cds_user, cds_pwd)
        time.sleep(5)
