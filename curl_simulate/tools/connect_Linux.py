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

from curl_simulate.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def connect_linux(command, ip, user, pwd):
    """
    输入command在指定ip的linux设备上执行
    :param command: 
    :param ip: 
    :param user: 
    :param pwd: 
    :return: 
    """
    log.info(u'链接' + ip + u'，开始操作')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    log.info(u'IP User Pwd 信息' + ip + '\t' + user + '\t' + pwd)
    ssh.connect(ip, 22, user, pwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    log.info(u'链接' + ip + u'，开始操作' + unicode(command))
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    info1 = stdout.read()
    info2 = stderr.read()
    info = info1 + info2
    log.info(u'链接了linux后执行操作的返回值' + str(info))
    ssh.close()
    return info


def modify_linux_config(host, user, pwd, cds_ip, database_pwd, database_user, cds_pwd, src_system):
    """
    修改config-linux_to_curl里的配置文件
    :param cds_pwd: 
    :param database_user: 
    :param database_pwd: 
    :param cds_ip: 
    :param host: 
    :param user: 
    :param pwd: 
    :return: 
    """
    f = open('./http/config_linux_to_curl', 'w+')
    message = host + ' ' + user + ' ' + pwd + ' ' + cds_ip + ' ' + database_pwd + ' ' + database_user + ' ' + cds_pwd + ' ' + src_system
    f.write(message)
