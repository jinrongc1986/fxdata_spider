#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys, time
import MySQLdb
import getopt
import subprocess
# import socket, fcntl, struct
import ssh_cds
import ssh

# def get_ip(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


local_ip = '192.168.0.59'  # get_ip('br100')
# 命令行参数设置
opts, arts = getopt.getopt(sys.argv[1:], "hn:t:s:T:i:")
cachetype = "video"
times = 2
round_time = 0
seconds = 1
ipaddr = '192.168.1.106'
video_list=['http://183.134.64.20/videos/other/20170216/a2/bb/76e370a609dd1fa29e7c82f43f546e79.f4v?src=iqiyi.com',
            'http://v.stu.126.net/mooc-video/nos/mp4/2015/03/27/1322039_sd.mp4?ak=99ed7479ee303d1b1361b0ee5a4abcee95d6c4cf77bd7eeac1e8a89641d43dcd06ee968bcec1b2f450fde9b3fc79068cd9f4d31d7ce98d2c12bc713355b1f8c840a6759a00e64c107587394a0b73bfaa90b601143824cf18b58a69ea00438816e2c4caba0e116581c14e4824cb46dc107feb6d0bf73a0d052df948b3525aefb09eed6bb2ffe8530b0f8655d97b53dc6197cbdc8f6a5d1563323094d2340ba3cf2919f5e4aded4ea11a82dd96c04efc1a',
            'http://112.17.4.15/youku/6571926CC6C3474A5940A623F/030002060058B6C060FD7C011BA6A92E5DFA92-ACD8-9369-6470-2394B4ED27B2.flv?sid=04885294912141063e541_00&sign=be6cf588cc4a8f15ca53181ced4de934&ctype=10',
            'http://mov.bn.netease.com/open-movie/nos/flv/2017/02/23/SCD1UTA29_hd.flv',
            ]
for op, value in opts:
    if op == "-n":
        times = value
        times = int(times)
    elif op == "-t":
        cachetype = value
    elif op == "-i":
        ipaddr = value
    elif op == "-T":
        round_time = value
        round_time = int(round_time)
    elif op == "-s":
        seconds = value
        seconds = int(seconds)
    elif op == "-h":
        print "支持循环次数,默认2次: -n  X"
        print "支持video,http,mobile类型选择,默认video: -t XXX"
        print "支持每个curl间的等待时间选择，单位为秒，默认为1秒: -s x"
        sys.exit()

cachefile = cachetype + '_cache'
logfile = cachetype + '_service_log'

# 设置默认编码为UTF-8，否则从数据库读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')

# 初始化数据库、防火墙信息
querycmd = "cat /etc/sysconfig/iptables"
execmd = "sed -i '6i -A INPUT -s %s -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/sysconfig/iptables" % local_ip
ssh_cds.cds_init(querycmd, execmd, ipaddr, local_ip)

# 连接数据库
conn = MySQLdb.Connection(host=ipaddr, user="root", passwd="0rd1230ac", charset="UTF8")
conn.select_db('cache')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

# 检查icached capture uri数目
ssh_cmd_icached = '/home/icache/icached debug'
ssh_result = ssh.main(ssh_cmd_icached)
cap_uri_str = int(ssh_result.split('capture uri:')[1].split("\n")[0].strip(" "))

# 启动时间
ISOTIMEFORMAT = '%Y-%m-%d %X'
print 'start curl at time:'
starttime = time.strftime(ISOTIMEFORMAT, time.localtime())
print starttime

# 执行curl动作
sql_query = "select uri from " + cachefile
print 'sqi is      ' + sql_query
cursor.execute(sql_query)
results = cursor.fetchall()
# print results
url_num = len(results)
print 'total uri is %d' % url_num
for i in range(times):
    print 'round : %d' % (i + 1)
    print 'running...'
    percent = 0
    count = 1
    for result in results:
        # uri = result['uri']
        uri=video_list[count]
        cmd = "curl -o /dev/null -L '" + uri + "' --user-agent 'iphone'" + ' --limit-rate 5M'
        print 'cmd_command:     ' + cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(seconds)
        percent = 1.0 * count / url_num * 100
        sys.stdout.write('\rcomplete percent:%10.4s%s' % (str(percent), '%'))
        sys.stdout.flush()
        # python 3.0方式
        # print ('complete percent:%10.4s%s'%(str(percent),'%'),end='\r')
        count += 1
    print '\nround %d success' % (i + 1)
    print 'wait for %d second' % round_time
    time.sleep(round_time)
# 准备执行结果比较
print 'stop curl & wait for result...'
time.sleep(10)
curl_num = times * len(results)

# 检查icached capture uri最新数目,并计算curl期间的uri数量
ssh_cmd_icached = '/home/icache/icached debug'
ssh_result = ssh.main(ssh_cmd_icached)
cap_uri_end = int(ssh_result.split('capture uri:')[1].split("\n")[0].strip(" "))
cap_uri_num = cap_uri_end - cap_uri_str

# 获取数据库日志条目数并比对curl执行数量，已确认服务是否全部成功
sql_query_1 = "select count(*) from " + logfile + " where create_time > '%s';" % (starttime)
cursor.execute(sql_query_1)
log_results = cursor.fetchall()
log_num = int(log_results[0]['count(*)'])

sql_query_2 = "select count(*) from location_log where create_time > '%s' and client_ip='%s';" % (starttime, ipaddr)
cursor.execute(sql_query_2)
location_results = cursor.fetchall()
location_num = int(location_results[0]['count(*)'])

if log_num == curl_num:
    print 'all %d curls successfully!' % log_num
else:
    print 'The number of curls is %d' % curl_num
    print 'The number of captured curls is %d' % cap_uri_num
    print 'The number of location is %d' % location_num
    print 'The number of log is %d' % log_num

# 关闭指针
cursor.close()

# 关闭数据库连接
conn.close()

print 'finished'
print time.strftime(ISOTIMEFORMAT, time.localtime())

