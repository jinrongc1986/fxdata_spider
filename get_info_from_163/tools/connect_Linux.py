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

from get_info_from_163.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def connect_linux(command='service iptables stop', ip='192.168.0.59', user='root', pwd='FxData!Cds@2016_'):
    """
    输入command在指定ip的linux设备上执行
    :param command: 
    :param ip: 
    :param user: 
    :param pwd: 
    :return: 
    """
    log.info(u'链接59，开始操作')
    paramiko.util.log_to_file("paramiko.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, user, pwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    log.info(u'链接59，执行操作：' + unicode(command))
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    info = stdout.read()
    log.info(u'链接了linux后执行操作的返回值'+str(info))
    ssh.close()
    return info


if __name__ == '__main__':
    x = connect_linux(
        ' /home/icache/icached debug', '192.168.1.106')
    print "----------------------------------\n" + x
