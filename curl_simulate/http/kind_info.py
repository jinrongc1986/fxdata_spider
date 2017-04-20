#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = class_info
#author = tangtao
#time   = 2017/3/21 16:41
#Description=根据main函数中的kind来计算每个kind中的数据
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
import os
import sys

from curl_simulate.tools.curl_kind import kind1, kind2, kind3, kind4, kind5, kind0
from curl_simulate.tools.log.operation_log import my_log

reload(sys)
sys.setdefaultencoding('utf-8')
log = my_log()


def calculate_kind(timestamp, kind, limit):
    """
    curl了哪些资源都写入到文件中
    :param limit: 
    :param timestamp: 
    :param kind: 
    :return: 
    """
    curl_log = "./curl_log/curl_log_" + timestamp
    if not os.path.exists('./curl_log'):
        os.mkdir('./curl_log')
    f = open(curl_log, 'w')
    f.close()
    if kind == 1:
        log.info(u'现在开始执行kind1的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind1(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind1伪造curl_log成功')
    elif kind == 2:
        log.info(u'现在开始执行kind2的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind2(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind2伪造curl_log成功')
    elif kind == 3:
        log.info(u'现在开始执行kind3的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind3(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind3伪造curl_log成功')
    elif kind == 4:
        log.info(u'现在开始执行kind4的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind4(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind4伪造curl_log成功')
    elif kind == 5:
        log.info(u'现在开始执行kind5的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind5(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind5伪造curl_log成功')
    elif kind == 0:
        log.info(u'现在开始执行kind0的操作（不会执行curl操作，只是伪造数据写入curl_log中）')
        kind0(time_stamp=timestamp, is_sleep=False, limit=limit, time_line=0)
        log.info(u'kind0伪造curl_log成功')
    f = open(curl_log, 'r')
    total_cache_size = 0
    lines = f.readlines()
    is_kind_info_dir_exist = os.path.exists('./kind_info')
    if is_kind_info_dir_exist is False:
        log.info(u"kind_info 这个文件夹不存在")
        os.mkdir('./kind_info')
        log.info(u"kind_info 新建完毕")
    is_dir_exist = os.path.exists('./kind_info/' + timestamp)
    if is_dir_exist is True:
        pass
    else:
        log.info(u"kind_info 中 指定时间戳的文件不存在")
        os.mkdir('./kind_info/' + timestamp)
        log.info(u"kind_info 中 指定时间戳的文件新建完毕")
    x = open('./kind_info/' + timestamp + '/cache_service_kind' + str(kind), "w")
    message = u'删除kind' + str(kind) + u'的文件中的内容 准备写入资料'
    log.info(message)
    x.close()
    kind_info_file = './kind_info/' + timestamp + '/cache_service_kind'
    for line in lines:
        if 'curl' in line:
            url = line.split()[8]
            x = open(kind_info_file + str(kind), "a+")
            x.write(url + ' ')
            x.close()
        if 'class' in line:
            cache_size_temp = line.split()[2]
            cache_size = int(cache_size_temp.replace("cache_size=", ''))
            class_kind = line.split()[0]
            category = line.split()[1]
            total_cache_size += cache_size
            x = open(kind_info_file + str(kind), "a+")
            x.write(class_kind + ' ' + category + ' ')
            x.write("cache_size=" + str(cache_size) + '\n')
            x.close()
    x = open(kind_info_file + str(kind), "a+")
    x.write(str(total_cache_size) + '\n')
    x.write('-------------------------------------\n')
    x.close()
    message = u'kind' + unicode(kind) + u'的文件中的内容 写入完毕'
    log.info(message)
    kind_info_verbose(timestamp, kind)


def kind_info_verbose(time_stamp, kind=1):
    """
    求出每种kind的操作所涉及到的信息
    :param time_stamp: 
    :param kind: 
    :return: 
    """
    message = u'开始计算kind' + unicode(kind) + u'的文件中内容详情'
    log.info(message)
    kind_info_file = './kind_info/' + time_stamp + '/cache_service_kind'
    f = open(kind_info_file + str(kind), "a+")
    lines = f.readlines()
    httpcache_count = 0
    videocache_count = 0
    mobilecache_count = 0
    httpcache_size_total = 0
    videocache_size_total = 0
    mobilecache_size_total = 0
    http_other = 0
    http_other_size_total = 0
    http_soft = 0
    http_soft_size_total = 0
    http_zip = 0
    http_zip_size_total = 0
    http_doc = 0
    http_doc_size_total = 0
    http_pic = 0
    http_pic_size_total = 0
    mobile_android = 0
    mobile_android_size_total = 0
    mobile_ios = 0
    mobile_ios_size_total = 0
    mobile_wp = 0
    mobile_wp_size_total = 0
    video_other = 0
    video_other_size_total = 0
    video_youku = 0
    video_youku_size_total = 0
    video_miaopai = 0
    video_miaopai_size_total = 0
    video_sohu = 0
    video_sohu_size_total = 0
    video_fenghuang = 0
    video_fenghuang_size_total = 0
    video_netease = 0
    video_netease_size_total = 0
    video_ads = 0
    video_ads_size_total = 0
    video_56 = 0
    video_56_size_total = 0
    video_pptv = 0
    video_pptv_size_total = 0
    video_cctv = 0
    video_cctv_size_total = 0
    video_bilibili = 0
    video_bilibili_size_total = 0
    video_moc = 0
    video_moc_size_total = 0
    video_jidong = 0
    video_jidong_size_total = 0
    video_tecent = 0
    video_tecent_size_total = 0
    video_sina = 0
    video_sina_size_total = 0
    video_iqiyi = 0
    video_iqiyi_size_total = 0
    video_leshi = 0
    video_leshi_size_total = 0
    video_fenxing = 0
    video_fenxing_size_total = 0
    video_icntv = 0
    video_icntv_size_total = 0
    video_mongotv = 0
    video_mongotv_size_total = 0
    for line in lines:
        if len(line.split()) == 4:
            if line.split()[1] == "class=httpcache":
                httpcache_count += 1
                httpcache_size = int(line.split()[3].replace("cache_size=", ''))
                httpcache_size_total += httpcache_size
            elif line.split()[1] == "class=videocache":
                videocache_count += 1
                videocache_size = int(line.split()[3].replace("cache_size=", ''))
                videocache_size_total += videocache_size
            elif line.split()[1] == "class=mobilecache":
                mobilecache_count += 1
                mobilecache_size = int(line.split()[3].replace("cache_size=", ''))
                mobilecache_size_total += mobilecache_size
            if line.split()[1] == "class=httpcache" and line.split()[2] == 'category=0':
                http_other += 1
                http_other_size = int(line.split()[3].replace("cache_size=", ''))
                http_other_size_total += http_other_size
            if line.split()[1] == "class=httpcache" and line.split()[2] == 'category=1':
                http_soft += 1
                http_soft_size = int(line.split()[3].replace("cache_size=", ''))
                http_soft_size_total += http_soft_size
            if line.split()[1] == "class=httpcache" and line.split()[2] == 'category=2':
                http_zip += 1
                http_zip_size = int(line.split()[3].replace("cache_size=", ''))
                http_zip_size_total += http_zip_size
            if line.split()[1] == "class=httpcache" and line.split()[2] == 'category=3':
                http_doc += 1
                http_doc_size = int(line.split()[3].replace("cache_size=", ''))
                http_doc_size_total += http_doc_size
            if line.split()[1] == "class=httpcache" and line.split()[2] == 'category=4':
                http_pic += 1
                http_pic_size = int(line.split()[3].replace("cache_size=", ''))
                http_pic_size_total += http_pic_size
            if line.split()[1] == "class=mobilecache" and line.split()[2] == 'category=0':
                mobile_android += 1
                mobile_android_size = int(line.split()[3].replace("cache_size=", ''))
                mobile_android_size_total += mobile_android_size
            if line.split()[1] == "class=mobilecache" and line.split()[2] == 'category=1':
                mobile_ios += 1
                mobile_ios_size = int(line.split()[3].replace("cache_size=", ''))
                mobile_ios_size_total += mobile_ios_size
            if line.split()[1] == "class=mobilecache" and line.split()[2] == 'category=2':
                mobile_wp += 1
                mobile_wp_size = int(line.split()[3].replace("cache_size=", ''))
                mobile_wp_size_total += mobile_wp_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=0':
                video_other += 1
                video_other_size = int(line.split()[3].replace("cache_size=", ''))
                video_other_size_total += video_other_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=1':
                video_youku += 1
                video_youku_size = int(line.split()[3].replace("cache_size=", ''))
                video_youku_size_total += video_youku_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=2':
                video_miaopai += 1
                video_miaopai_size = int(line.split()[3].replace("cache_size=", ''))
                video_miaopai_size_total += video_miaopai_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=3':
                video_sohu += 1
                video_sohu_size = int(line.split()[3].replace("cache_size=", ''))
                video_sohu_size_total += video_sohu_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=4':
                video_fenghuang += 1
                video_fenghuang_size = int(line.split()[3].replace("cache_size=", ''))
                video_fenghuang_size_total += video_fenghuang_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=5':
                video_netease += 1
                video_netease_size = int(line.split()[3].replace("cache_size=", ''))
                video_netease_size_total += video_netease_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=6':
                video_ads += 1
                video_ads_size = int(line.split()[3].replace("cache_size=", ''))
                video_ads_size_total += video_ads_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=7':
                video_56 += 1
                video_56_size = int(line.split()[3].replace("cache_size=", ''))
                video_56_size_total += video_56_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=8':
                video_pptv += 1
                video_pptv_size = int(line.split()[3].replace("cache_size=", ''))
                video_pptv_size_total += video_pptv_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=9':
                video_cctv += 1
                video_cctv_size = int(line.split()[3].replace("cache_size=", ''))
                video_cctv_size_total += video_cctv_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=10':
                video_bilibili += 1
                video_bilibili_size = int(line.split()[3].replace("cache_size=", ''))
                video_bilibili_size_total += video_bilibili_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=11':
                video_moc += 1
                video_moc_size = int(line.split()[3].replace("cache_size=", ''))
                video_moc_size_total += video_moc_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=12':
                video_jidong += 1
                video_jidong_size = int(line.split()[3].replace("cache_size=", ''))
                video_jidong_size_total += video_jidong_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=13':
                video_tecent += 1
                video_tecent_size = int(line.split()[3].replace("cache_size=", ''))
                video_tecent_size_total += video_tecent_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=14':
                video_sina += 1
                video_sina_size = int(line.split()[3].replace("cache_size=", ''))
                video_sina_size_total += video_sina_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=15':
                video_iqiyi += 1
                video_iqiyi_size = int(line.split()[3].replace("cache_size=", ''))
                video_iqiyi_size_total += video_iqiyi_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=16':
                video_leshi += 1
                video_leshi_size = int(line.split()[3].replace("cache_size=", ''))
                video_leshi_size_total += video_leshi_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=17':
                video_fenxing += 1
                video_fenxing_size = int(line.split()[3].replace("cache_size=", ''))
                video_fenxing_size_total += video_fenxing_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=18':
                video_icntv += 1
                video_icntv_size = int(line.split()[3].replace("cache_size=", ''))
                video_icntv_size_total += video_icntv_size
            if line.split()[1] == "class=videocache" and line.split()[2] == 'category=19':
                video_mongotv += 1
                video_mongotv_size = int(line.split()[3].replace("cache_size=", ''))
                video_mongotv_size_total += video_mongotv_size
    f.write('httpcache:' + str(httpcache_count) + ' total_size:' + str(httpcache_size_total / 1024 / 1024) + 'mb\n')
    message = u'kind' + unicode(kind) + u'中httpcache执行了' + unicode(httpcache_count) + u'次'
    log.info(message)
    f.write(
        'mobilecache:' + str(mobilecache_count) + ' total_size:' + str(mobilecache_size_total / 1024 / 1024) + 'mb\n')
    message = u'kind' + unicode(kind) + u'中mobilecache执行了' + unicode(httpcache_count) + u'次'
    log.info(message)
    f.write('videocache:' + str(videocache_count) + ' total_size:' + str(videocache_size_total / 1024 / 1024) + 'mb\n')
    message = u'kind' + unicode(kind) + u'videocache' + unicode(httpcache_count) + u'次'
    log.info(message)
    f.write('-----------\n')

    if http_other != 0:
        f.write('http_other:' + str(http_other) + ' total_size:' + str(http_other_size_total / 1024 / 1024) + 'mb\n')
    if http_soft != 0:
        f.write('http_soft:' + str(http_soft) + ' total_size:' + str(http_soft_size_total / 1024 / 1024) + 'mb\n')
    if http_zip != 0:
        f.write('http_zip:' + str(http_zip) + ' total_size:' + str(http_zip_size_total / 1024 / 1024) + 'mb\n')
    if http_doc != 0:
        f.write('http_doc:' + str(http_doc) + ' total_size:' + str(http_doc_size_total / 1024 / 1024) + 'mb\n')
    if http_pic != 0:
        f.write('http_pic:' + str(http_pic) + ' total_size:' + str(http_pic_size_total / 1024 / 1024) + 'mb\n')
    if mobile_android != 0:
        f.write('mobile_android:' + str(mobile_android) + ' total_size:' + str(
            mobile_android_size_total / 1024 / 1024) + 'mb\n')
    if mobile_ios != 0:
        f.write('mobile_ios:' + str(mobile_ios) + ' total_size:' + str(mobile_ios_size_total / 1024 / 1024) + 'mb\n')
    if mobile_wp != 0:
        f.write('mobile_wp:' + str(mobile_wp) + ' total_size:' + str(mobile_wp_size_total / 1024 / 1024) + 'mb\n')
    if video_other != 0:
        f.write('video_other:' + str(video_other) + ' total_size:' + str(video_other_size_total / 1024 / 1024) + 'mb\n')
    if video_youku != 0:
        f.write('video_youku:' + str(video_youku) + ' total_size:' + str(video_youku_size_total / 1024 / 1024) + 'mb\n')
    if video_miaopai != 0:
        f.write('video_miaopai:' + str(video_miaopai) + ' total_size:' + str(
            video_miaopai_size_total / 1024 / 1024) + 'mb\n')
    if video_sohu != 0:
        f.write('video_sohu:' + str(video_sohu) + ' total_size:' + str(video_sohu_size_total / 1024 / 1024) + 'mb\n')
    if video_fenghuang != 0:
        f.write('video_fenghuang:' + str(video_fenghuang) + ' total_size:' + str(
            video_fenghuang_size_total / 1024 / 1024) + 'mb\n')
    if video_netease != 0:
        f.write('video_netease:' + str(video_netease) + ' total_size:' + str(
            video_netease_size_total / 1024 / 1024) + 'mb\n')
    if video_ads != 0:
        f.write('video_ads:' + str(video_ads) + ' total_size:' + str(video_ads_size_total / 1024 / 1024) + 'mb\n')
    if video_56 != 0:
        f.write('video_56:' + str(video_56) + ' total_size:' + str(video_56_size_total / 1024 / 1024) + 'mb\n')
    if video_pptv != 0:
        f.write('video_pptv:' + str(video_pptv) + ' total_size:' + str(video_pptv_size_total / 1024 / 1024) + 'mb\n')
    if video_cctv != 0:
        f.write('video_cctv:' + str(video_cctv) + ' total_size:' + str(video_cctv_size_total / 1024 / 1024) + 'mb\n')
    if video_bilibili != 0:
        f.write('video_bilibili:' + str(video_bilibili) + ' total_size:' + str(
            video_bilibili_size_total / 1024 / 1024) + 'mb\n')
    if video_moc != 0:
        f.write('video_moc:' + str(video_moc) + ' total_size:' + str(video_moc_size_total / 1024 / 1024) + 'mb\n')
    if video_jidong != 0:
        f.write(
            'video_jidong:' + str(video_jidong) + ' total_size:' + str(video_jidong_size_total / 1024 / 1024) + 'mb\n')
    if video_tecent != 0:
        f.write(
            'video_tecent:' + str(video_tecent) + ' total_size:' + str(video_tecent_size_total / 1024 / 1024) + 'mb\n')
    if video_sina != 0:
        f.write('video_sina:' + str(video_sina) + ' total_size:' + str(video_sina_size_total / 1024 / 1024) + 'mb\n')
    if video_iqiyi != 0:
        f.write('video_iqiyi:' + str(video_iqiyi) + ' total_size:' + str(video_iqiyi_size_total / 1024 / 1024) + 'mb\n')
    if video_leshi != 0:
        f.write('video_leshi:' + str(video_leshi) + ' total_size:' + str(video_leshi_size_total / 1024 / 1024) + 'mb\n')
    if video_fenxing != 0:
        f.write('video_fenxing:' + str(video_fenxing) + ' total_size:' + str(
            video_fenxing_size_total / 1024 / 1024) + 'mb\n')
    if video_icntv != 0:
        f.write('video_icntv:' + str(video_icntv) + ' total_size:' + str(video_icntv_size_total / 1024 / 1024) + 'mb\n')
    if video_mongotv != 0:
        f.write('video_mongotv:' + str(video_mongotv) + ' total_size:' + str(
            video_mongotv_size_total / 1024 / 1024) + 'mb\n')
