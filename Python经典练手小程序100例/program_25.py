# -*- coding: utf-8 -*-

"""
【程序25】
题目：求1+2!+3!+...+20!的和。
程序分析：先定义一个阶乘的函数，再使用循环语句进行20以内阶乘的求和。
"""

result = 0
factorial = 1
for i in range(1, 21):
    factorial *= i
    result += factorial
print('1+2!+3!+...+20!=%d' % result)

'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = 0
for i in range(1, 21):
    result = result + factorial(i)
print('1+2!+3!+...+20!=%d' % result)
'''
