# fxdata_spider
工作需要定制的爬虫

目前第一阶段的工作内容都放在get_info_from_163文件夹中

在此文件夹中有以下几个文件夹，所存放的文件及内容介绍如下:

·curl文件夹 curl.py 主要提供curl各种资源，如curl某个特定的url，curl某个特定的class和category，curl某个特定的class

·http文件夹下的cache文件夹是根据class 和category 读取数据库中已存在的资源的url和文件大小  这个文件是由http.py生成的

kind_info是每种kind（多个curl资源组成某种kind）的url地址和总的大小，这个文件是由class_info.py生成的config

config_linux_to_curl里的内容为你所需要执行curl操作的linux机器的ip 登录帐号和密码

tools文件夹下存放链接数据库以及链接linux的函数

使用的时候直接调用根目录下的main函数即可

日志文件说明

linux_curl_log : 在什么时间 curl了什么东西，包括url 大小 class 和category 开始和结束的时候还会输出debug日志以及一共循环执行了多少次kind


原理图：

第一步：使用get_all_cache()函数 根据class 和 category 从数据库中筛选出小于10mb的资源，放入各自的文件夹中 /http/cache/各类文件

kind为各种curl指定的class和category的集合，不同的kind由不同的class和category组合而成。而他们所执行的curl的url都是上文中/http/cache中的url

第二步：使用calculate_kind函数获取没中kind所curl的资源并且写入到/kind_info/cache_service下 里面的信息包含了各种class资源的大小 和各种class+category的资源大小

第三步：输入开始时间和结束时间开始执行规律的curl操作 在执行前和执行后都获取一次debug信息 

开始的时间请务必设定为5*n+1 即第6，11，16分钟之类的，这样的话，执行第一次curl会在五分钟维度内的第一分钟后，第二次curl会在五分钟纬度内的第三分钟之后

所有执行的curl操作都写入到curl_log文件中 这个文件就是日后用来分析用的文件

目前共五个kind 每个kind分为两部分，中间间隔120秒 

固定每五分钟执行一次kind 五个kind一个循环，直到到达指定的结束时间

第四步：使用get_resource_verbose函数，从curl_log中获取每个资源执行了多少次，随后从数据库中获取该资源的大小并且写入到resource_list_verbose中

第五步：使用hot_list函数，根据次数*每个资源的大小求出总共的service_size后从大到小排序并且根据class和总榜单写入相应的文件中。