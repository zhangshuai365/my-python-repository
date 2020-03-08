# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序05】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

# 程序源代码1(选择法)：
L = []
num = 5
for i in range(num):
    x = int(input('integer:\n'))
    L.append(x)

for i in range(0, num - 1):
    for j in range(0, num - i - 1):
        if L[j + 1] < L[j]:
            L[j + 1], L[j] = L[j], L[j + 1]
print(L)

'''
# 程序源代码2(冒泡法)：
L = []
for i in range(3):
    x = int(input('integer:\n'))
    L.append(x)
L.sort()
print(L)
'''

'''
# 程序源代码3：
L = []
num = 5
for i in range(num):
    x = int(input('integer:\n'))
    L.append(x)

for i in range(0, num):
    for j in range(i + 1, num):
        if L[i] > L[j]:
            L[j], L[i] = L[i], L[j]
print(L)
'''
