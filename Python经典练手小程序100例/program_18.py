# -*- coding: utf-8 -*-

"""
【程序18】
题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
"""

a = int(input("a = "))
n = int(input("n = "))

num_list = [0]
for i in range(1, n + 1):
    Tn = num_list[i - 1] * 10 + a
    num_list.append(Tn)
print(" + ".join(str(x) for x in num_list[1:]), "= %d" % sum(num_list))
