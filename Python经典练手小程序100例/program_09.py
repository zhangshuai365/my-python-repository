# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序09】
题目：要求输出国际象棋棋盘。
程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。
"""

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("█" * 2, end="")
        else:
            print('  ', end="")
    print()
