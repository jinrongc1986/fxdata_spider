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


def modify_linux_config(host, user, pwd, cds_ip, database_pwd, database_user, cds_pwd, src_system, need_assert):
    """
    修改config-linux_to_curl里的配置文件
    我们以 在106上读取数据库资源，59上执行curl动作为例子 对下面的参数进行说明
    :param src_system: 59上的系统，此处输入linux，如果是56（本人的pc）则此处请输入windows
    :param cds_pwd: 106的root帐号的密码，不是123就是FxData!Cds@2016_ 
    :param database_user: 106的数据库的帐号 一般是root
    :param database_pwd: 106的数据库的密码，一般是0rd1230ac
    :param cds_ip: 106的ip地址
    :param host: 执行curl动作的ip 此处是59
    :param user: 如果host是linux系统的话，则此处需要输入的是这台设备ssh的帐号，一般是root
    :param pwd: 如果host是linux系统的话，则此处需要输入的是这台设备ssh的密码，一般不是123就是FxData!Cds@2016_ 
    :return: 
    """
    f = open('./http/config_linux_to_curl', 'w+')
    message = host + ' ' + user + ' ' + pwd + ' ' + cds_ip + ' ' + database_pwd + ' ' + database_user + ' ' + cds_pwd + ' ' + src_system + ' ' + str(
        need_assert)
    f.write(message)
