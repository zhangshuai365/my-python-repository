# -*- coding: utf-8 -*-

"""
【程序11】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列满足斐波那契数列：1,1,2,3,5,8,13,21…
"""


def num_rabbit(n):
    num = 1
    if n == 1 or n == 2:
        return num
    elif n > 0 and n % 1 == 0:
        return num_rabbit(n - 1) + num_rabbit(n - 2)
    else:
        return ("输入错误")


for month in range(1, 16):
    print("第" + str(month) + "个月的兔子总对数:", num_rabbit(month))
