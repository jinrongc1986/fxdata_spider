#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = test
#author = tangtao
#time   = 2017/3/20 15:25
#Description=sched用法举例
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
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
import time
import sched

schedule = sched.scheduler(time.time, time.sleep)


def func():
    print "now is", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), " | output="


def timer(seconds_to_wait1):
    schedule.enter(3, 0, func, ())
    schedule.run()


"""
schedule是一个对象，名称是其他的都行，只要是这一号任务即可，别搞个字符串来.enter就行了。（这篇教程写得还是比较面向初学者，废话挺多）

schedule.enter(delay, priority, action, arguments)

第一个参数是一个整数或者float，代表多少秒后执行这个action任务。

第二个参数priority是优先级，0代表优先级最高，1次之，2次次之…当两个任务是预定在同一个时刻执行时，根据优先级决定谁先执行。

第三个参数就是你要执行的任务，可以简单的理解成你要执行的函数的函数名。

第四个参数是你要传入的这个定时执行的action为函数名的函数的参数，最好是用"()"括号来包起来，包起来肯定是不会出错的。
其次，当你只传入一个参数时，用括号包起来后，一定要记住再打上一个逗号。即：schedule.enter(delay, priority, action, (argument1,))
虽然看起来有有点怪，但一定要这样，否则，会出现错误，比如你不打逗号，你传入一个字符串，它会以为你传入的是一个个字符，且每个字符的地位等于一个参数。总之切记，打上逗号，就安全了。
否则会出问题的。 另外如果没有参数要传入，就直接传入空括号即可，即：schedule.enter(delay, priority, action, () )
"""
if __name__ == '__main__':
    expect_time = '2017-03-20 16:28:00'
    expect_time = datetime.datetime.strptime(expect_time, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
    wait_time = str(expect_time - current_time)
    minute = int(wait_time.split(':')[1])
    seconds = int(wait_time.split(':')[2])
    seconds_to_wait = minute * 60 + seconds
    timer(seconds_to_wait)
