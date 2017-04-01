#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = wrong_statistics_by_judge
#author = tangtao
#time   = 2017/3/30 15:38
#Description=从获取的错误日志中提取数据
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

from get_info_from_163.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def statics_location_log(timestamp):
    """
    从location_log中某个采集失败了多少次并且写入到指定的文件中
    :param timestamp: 
    :return: 
    """
    global location_url
    filepath = "./judge/location_log/" + timestamp
    f = open(filepath)
    x = open(filepath + "-statistics", 'w')
    info = f.read().split('***************************************')
    account = len(info) - 1  # 未采集到的重新向日志的总和
    log.info(u'未采集到的重定向日志有' + str(account) + u'条')
    result = dict()
    file_resource_list = './kind_info/' + timestamp + '/resource_list'
    z = open(file_resource_list, 'r')
    curl_infos = z.readlines()
    for i in range(0, account):
        location_url = info[i].split()[2]  # 未采集到的重定向日志的url
        if location_url in result:
            result[location_url] += 1
        else:
            result[location_url] = 1
    result = sorted(result.iteritems(), key=lambda times: times[1], reverse=True)  # 根据total_size 从大到小排序
    for result_url in result:
        log.info(result_url[0] + '\t' + u'失败次数:' + str(result_url[1]) + '\n')
        message = result_url[0] + '\t' + u'失败次数:' + str(result_url[1]) + '\n'
        x.write(message)
    x = open(filepath + "-statistics", 'r')
    statics_infos = x.readlines()
    x = open(filepath + "-statistics", 'w')
    for statics_info in statics_infos:
        statics_info_url = statics_info.split()[0]  # 从统计日志中获取的url
        fail_times = statics_info.split()[1].replace('失败次数:', '')
        for curl_info in curl_infos:
            curl_info_url = curl_info.split()[0]
            curl_times = curl_info.split()[1].replace('times:', '')
            if statics_info_url == curl_info_url:
                fail_rate = float(fail_times) / float(curl_times) * 100
                message = statics_info_url + '\t' + u'失败次数：' + str(
                    fail_times) + '\t' + u"总的执行次数为：" + curl_times + '\t' + u'失败的概率为：' + str(fail_rate) + '%' + '\n'
                log.info(message)
                x.write(message)
    x.close()


def statics_service_log(timestamp):
    """
    从location_log中某个采集失败了多少次并且写入到指定的文件中
    :param timestamp: 
    :return: 
    """
    file_resource_list = './kind_info/' + timestamp + '/resource_list'
    z = open(file_resource_list, 'r')
    curl_infos = z.readlines()
    filepath = "./judge/service_log/" + timestamp
    f = open(filepath)
    x = open(filepath + "-statistics", 'w')
    info = f.read().split('***************************************')
    account = len(info) - 1
    log.info(u'未采集到的服务日志有' + str(account) + u'条')
    result = dict()
    for i in range(0, account):
        md5 = info[i].split()[2]
        if md5 in result:
            result[md5] += 1
        else:
            result[md5] = 1
    result = sorted(result.iteritems(), key=lambda times: times[1], reverse=True)  # 根据total_size 从大到小排序
    for md5 in result:
        log.info(md5[0] + '\t' + u'失败次数:' + str(md5[1]) + '\n')
        message = md5[0] + '\t' + u'失败次数:' + str(md5[1]) + '\n'
        x.write(message)

    # x = open(filepath + "-statistics", 'r')
    # statics_infos = x.readlines()
    # x = open(filepath + "-statistics", 'w')
    # for statics_info in statics_infos:
    #     statics_info_url = statics_info.split()[0]  # 从统计日志中获取的url
    #     fail_times = statics_info.split()[1].replace('失败次数:', '')
    #     for curl_info in curl_infos:
    #         curl_info_url = curl_info.split()[0]
    #         curl_times = curl_info.split()[1].replace('times:', '')
    #         if statics_info_url == curl_info_url:
    #             fail_rate = float(fail_times) / float(curl_times) * 100
    #             message = statics_info_url + '\t' + u'失败次数：' + str(
    #                 fail_times) + '\t' + u"总的执行次数为：" + curl_times + '\t' + u'失败的概率为：' + str(fail_rate) + '%' + '\n'
    #             log.info(message)
    #             x.write(message)
    x.close()


def wrong_statistics_log(timestamp):
    """
    错误日志的信息统计
    :param timestamp: 
    :return: 
    """
    statics_service_log(timestamp)
    statics_location_log(timestamp)
