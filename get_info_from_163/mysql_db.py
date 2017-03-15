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


def execute_mysql_fetchall(execute, filepath, category):
    """
    返回一个元组，里面有查询到的所有信息
    :param execute:
    :return:
    """
    conn = init_db()
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


if __name__ == '__main__':
    pass
