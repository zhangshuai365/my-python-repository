# -*- coding: utf-8 -*-
# Python 3.x

"""
Python经典练手小程序100例
【程序1】
题目：有1、2、3、4四个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
"""


def function_1():
    num = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (k != j and k != i and j != i):
                    print("%d%d%d" % (i, j, k), end=' ')
                    num = num + 1
    print('\n' + 'number:', num)


function_1()
