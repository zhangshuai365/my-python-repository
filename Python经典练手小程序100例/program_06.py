# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序06】
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""


def fib(n):
    a, b = 1, 1
    for i in range(0, n - 2):
        a, b = a + b, a
    return a


def fib_1(n):
    if n in [1, 2]:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    fib = []
    for n in range(1, n + 1):
        if n < 3:
            fib_item = 1
        else:
            a, b = 1, 1
            for i in range(0, n - 2):
                a, b = a + b, a
                fib_item = a
        fib.append(fib_item)
    return fib


def fib_3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs


print(fib_2(10))
