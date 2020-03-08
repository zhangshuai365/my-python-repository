# -*- coding: utf-8 -*-

"""
【程序13】
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该
数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""

for n in range(100, 1001):
    i = n // 100
    j = n % 100 // 10
    k = n % 10
    if n == i + j ** 3 + k ** 3:
        print("%-5d" % n, end="")

'''
# method 2
for n in range(100, 1000):
    s = str(n)
    digit_100 = int(s[0])
    digit_10 = int(s[1])
    digit_1 = int(s[2])
    if digit_100 ** 3 + digit_10 ** 3 + digit_1 ** 3 == n:
        print("%-5d" % n, end="")
'''
