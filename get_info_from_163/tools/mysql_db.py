#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = mysql_db
#author = tangtao
#time   = 2017/3/15 14:46
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
import json
import MySQLdb

from get_info_from_163.tools.connect_Linux import connect_linux

reload(sys)
sys.setdefaultencoding('utf-8')


def init_db(host='192.168.1.106', user='root', passwd='0rd1230ac'):
    """
    请在此处输入数据库的信息
    :return:
    """
    connect = MySQLdb.connect(
        host=host,
        port=3306,
        user=user,
        db='cache',
        charset="utf8",  # 确保没有乱码
        passwd=passwd
    )
    assert isinstance(connect, object)
    return connect


def execute_mysql_get_cache_info(execute, filepath, category, host='192.168.1.106', user='root', passwd='0rd1230ac'):
    """
    返回一个元组，里面有查询到的所有信息
    并且把他写入指定的文件
    :param passwd: 数据库密码
    :param user: 数据库帐号
    :param host: 数据库ip
    :param category:
    :param filepath:
    :param execute:
    :return:
    """
    conn = init_db(host, user, passwd)
    cur = conn.cursor()
    cur.execute(execute)
    results = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    filepath = filepath + category
    open(filepath, "w")
    for uri in results:
        with open(filepath, "a+") as f:
            json.dump(uri, f, ensure_ascii=False)
            f.write('\n')
    return results


def execute_mysql(execute, host='192.168.1.106', user='root', passwd='0rd1230ac'):
    """
    返回数据库查询的单个信息
    :param execute:
    :param host:
    :param user:
    :param passwd:
    :return:
    """
    conn = init_db(host, user, passwd)
    cur = conn.cursor()
    cur.execute(execute)
    results = cur.fetchone()
    # results = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return results


def get_location_log(url):
    """
    根据url获取location资料后，下一步对比
    :param url:
    :return:
    """
    connect_linux('service iptables stop', '192.168.1.106')  # 初始化 免得数据库无法连上（执行关闭防火墙的操作）
    cmd1 = 'SELECT class,category,cache_size FROM location_log WHERE req_uri = "'
    cmd2 = '" ORDER BY create_time DESC'
    cmd = cmd1 + url + cmd2
    return execute_mysql(cmd)


if __name__ == '__main__':
    print get_location_log('http://112.17.6.140/videos/other/20170213/ea/50/e33bf11c06f9534ca29e7aed999c89db.f4v')
