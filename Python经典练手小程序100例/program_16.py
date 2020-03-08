# -*- coding: utf-8 -*-

"""
【程序16】
题目：输出格式为 dd/mm/yyyy的日期。
程序分析：使用 time及datetime 模块。
"""

import time
import datetime

print(time.strftime('%m/%d/%Y', time.localtime()))

print(datetime.date.today())
print(datetime.date.today().strftime('%m/%d/%Y'))
print(datetime.date(2008, 8, 8))
