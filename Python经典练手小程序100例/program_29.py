# -*- coding: utf-8 -*-

"""
【程序29】
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析：使用while原句计算位数，使用递归语句将最后一位取出，将原数处以10，将新数乘以10再加上取出的数字。
"""

a = int(input('请输入一个正整数：'))


def length(n):
    l = 0
    while n >= 1:
        l += 1
        n /= 10
    return l


print(length(a))

list1 = []


def rev_print(n):
    if n < 10:
        return list1.append(str(n))
    else:
        list1.append(str(n % 10))
        n = int((n - n % 10) // 10)
        rev_print(n)


rev_print(a)
print(''.join(list1))
