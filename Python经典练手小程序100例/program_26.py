# -*- coding: utf-8 -*-

"""
【程序26】
题目：利用递归方法求5!。
程序分析：先定义1的阶乘为1，在定义n的阶乘=n*(n-1)!。
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('5!=%d' % factorial(5))

'''
from functools import reduce


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print('5!=%d' % factorial(5))

'''
