# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序10】
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
"""

import time


def print_time():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


for i in range(3):
    print_time()
    # 暂停一秒
    time.sleep(1)
