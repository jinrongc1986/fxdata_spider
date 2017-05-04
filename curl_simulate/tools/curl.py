#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = curl
#author = tangtao
#time   = 2017/3/16 10:10
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
import datetime
import subprocess
import os
import sys
from datetime import datetime
import time

from curl_simulate import total_base_dir
from curl_simulate.tools import init_config_file
from curl_simulate.tools.connect_Linux import connect_linux
from curl_simulate.tools.judge import assert_location_log, assert_service_log
from curl_simulate.tools.log.operation_log import my_log
import time

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def do_curl(time_stamp, command, system, really_do):
    """
    执行curl命令，目前只支持windows系统和linux系统
    :param really_do: 默认是真的要执行curl操作
    :param time_stamp:
    :param command:命令语句
    :param system:linux or windows
    :return:
    """
    linux_config = init_config_file().readline().split()
    src_ip = linux_config[0]
    user = linux_config[1]
    pwd = linux_config[2]
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.info(u'当前时间为：' + unicode(current_time))
    if system == 'windows' or 'linux_self':
        log.info(u'选择的是windows设备执行curl操作' + str(command))
        curl_log = "./curl_log/curl_log_" + time_stamp
        if really_do:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            info = p.stdout.read()
            log.info(u'windows上执行的命令返回值为：' + str(info))
            curl_log = "./curl_log/curl_log_" + time_stamp
            with open(curl_log, "a") as f:
                now_over_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(
                    current_time + '\n' + command + '\n' + "" + info + now_over_time + '\n' + '------------------------------' + '\n')
                f.flush()
        else:
            x1 = open(curl_log, 'a+')
            x1.write(current_time + '\n' + command + '\n')
    elif system == 'linux':  # 此处编写linux下的命令
        log.info(u'选择的是linux设备执行curl操作')
        curl_log = "./curl_log/curl_log_" + time_stamp
        # 在此增加读取linux配置的语句
        log.info(u"linux的信息如下所示：ip address:" + src_ip + ' user:' + user + " password:" + pwd)
        if really_do is True:
            info = connect_linux(command, src_ip, user, pwd)
            log.info(u"执行的命令为" + unicode(command) + u'并且写入到curl_log中')
            log.info(u"获取到的info信息为" + unicode(info) + u'并且写入到curl_log中')
            with open(curl_log, "a") as f:
                now_over_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(
                    current_time + '\n' + command + '\n' + "" + info + now_over_time + '\n' + '------------------------------' + '\n')
                f.flush()
        else:
            x1 = open(curl_log, 'a+')
            x1.write(current_time + '\n' + command + '\n')


def curl_resource_verbose(timestamp, classes, category, limit, system, ua, need_assert,
                          really_do):
    """
    根据class（就是上面的kind，因为class是自带的关键字，故换成kind）和category，还有limit来执行curl动作
    :param really_do: 
    :param need_assert: 
    :param timestamp:
    :param ua:
    :param system:
    :param classes:http mobile or video
    :param category:
    :param limit:最近的n个资源
    :return:
    """

    curl_verbose_start_time = datetime.now()
    log.info(u"curl_resource_verbose函数 开始执行！！！，此时class与category分别为：" + str(classes) + ' ' + str(category))
    global x
    if classes == 0:
        kind_ = 'httpcache'
    elif classes == 1:
        kind_ = 'mobilecache'
    else:
        kind_ = 'videocache'
    filepath = './http/cache_info/' + timestamp + '/' + kind_ + str(category)  # 找到存放资源地址的文件 随后遍历
    log.info(u"打开下面的文件夹，读取里面的内容" + unicode(filepath))
    cache_url_list = []
    cache_size_list = []
    md5_list = []
    count = 0  # 计算文件中一共有多少资源 从0开始
    cache_size_total = 0
    for line in open(filepath):
        md5 = line.split(',')[-1]
        md5 = md5.replace('"', '')
        md5 = md5.replace(']', '')
        md5 = md5.replace('\n', '')
        md5 = md5.replace(" ", "")
        cache_size = line.split(',')[-2]  # 此处获取资源的缓存大小
        line = line.split(',')[0]  # 此处获取的地址
        line = line.replace('["', '')
        line = line.replace('"', '')
        line = line.replace('\n', '')
        cache_size = int(cache_size.replace(']', ''))
        cache_size_list.append(cache_size)
        cache_url_list.append(line)
        md5_list.append(md5)
        count += 1
    log.info(u"从" + unicode(filepath) + u"中，读取md5，资源的缓存大小，url 都放入到数组中" +
             u'其中class和category分别为：' + str(classes) + " " + str(category))
    log.info(u"得到的md5数组：" + unicode(md5_list) + u" url数组：" + unicode(cache_url_list) + u" 缓存大小数组：" + unicode(
        cache_size_list) + u" 资源总数为：" + unicode(count))
    if count <= limit:  # 如果出现limit为5而实际只存在两个或三个数据的时候
        log.info(u"此时limit大于count")
        limit = count
    i = 0
    while i < limit:
        curl_one_start_time = datetime.now()
        command1 = 'curl --connect-timeout 5 -m 10 -o test666 -L "'  # 连接超时时间用 --connect-timeout 参数来指定，数据传输的最大允许时间用 -m 参数来指定。
        command2 = '" '
        command3 = ' --user-agent "' + ua + '"'
        url = cache_url_list[i]
        command = command1 + url + command2 + command3
        try:
            now1 = datetime.now()
            log.info(
                u'执行的操作指令为：' + unicode(command) + u" 以及class代码为：" + str(classes) + u' category代码为：' + str(category))
            do_curl(timestamp, command, system, really_do)  # 执行curl 操作
            now2 = datetime.now()
            log.info(u'执行这个curl操作花费的时间为：' + str(now2 - now1))
        except BaseException as e:
            log.info(u'curl错误信息' + unicode(e))
            exit()  # 如果无法链接虚拟机则直接退出
        cache_size_total = cache_size_list[i] + cache_size_total  # 写入日志的cache_size_total指的是执行了curl的所有资源的大小总和
        log.info(
            unicode(kind_) + ' ' + unicode(category) + u'的执行了curl的资源大小总和为：' + str(cache_size_total) + u'并且写入curl_log中 ')
        curl_log = './curl_log/curl_log_' + timestamp
        if not really_do:
            x = open(curl_log, 'a')
            x.write('class=' + str(kind_) + ' category=' + str(
                category) + ' cache_size=' + str(cache_size_list[i]) + ' cache_size_total:' + str(
                cache_size_total) + '\n' + '----------------------------------------------------------------------------------' + '\n')  # 在curl_log中，——————————这个线就是一条curl_log信息的分割线
            x.flush()
        curl_one_end_time = datetime.now()
        curl_one_use_time = curl_one_end_time - curl_one_start_time
        if really_do:
            message = u'执行一个curl所话费的时间如下：执行的class为' + '\n' + str(classes) + u'category为：' + str(
                category) + u'第几个资源：' + str(
                i) + '\n' + u'url:' + url + '\t' + u'开始时间' + str(curl_one_start_time) + '\t' + u'结束时间为：' + str(
                curl_one_end_time) + '\t' + u'所花费的时间为：' + str(
                curl_one_use_time)
            log.info(message)
            curl_class_use_time_log = os.path.join(total_base_dir, 'operation_log', timestamp + 'curl_one_use_time')
            with open(curl_class_use_time_log, 'a')as f:
                f.write(message + '\n' + '-----------------------------------------' + '\n')
        i += 1
    z = 0
    if need_assert is True:  # 执行完curl 一个class+category后进行校验工作
        log.info(u"开始校验核对服务日志和重定向日志")
        while z < limit:
            cache_size_each = cache_size_list[z]
            url = cache_url_list[z]
            md5_each = md5_list[z]
            log.info(
                u'开始执行判断校验程序cache_size_each  url  md5分别为' + str(cache_size_each) + ' ' + str(url) + ' ' + str(
                    md5_each))
            time.sleep(5)
            current_time_start = datetime.now()
            assert_location_log(classes, category, url, cache_size_each, timestamp)
            current_time_end = datetime.now()
            log.info(
                u'location_log+url+md5分别为 以及开始结束的时间分别为：' + str(current_time_start) + '\t' + str(url) + ' ' + str(
                    md5_each) + '\t' + str(current_time_end) + u'执行该判断函数花费了：' + str(
                    current_time_end - current_time_start))
            current_time_start = datetime.now()
            assert_service_log(classes, category, cache_size_each, cache_size_each, md5_each, timestamp)
            current_time_end = datetime.now()
            log.info(
                u'service_log+url+md5分别为 以及开始结束的时间分别为：' + str(current_time_start) + '\t' + str(url) + ' ' + str(
                    md5_each) + '\t' + str(current_time_end) + '\t' + u'执行该判断函数花费了：' + str(
                    current_time_end - current_time_start))
            z += 1
    if really_do:
        curl_verbose_end_time = datetime.now()
        curl_verbose_use_time = curl_verbose_end_time - curl_verbose_start_time
        message = u'执行这个curl_resource_verbose class category 和用时分别为：' + '\n' + str(classes) + ' ' + str(
            category) + '\t' + u'开始时间：' + str(curl_verbose_start_time) + '\t' + u'结束时间为：' + str(
            curl_verbose_end_time) + '\t' + str(
            curl_verbose_use_time)
        log.info(message)
        curl_class_use_time_log = os.path.join(total_base_dir, 'operation_log', timestamp + 'curl_class_use_time')
        with open(curl_class_use_time_log, 'a')as f:
            f.write(message + '\n' + '-----------------------------------------' + '\n')


def curl_resource_class(timestamp, classes, limit, system, ua, need_assert,
                        really_do):
    """
    根据class的种类来curl所有的这个class下的cache资源（存放于文件中）
    :param really_do: 
    :param need_assert: 
    :param timestamp:
    :param system:
    :param ua:
    :param limit:
    :param classes:
    :return:
    """
    if classes == 0:
        for i in range(0, 5):
            curl_resource_verbose(timestamp, 0, i, limit, system, ua, need_assert, really_do)
    elif classes == 1:
        for i in range(0, 3):
            curl_resource_verbose(timestamp, 1, i, limit, system, ua, need_assert, really_do)
    elif classes == 2:
        for i in range(0, 20):
            curl_resource_verbose(timestamp, 2, i, limit, system, ua, need_assert, really_do)


def curl_all(time_stamp, limit, need_assert, really_do):
    """
    curl所有的资源
    :param really_do: 
    :param need_assert: 
    :param limit: 
    :param time_stamp: 
    :return: 
    """
    curl_resource_class(time_stamp, 0, limit, "linux", "iphone", need_assert, really_do)
    curl_resource_class(time_stamp, 1, limit, "linux", "windows", need_assert, really_do)
    curl_resource_class(time_stamp, 2, limit, "linux", "iphone", need_assert, really_do)
