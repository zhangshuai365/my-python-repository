# -*- coding: utf-8 -*-

"""
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此
数不是素数，反之是素数。
"""

from math import sqrt

a = []
for i in range(101, 201):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        a.append(i)

print("素数个数：", len(a))
for x in a: print(x, end=" ")
