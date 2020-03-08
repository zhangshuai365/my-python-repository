# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序08】
题目：输出9*9口诀。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
程序源代码1：
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, i * j), end=" ")
    print()

i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print("%d*%d=%d" % (j, i, i * j), end=" ")
        j += 1
    print(end="\n")
    i += 1
