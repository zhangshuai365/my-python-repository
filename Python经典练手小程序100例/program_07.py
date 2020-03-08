# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序07】
题目： 将一个列表的数据复制到另一个列表中。
程序分析：若采用直接赋值，当新的列表的值变动时，旧列表也发生改变，要避免发生，有一些方法。
"""

a = [1, 2, 3]
b = a * 1
b[1] = 0
print(a)

a = [1, 2, 3]
b = a[:]
b[1] = 0
print(a)

a = [1, 2, 3]
for i in range(len(a)):
    b[i] = a[i]
b[1] = 0
print(a)

a = [1, 2, 3]
b = []
b.extend(a)
b[1] = 0
print(a)

import copy

a = [1, 2, 3]
b = a.copy()
b[1] = 0
print(a)

a = [1, 2, 3]
b = [i for i in a]
b[1] = 0
print(a)

a = [1, 2, 3, 4, 5]
b = ["A", "B", a]
c = b
d = b[:]
c[0] = "C"
d[0] = "D"
d[2][0] = "x"
print(b)

a = [1, 2, 3, 4, 5]
b = ["A", "B", a]
e = b.copy()
e[0] = "D"
e[2][0] = "x"
print(b)

a = [1, 2, 3, 4, 5]
b = ["A", "B", a]
f = [i for i in b]
f[0] = "D"
f[2][0] = "x"
print(b)

a = [1, 2, 3, 4, 5]
b = ["A", "B", a]
g = copy.deepcopy(b)
g[0] = "D"
g[2][0] = "x"
print(b)
