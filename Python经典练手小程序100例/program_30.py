# -*- coding: utf-8 -*-

"""
【程序30】
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：利用程序29进行逆序，再判断逆序形成的数与原数是否相等。
"""

a = int(input("请输入一个正整数："))


def rev_print(n):
    b = 0
    while n:
        b = n % 10 + b * 10
        n = (n - n % 10) // 10
    return b


print('%d%s%s' % (a, '是' if rev_print(a) == a else '不是', '回文数。'))
