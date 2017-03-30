#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = connect_DB
#author = tangtao
#time   = 2017/3/16 15:13
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
import paramiko
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


def connect_linux(command='service iptables stop', ip='192.168.0.59', user='root', pwd='FxData!Cds@2016_'):
    paramiko.util.log_to_file("paramiko.log")
    # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, pwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    info = stdout.read()
    return info


if __name__ == '__main__':
    x = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    print "----------------------------------\n" + x
