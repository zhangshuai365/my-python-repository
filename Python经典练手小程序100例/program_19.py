# -*- coding: utf-8 -*-

"""
【程序19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：
对1000以内的每一个数n执行以下操作：
1. 从k=1开始，用k去整除n，若n能被k整除，则k为n的因子;
2. 直到k=n/2,判断所有因子之和是否等于n;
3. 若相等，则将n添加至目标列表。
"""

result = []
for n in range(1, 1000):
    prime = []
    for k in range(1, int(n / 2) + 1):
        if n % k == 0:
            prime.append(k)
    if (sum(prime) == n):
        result.append(n)
print(result)
