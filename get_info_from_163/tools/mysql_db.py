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
    cur.close()
    conn.commit()
    conn.close()
    return results


if __name__ == '__main__':
    execute_mysql("SELECT cache_size FROM http_cache WHERE uri='http://officecdn.microsoft.com/pr/64256afe-f5d9-4f86-8936-8840a6a4f5be/Office/Data/16.0.7870.2024/i642052.cab'")
