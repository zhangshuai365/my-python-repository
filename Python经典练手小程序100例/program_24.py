# -*- coding: utf-8 -*-

"""
【程序24】
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：分子与分母的变化规律均为斐波那契数列。
"""


def fun(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fun(n - 1) + fun(n - 2)


list1 = []

for i in range(20):
    list1.append(fun(i + 1) / fun(i))

print("sum:%.4f" % (sum(list1)))
